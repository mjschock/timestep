import { Agent, tool } from "@openai/agents";
import { AgentConfiguration } from '@openai/agents-core';
import { z } from "zod";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { listAgents, Agent as AgentConfig } from "../api/agentsApi.js";
import { getMcpServer } from "../api/settings/mcpServersApi.js";
import { RepositoryContainer, DefaultRepositoryContainer } from "../services/backing/repositoryContainer.js";

// Load agents using the agents API
async function loadAgents(repositories?: RepositoryContainer): Promise<AgentConfig[]> {
    try {
        const response = await listAgents(repositories);
        console.log(`📋 Loaded ${response.data.length} agents from agents API`);
        return response.data;
    } catch (error) {
        console.error(`Error loading agents from API: ${error}`);
        throw new Error(`Unable to load agents: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
}


// MCP servers are now loaded dynamically via API calls

// Create agent lookup map by ID
async function createAgentsLookup(repositories?: RepositoryContainer): Promise<{ [id: string]: AgentConfig }> {
    const agents = await loadAgents(repositories);
    const agentsById: { [id: string]: AgentConfig } = {};

    for (const agent of agents) {
        agentsById[agent.id] = agent;
    }

    return agentsById;
}



// MCP client function to invoke a tool with specific server
async function invokeMcpTool(serverUrl: string, toolName: string, parameters: any, authToken?: string): Promise<string> {
    try {
        // Create transport and client with optional authentication
        const transportUrl = new URL(serverUrl);
        const transportOptions: any = {};
        
        // Add authorization header if authToken is provided
        if (authToken) {
            transportOptions.requestInit = {
                headers: {
                    'Authorization': `Bearer ${authToken}`,
                    'Accept': 'application/json, text/event-stream',
                    'Content-Type': 'application/json'
                }
            };
            // Use custom fetch that doesn't follow redirects for authenticated requests
            transportOptions.fetch = async (url: string | URL | Request, init?: RequestInit) => {
                return fetch(url, { ...init, redirect: 'manual' });
            };
        }
        
        const transport = new StreamableHTTPClientTransport(transportUrl, transportOptions);
        
        const client = new Client({
            name: "a2a-agent-executor",
            version: "1.0.0"
        }, {
            capabilities: {}
        });
        
        // Connect to the server
        await client.connect(transport);
        
        // Call the tool
        const result = await client.callTool({
            name: toolName,
            arguments: parameters
        });
        
        // Extract text content from the result
        let content = '';
        if (result.content && Array.isArray(result.content)) {
            for (const item of result.content) {
                if (item.type === 'text' && typeof item.text === 'string') {
                    content += item.text;
                }
            }
        }
        
        // Clean up
        await client.close();
        
        return content || `Tool ${toolName} executed successfully`;
    } catch (error) {
        console.error(`Error invoking MCP tool ${toolName}:`, error);
        return `Error executing tool ${toolName}: ${error instanceof Error ? error.message : String(error)}`;
    }
}

// Function to load specific tools based on toolIds - only connects to referenced servers
async function loadToolsForAgent(toolIds: string[], repositories?: RepositoryContainer): Promise<any[]> {
    const tools = [];
    
    // Group tools by MCP server - only include servers that are actually referenced
    const serverToolsMap: { [serverId: string]: { serverUrl: string, toolNames: string[], authToken?: string } } = {};

    // First pass: collect all unique server IDs
    const serverIds = new Set<string>();
    const toolsByServer: { [serverId: string]: string[] } = {};

    for (const toolId of toolIds) {
        const [serverId, toolName] = toolId.split('.');
        if (!serverId || !toolName) {
            console.warn(`⚠️  Invalid toolId format: ${toolId}. Expected format: serverId.toolName`);
            continue;
        }

        serverIds.add(serverId);
        if (!toolsByServer[serverId]) {
            toolsByServer[serverId] = [];
        }
        toolsByServer[serverId].push(toolName);
    }

    // Second pass: lookup each server and validate
    for (const serverId of serverIds) {
        const server = await getMcpServer(serverId, repositories);
        if (!server || !server.enabled) {
            console.warn(`⚠️  MCP server with ID ${serverId} not found or disabled`);
            continue;
        }

        serverToolsMap[serverId] = {
            serverUrl: server.serverUrl,
            toolNames: toolsByServer[serverId],
            authToken: server.authToken
        };
    }
    
    // Only connect to servers that have tools referenced in toolIds
    for (const [serverId, serverInfo] of Object.entries(serverToolsMap)) {
        try {
            console.log(`🔌 Connecting to MCP server ${serverId} at ${serverInfo.serverUrl} for tools: ${serverInfo.toolNames.join(', ')}`);
            
            const transportUrl = new URL(serverInfo.serverUrl);
            const transportOptions: any = {};
            
            // Add authorization header if authToken is provided
            if (serverInfo.authToken) {
                transportOptions.requestInit = {
                    headers: {
                        'Authorization': `Bearer ${serverInfo.authToken}`,
                        'Accept': 'application/json, text/event-stream',
                        'Content-Type': 'application/json'
                    }
                };
                // Use custom fetch that doesn't follow redirects for authenticated requests
                transportOptions.fetch = async (url: string | URL | Request, init?: RequestInit) => {
                    return fetch(url, { ...init, redirect: 'manual' });
                };
            }
            
            const transport = new StreamableHTTPClientTransport(transportUrl, transportOptions);
            
            const client = new Client({
                name: "a2a-agent-executor",
                version: "1.0.0"
            }, {
                capabilities: {}
            });
            
            await client.connect(transport);
            // Call list-tools only once per server
            const mcpTools = await client.listTools();
            await client.close();
            
            // Filter tools to only include the ones requested in toolIds
            for (const mcpTool of mcpTools.tools) {
                if (serverInfo.toolNames.includes(mcpTool.name)) {
                    console.log(`🔧 Loading tool: ${serverId}.${mcpTool.name}`);
                    
                    const dynamicTool = tool({
                        name: mcpTool.name,
                        description: mcpTool.description || 'No description available',
                        parameters: createZodSchemaFromJsonSchema(mcpTool.inputSchema) as z.ZodObject<any>,
                        async execute(params: any) {
                            console.log(`🔧 Executing MCP tool ${mcpTool.name} with params:`, params);
                            const result = await invokeMcpTool(serverInfo.serverUrl, mcpTool.name, params, serverInfo.authToken);
                            console.log(`🔧 MCP tool ${mcpTool.name} result:`, result);
                            return result;
                        },
                        needsApproval: true,
                    });
                    
                    tools.push(dynamicTool);
                }
            }
        } catch (error) {
            console.error(`❌ Error loading tools from MCP server ${serverId}:`, error);
        }
    }
    
    console.log(`✅ Loaded ${tools.length} tools from ${Object.keys(serverToolsMap).length} MCP servers`);
    return tools;
}

// Helper function to create Zod schema from JSON schema
function createZodSchemaFromJsonSchema(jsonSchema: any): z.ZodSchema {
    if (!jsonSchema || jsonSchema.type !== "object") {
        return z.object({});
    }

    const shape: Record<string, z.ZodSchema> = {};
    
    if (jsonSchema.properties) {
        for (const [key, prop] of Object.entries(jsonSchema.properties)) {
            const propSchema = prop as any;
            switch (propSchema.type) {
                case "string":
                    shape[key] = z.string();
                    break;
                case "number":
                    shape[key] = z.number();
                    break;
                case "boolean":
                    shape[key] = z.boolean();
                    break;
                case "array":
                    shape[key] = z.array(z.any());
                    break;
                default:
                    shape[key] = z.any();
            }
        }
    }

    return z.object(shape);
}

async function getContext(agentId: string, repositories?: RepositoryContainer) {
    console.log('🔍 Getting context for agent ID:', agentId);

    // Get the agents lookup map
    const agentsById = await createAgentsLookup(repositories);

    // Get the specific agent configuration by ID
    const context = agentsById[agentId];
    if (!context) {
        throw new Error(`Agent with ID ${agentId} not found in agents configuration`);
    }
    
    const handoffs: Agent[] = [];

    // Resolve handoff agents by their IDs and load their tools
    if (context.handoffIds && Array.isArray(context.handoffIds)) {
        for (const handoffId of context.handoffIds) {
            const handoffConfig = agentsById[handoffId];
            if (handoffConfig) {
                // Load tools for this handoff agent based on its toolIds
                const handoffTools = await loadToolsForAgent(handoffConfig.toolIds || []);
                console.log(`🔄 Loaded ${handoffTools.length} tools for handoff agent ${handoffConfig.name}`);
                
                const agent = new Agent({
                    name: handoffConfig.name,
                    handoffDescription: handoffConfig.handoffDescription,
                    instructions: handoffConfig.instructions,
                    model: handoffConfig.model,
                    modelSettings: handoffConfig.modelSettings,
                    tools: handoffTools, // ✅ Include tools for handoff agent
                });
                handoffs.push(agent);
            } else {
                console.warn(`⚠️  Handoff agent with ID ${handoffId} not found in agents configuration`);
            }
        }
    }

    return {
        model: context.model,
        name: context.name,
        instructions: context.instructions,
        handoffs: handoffs,
        modelSettings: context.modelSettings,
        toolIds: context.toolIds || [], // Include toolIds from agent configuration
    };
}

export class AgentFactory {
    repositories: RepositoryContainer;

    constructor(repositories?: RepositoryContainer) {
        this.repositories = repositories || new DefaultRepositoryContainer();
    }

    async buildAgentConfig(agentId: string) {
        const context = await getContext(agentId, this.repositories);

        // Load tools based on agent's toolIds
        const tools = await loadToolsForAgent(context.toolIds || [], this.repositories);

        const agentConfig: AgentConfiguration = {
            name: context.name,
            instructions: context.instructions,
            handoffs: context.handoffs,
            model: context.model,
            modelSettings: context.modelSettings,
            tools: tools,
            handoffDescription: '',
            mcpServers: [],
            inputGuardrails: [],
            outputGuardrails: [],
            outputType: 'text',
            toolUseBehavior: 'run_llm_again',
            resetToolChoice: true,
        };

        return {
            config: agentConfig,
            createAgent: () => this.createAgent(agentConfig)
        };
    }


    createAgent(agentConfig: AgentConfiguration) {
        // return new Agent(agentConfig);
        const agent = new Agent(agentConfig);
        return agent;
    }
}