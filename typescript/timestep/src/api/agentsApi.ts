/**
 * Agents API
 *
 * This module provides functions for managing agent configurations.
 * It handles loading agents from configuration files and provides defaults
 * when configuration is not available.
 */

import { getTimestepPaths } from "../utils.js";
import * as fs from 'node:fs';
import * as path from 'node:path';
import type { AgentCard, AgentSkill } from "@a2a-js/sdk";
import { TaskStore } from "@a2a-js/sdk/server";
import { AgentExecutor } from "@a2a-js/sdk/server";
import { ContextAwareRequestHandler } from "./context_aware_request_handler.js";
import { Request, Response, NextFunction } from "express";

/**
 * Represents an agent configuration
 */
export interface Agent {
  /** The agent identifier */
  id: string;
  /** The agent name */
  name: string;
  /** System instructions for the agent */
  instructions: string;
  /** Description for handoff purposes */
  handoffDescription?: string;
  /** IDs of agents this agent can hand off to */
  handoffIds?: string[];
  /** IDs of tools available to this agent */
  toolIds: string[];
  /** Model identifier to use */
  model: string;
  /** Model configuration settings */
  modelSettings: {
    temperature: number;
    [key: string]: any;
  };
}

/**
 * Response from the list agents endpoint
 */
export interface ListAgentsResponse {
  /** The object type, which is always "list" */
  object: 'list';
  /** Array of agent objects */
  data: Agent[];
}

// Default agents configuration
const DEFAULT_AGENTS: Agent[] = [
  {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Personal Assistant",
    "instructions": "# System context\nYou are part of a multi-agent system called the Agents SDK, designed to make agent coordination and execution easy. Agents uses two primary abstraction: **Agents** and **Handoffs**. An agent encompasses instructions and tools and can hand off a conversation to another agent when appropriate. Handoffs are achieved by calling a handoff function, generally named `transfer_to_<agent_name>`. Transfers between agents are handled seamlessly in the background; do not mention or draw attention to these transfers in your conversation with the user.\nYou are an AI agent acting as a personal assistant.",
    "handoffIds": ["11111111-1111-1111-1111-111111111111", "22222222-2222-2222-2222-222222222222", "33333333-3333-3333-3333-333333333333", "44444444-4444-4444-4444-444444444444", "55555555-5555-5555-5555-555555555555", "66666666-6666-6666-6666-666666666666", "77777777-7777-7777-7777-777777777777"],
    "toolIds": ["00000000-0000-0000-0000-000000000000.think"],
    "model": "ollama/gpt-oss:20b",
    "modelSettings": {"temperature": 0.0}
  },
  {
    "id": "11111111-1111-1111-1111-111111111111",
    "name": "Administrative Assistant",
    "instructions": "You must always use the tools to answer questions.",
    "handoffDescription": "An administrative assistant that can manage administrative tasks on behalf of the user.",
    "toolIds": ["00000000-0000-0000-0000-000000000000.think", "11111111-1111-1111-1111-111111111111.RUBE_CREATE_PLAN", "11111111-1111-1111-1111-111111111111.RUBE_MULTI_EXECUTE_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_BASH_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_WORKBENCH", "11111111-1111-1111-1111-111111111111.RUBE_SEARCH_TOOLS"],
    "model": "ollama/gpt-oss:20b",
    "modelSettings": {"temperature": 0.0}
  },
  {
    "id": "22222222-2222-2222-2222-222222222222",
    "name": "Communications Coordinator",
    "instructions": "You must always use the tools to answer questions.",
    "handoffDescription": "A communications coordinator that can manage communications on behalf of the user.",
    "toolIds": ["00000000-0000-0000-0000-000000000000.think", "11111111-1111-1111-1111-111111111111.RUBE_CREATE_PLAN", "11111111-1111-1111-1111-111111111111.RUBE_MULTI_EXECUTE_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_BASH_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_WORKBENCH", "11111111-1111-1111-1111-111111111111.RUBE_SEARCH_TOOLS", "22222222-2222-2222-2222-222222222222.archive_chat", "22222222-2222-2222-2222-222222222222.clear_chat_reminder", "22222222-2222-2222-2222-222222222222.download_attachment", "22222222-2222-2222-2222-222222222222.get_accounts", "22222222-2222-2222-2222-222222222222.get_chat", "22222222-2222-2222-2222-222222222222.open_in_app", "22222222-2222-2222-2222-222222222222.search_chats", "22222222-2222-2222-2222-222222222222.search_messages", "22222222-2222-2222-2222-222222222222.send_message", "22222222-2222-2222-2222-222222222222.set_chat_reminder"],
    "model": "ollama/gpt-oss:20b",
    "modelSettings": {"temperature": 0.0}
  },
  {
    "id": "33333333-3333-3333-3333-333333333333",
    "name": "Content Creator",
    "instructions": "You must always use the tools to answer questions.",
    "handoffDescription": "A content creator that can create content on behalf of the user.",
    "toolIds": ["00000000-0000-0000-0000-000000000000.think", "11111111-1111-1111-1111-111111111111.RUBE_CREATE_PLAN", "11111111-1111-1111-1111-111111111111.RUBE_MULTI_EXECUTE_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_BASH_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_WORKBENCH", "11111111-1111-1111-1111-111111111111.RUBE_SEARCH_TOOLS"],
    "model": "ollama/gpt-oss:20b",
    "modelSettings": {"temperature": 0.0}
  },
  {
    "id": "44444444-4444-4444-4444-444444444444",
    "name": "Project Manager",
    "instructions": "You must always use the tools to answer questions.",
    "handoffDescription": "A project manager that can manage projects on behalf of the user.",
    "toolIds": ["00000000-0000-0000-0000-000000000000.think", "11111111-1111-1111-1111-111111111111.RUBE_CREATE_PLAN", "11111111-1111-1111-1111-111111111111.RUBE_MULTI_EXECUTE_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_BASH_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_WORKBENCH", "11111111-1111-1111-1111-111111111111.RUBE_SEARCH_TOOLS"],
    "model": "ollama/gpt-oss:20b",
    "modelSettings": {"temperature": 0.0}
  },
  {
    "id": "55555555-5555-5555-5555-555555555555",
    "name": "Research Assistant",
    "instructions": "You must always use the tools to answer questions.",
    "handoffDescription": "A research assistant that can research on behalf of the user.",
    "toolIds": ["00000000-0000-0000-0000-000000000000.think", "11111111-1111-1111-1111-111111111111.RUBE_CREATE_PLAN", "11111111-1111-1111-1111-111111111111.RUBE_MULTI_EXECUTE_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_BASH_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_WORKBENCH", "11111111-1111-1111-1111-111111111111.RUBE_SEARCH_TOOLS"],
    "model": "ollama/gpt-oss:20b",
    "modelSettings": {"temperature": 0.0}
  },
  {
    "id": "66666666-6666-6666-6666-666666666666",
    "name": "Scheduling Coordinator",
    "instructions": "You must always use the tools to answer questions.",
    "handoffDescription": "A scheduling coordinator that can schedule appointments on behalf of the user.",
    "toolIds": ["00000000-0000-0000-0000-000000000000.think", "11111111-1111-1111-1111-111111111111.RUBE_CREATE_PLAN", "11111111-1111-1111-1111-111111111111.RUBE_MULTI_EXECUTE_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_BASH_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_WORKBENCH", "11111111-1111-1111-1111-111111111111.RUBE_SEARCH_TOOLS"],
    "model": "ollama/gpt-oss:20b",
    "modelSettings": {"temperature": 0.0}
  },
  {
    "id": "77777777-7777-7777-7777-777777777777",
    "name": "Weather Assistant",
    "instructions": "You are a weather expert that provides accurate weather forecasts and alerts. You must always use the weather tools to answer questions about weather conditions, forecasts, and alerts.",
    "handoffDescription": "A weather assistant that can provide weather forecasts and alerts for any location.",
    "toolIds": ["00000000-0000-0000-0000-000000000000.get-alerts", "00000000-0000-0000-0000-000000000000.get-forecast", "00000000-0000-0000-0000-000000000000.think", "11111111-1111-1111-1111-111111111111.RUBE_CREATE_PLAN", "11111111-1111-1111-1111-111111111111.RUBE_MULTI_EXECUTE_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_BASH_TOOL", "11111111-1111-1111-1111-111111111111.RUBE_REMOTE_WORKBENCH", "11111111-1111-1111-1111-111111111111.RUBE_SEARCH_TOOLS"],
    "model": "ollama/gpt-oss:20b",
    "modelSettings": {"temperature": 0.0}
  }
];

/**
 * Create the agents configuration file with default agents
 *
 * @param agentsConfigPath - Path to the agents configuration file
 */
function createDefaultAgentsFile(agentsConfigPath: string): void {
  try {
    // Ensure the directory exists
    const dir = path.dirname(agentsConfigPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    // Write the default agents as JSONL
    const content = DEFAULT_AGENTS.map(agent => JSON.stringify(agent)).join('\n');
    fs.writeFileSync(agentsConfigPath, content, 'utf8');
    console.log(`📋 Created default agents configuration at: ${agentsConfigPath}`);
  } catch (error) {
    console.warn(`Failed to create default agents configuration at '${agentsConfigPath}': ${error}`);
  }
}

/**
 * List all available agents
 *
 * @returns Promise resolving to the list of agents
 */
export async function listAgents(): Promise<ListAgentsResponse> {
  const timestepPaths = getTimestepPaths();
  const agentsConfigPath = timestepPaths.agentsConfig;

  let agents: Agent[] = [];

  try {
    if (fs.existsSync(agentsConfigPath)) {
      try {
        const content = fs.readFileSync(agentsConfigPath, 'utf8');
        const lines = content.split('\n').filter(line => line.trim());

        agents = lines.map(line => {
          try {
            return JSON.parse(line) as Agent;
          } catch (err) {
            console.warn(`Failed to parse agent line: ${line}`, err);
            return null;
          }
        }).filter(Boolean) as Agent[];

        console.log(`📋 Loaded ${agents.length} agents from ${agentsConfigPath}`);
      } catch (error) {
        console.warn(`Failed to read agents configuration from '${agentsConfigPath}': ${error}. Creating default configuration.`);
        createDefaultAgentsFile(agentsConfigPath);
        agents = DEFAULT_AGENTS;
      }
    } else {
      console.warn(`Agents configuration file not found at: ${agentsConfigPath}. Creating default configuration.`);
      createDefaultAgentsFile(agentsConfigPath);
      agents = DEFAULT_AGENTS;
    }
  } catch (error) {
    console.warn(`Error loading agents configuration: ${error}. Using default agents.`);
    agents = DEFAULT_AGENTS;
  }

  return {
    object: 'list',
    data: agents,
  };
}

/**
 * Retrieve a specific agent by ID
 *
 * @param agentId - The ID of the agent to retrieve
 * @returns Promise resolving to the agent details or null if not found
 */
export async function getAgent(agentId: string): Promise<Agent | null> {
  const response = await listAgents();
  return response.data.find(agent => agent.id === agentId) || null;
}

/**
 * Check if an agent is available
 *
 * @param agentId - The ID of the agent to check
 * @returns Promise resolving to true if agent exists, false otherwise
 */
export async function isAgentAvailable(agentId: string): Promise<boolean> {
  const agent = await getAgent(agentId);
  return agent !== null;
}

/**
 * Create an agent card for a specific agent
 *
 * @param agentId - The ID of the agent
 * @param serverPort - The server port for the agent URL
 * @returns Promise resolving to the agent card
 */
export async function getAgentCard(agentId: string, serverPort: number): Promise<AgentCard> {
  const agent = await getAgent(agentId);
  if (!agent) {
    throw new Error(`Agent with ID ${agentId} not found`);
  }

  // Define agent skills
  const helloSkill: AgentSkill = {
    id: 'hello_world',
    name: 'Returns hello world',
    description: 'just returns hello world',
    tags: ['hello world'],
    examples: ['hi', 'hello world'],
  };

  const publicAgentCard: AgentCard = {
    name: agent.name,
    description: `A helpful AI agent powered by ${agent.name}`,
    url: `http://localhost:${serverPort}/agents/${agentId}/`,
    version: '1.0.0',
    protocolVersion: '0.3.0',
    preferredTransport: 'JSONRPC',
    defaultInputModes: ['text'],
    defaultOutputModes: ['text'],
    capabilities: { streaming: true },
    skills: [helloSkill],
    supportsAuthenticatedExtendedCard: true,
  };

  return publicAgentCard;
}

/**
 * Create a context-aware request handler for a specific agent
 *
 * @param agentId - The ID of the agent
 * @param taskStore - The shared task store
 * @param agentExecutor - The agent executor
 * @param serverPort - The server port for the agent URL
 * @returns Promise resolving to the configured request handler
 */
export async function createAgentRequestHandler(
  agentId: string,
  taskStore: TaskStore,
  agentExecutor: AgentExecutor,
  serverPort: number
): Promise<ContextAwareRequestHandler> {
  const agent = await getAgent(agentId);
  if (!agent) {
    throw new Error(`Agent with ID ${agentId} not found`);
  }

  const agentCard = await getAgentCard(agentId, serverPort);

  return new ContextAwareRequestHandler(
    agentId,
    agentCard,
    taskStore,
    agentExecutor
  );
}

/**
 * Express route handler for listing agents
 */
export async function handleListAgents(_req: Request, res: Response): Promise<void> {
  try {
    const response = await listAgents();
    res.json(response.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : 'Failed to load agents'
    });
  }
}

/**
 * Express route handler for dynamic agent requests
 */
export async function handleAgentRequest(
  req: Request, 
  res: Response, 
  next: NextFunction,
  taskStore: TaskStore,
  agentExecutor: AgentExecutor,
  serverPort: number
): Promise<void> {
  console.log(`🔍 Dynamic route handler called for agent: ${req.params['agentId']}, method: ${req.method}, path: ${req.path}`);
  try {
    const agentId = req.params['agentId'];
    
    // Check if agent exists
    if (!(await isAgentAvailable(agentId))) {
      console.log(`❌ Agent ${agentId} not found`);
      res.status(404).json({ 
        error: 'Agent not found',
        agentId: agentId 
      });
      return;
    }
    
    // Create request handler dynamically
    const requestHandler = await createAgentRequestHandler(
      agentId, 
      taskStore, 
      agentExecutor, 
      serverPort
    );
    
    // Create A2A Express app and delegate
    const { A2AExpressApp } = await import("@a2a-js/sdk/server/express");
    const agentAppBuilder = new A2AExpressApp(requestHandler);
    const agentApp = (await import("express")).default();
    agentAppBuilder.setupRoutes(agentApp);
    
    // Delegate to the agent-specific app
    agentApp(req, res, next);
    
  } catch (error) {
    console.error(`Error handling request for agent ${req.params['agentId']}:`, error);
    res.status(500).json({ 
      error: 'Internal server error',
      message: error instanceof Error ? error.message : 'Unknown error'
    });
  }
}