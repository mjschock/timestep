import express from "express";
// import { v4 as uuidv4 } from "uuid";
import type { AgentCard, AgentSkill } from "@a2a-js/sdk";
import { Task } from "@a2a-js/sdk";
import {
  TaskStore,
} from "@a2a-js/sdk/server";
import { A2AExpressApp } from "@a2a-js/sdk/server/express";
import { TimestepAIAgentExecutor } from "../core/agent_executor.js";
import { ContextAwareRequestHandler } from "./context_aware_request_handler.js";
import * as fs from 'node:fs';
import process from 'node:process';
import { getTimestepPaths } from "../utils.js";

// Get timestep configuration paths
const timestepPaths = getTimestepPaths();

// Load app configuration
const appConfigPath = timestepPaths.appConfig;
if (!fs.existsSync(appConfigPath)) {
    throw new Error(`App configuration file not found. Expected at: ${appConfigPath}`);
}
const APP_CONFIG = JSON.parse(fs.readFileSync(appConfigPath, 'utf8'));

// Load all agents configuration
const agentsConfigPath = timestepPaths.agentsConfig;
if (!fs.existsSync(agentsConfigPath)) {
    throw new Error(`Agents configuration file not found. Expected at: ${agentsConfigPath}`);
}
const agentsConfigContent = fs.readFileSync(agentsConfigPath, 'utf8');
const lines = agentsConfigContent.split('\n').filter(line => line.trim());

// Create agent lookup map by ID
const AGENTS_BY_ID: { [id: string]: any } = {};
for (const line of lines) {
    const agent = JSON.parse(line);
    AGENTS_BY_ID[agent.id] = agent;
}

// Get the default agent configuration for backward compatibility
const AGENT_CONFIG = AGENTS_BY_ID[APP_CONFIG.defaultAgentId];
if (!AGENT_CONFIG) {
    throw new Error(`Agent with ID ${APP_CONFIG.defaultAgentId} not found in agents.jsonl`);
}

// Custom task store with detailed logging
class LoggingTaskStore implements TaskStore {
  private store: Map<string, Task> = new Map();

  async load(taskId: string): Promise<Task | undefined> {
    console.log(`📋 TaskStore.load(${taskId})`);
    const entry = this.store.get(taskId);
    if (entry) {
      console.log(`📋 TaskStore.load(${taskId}) -> FOUND:`, {
        id: entry.id,
        contextId: entry.contextId,
        kind: entry.kind,
        status: entry.status
      });
      // Return copies to prevent external mutation
      return {...entry};
    } else {
      console.log(`📋 TaskStore.load(${taskId}) -> NOT FOUND`);
      console.log(`📋 TaskStore current keys:`, Array.from(this.store.keys()));
      return undefined;
    }
  }

  async save(task: Task): Promise<void> {
    console.log(`📋 TaskStore.save(${task.id})`, {
      id: task.id,
      contextId: task.contextId,
      kind: task.kind,
      status: task.status
    });
    // Store copies to prevent internal mutation if caller reuses objects
    this.store.set(task.id, {...task});
    console.log(`📋 TaskStore.save(${task.id}) -> SAVED`);
    console.log(`📋 TaskStore current keys after save:`, Array.from(this.store.keys()));
  }
}

// Context-aware request handler is now imported from ./context_aware_request_handler

// 1. Define agent skills
const helloSkill: AgentSkill = {
  id: 'hello_world',
  name: 'Returns hello world',
  description: 'just returns hello world',
  tags: ['hello world'],
  examples: ['hi', 'hello world'],
};


// 2. Define agent cards

// This will be the authenticated extended agent card
// It includes the additional 'extendedSkill'
// const extendedAgentCard: AgentCard = {
//   ...publicAgentCard,
//   name: `${AGENT_CONFIG.name} - Extended Edition`,
//   description: `The full-featured ${AGENT_CONFIG.name.toLowerCase()} for authenticated users.`,
//   version: '1.0.1',
//   skills: [helloSkill, extendedSkill],
// };

// 3. Server setup with agent-specific routing
const agentExecutor = new TimestepAIAgentExecutor();
// Use a shared task store to ensure tasks are properly managed across all handlers
const sharedTaskStore = new LoggingTaskStore();

// Create the main Express app
const mainApp = express();

// Create agent-specific handlers and mount them under /agents/{agentId}
for (const [agentId, agentConfig] of Object.entries(AGENTS_BY_ID)) {
  // Create public agent card for this agent
  const publicAgentCard: AgentCard = {
    name: agentConfig.name,
    description: `A helpful AI agent powered by ${agentConfig.name}`,
    url: `http://localhost:${APP_CONFIG.a2aServerPort}/agents/${agentId}/`,
    version: '1.0.0',
    protocolVersion: '0.3.0',
    preferredTransport: 'JSONRPC',
    defaultInputModes: ['text'],
    defaultOutputModes: ['text'],
    capabilities: { streaming: true },
    skills: [helloSkill],
    supportsAuthenticatedExtendedCard: true,
  };

  // Create context-aware request handlers for this agent
  const requestHandler = new ContextAwareRequestHandler(
    agentId,
    publicAgentCard,
    sharedTaskStore,
    agentExecutor
  );


  // Create A2A Express app for this agent
  const agentAppBuilder = new A2AExpressApp(requestHandler);
  const agentApp = express();
  agentAppBuilder.setupRoutes(agentApp);

  // Mount this agent's routes under /agents/{agentId}
  mainApp.use(`/agents/${agentId}`, agentApp);

  console.log(`🤖 Configured agent routes for ${agentConfig.name} at /agents/${agentId}/`);
}

const serverMain = () => {
  mainApp.listen(APP_CONFIG.a2aServerPort, () => {
    console.log(`🚀 A2A Agent Server started on http://localhost:${APP_CONFIG.a2aServerPort}`);
    console.log(`📚 Configured ${Object.keys(AGENTS_BY_ID).length} agents with routes /agents/{agentId}/`);
    console.log(`📋 Available agents: ${Object.keys(AGENTS_BY_ID).join(', ')}`);
  });
};

export { serverMain, mainApp as expressApp };

// Start the server if this file is run directly
if (import.meta.url === `file://${process.argv[1]}`) {
  serverMain();
}