import { Repository } from './repository.js';
import { Agent } from '../../api/agentsApi.js';
import { JsonlRepository } from './jsonlRepository.js';
import { getTimestepPaths } from '../../utils.js';
import * as fs from 'node:fs';
import * as path from 'node:path';

// Get timestep configuration paths
const timestepPaths = getTimestepPaths();

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
 * JSONL file-based implementation of AgentRepository.
 * Stores agents as JSON objects in a .jsonl file, one agent per line.
 */
export class JsonlAgentRepository extends JsonlRepository<Agent, string> implements Repository<Agent, string> {

    constructor() {
        super(timestepPaths.agentsConfig);
    }

    protected serialize(agent: Agent): string {
        return JSON.stringify(agent);
    }

    protected deserialize(line: string): Agent {
        return JSON.parse(line) as Agent;
    }

    protected getId(agent: Agent): string {
        return agent.id;
    }

    override async list(): Promise<Agent[]> {
        try {
            const agents = await super.list();
            if (agents.length > 0) {
                console.log(`📋 Loaded ${agents.length} agents from ${this.filePath}`);
                return agents;
            }
        } catch (error) {
            console.warn(`Failed to read agents configuration from '${this.filePath}': ${error}. Using default configuration.`);
        }

        // If no agents found or error reading, try to create default configuration
        // In restricted environments (like Supabase Edge Functions), this will fail gracefully
        try {
            await this.createDefaultAgentsFile();
            console.log(`📋 Created default agents configuration with ${DEFAULT_AGENTS.length} agents`);
        } catch (error) {
            console.warn(`Unable to create default configuration file (restricted environment): ${error}`);
            console.log(`📋 Using in-memory default agents configuration with ${DEFAULT_AGENTS.length} agents`);
        }

        return DEFAULT_AGENTS;
    }

    /**
     * Create the agents configuration file with default agents
     */
    private async createDefaultAgentsFile(): Promise<void> {
        try {
            // Ensure the directory exists
            const dir = path.dirname(this.filePath);
            if (!fs.existsSync(dir)) {
                fs.mkdirSync(dir, { recursive: true });
            }

            // Write the default agents as JSONL
            const lines = DEFAULT_AGENTS.map(agent => this.serialize(agent));
            await this.writeLines(lines);
            console.log(`📋 Created default agents configuration at: ${this.filePath}`);
        } catch (error) {
            console.warn(`Failed to create default agents configuration at '${this.filePath}': ${error}`);
        }
    }
}