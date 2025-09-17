#!/usr/bin/env -S deno run --allow-net --allow-read --allow-write --allow-env --allow-sys

/**
 * Express server with CLI endpoints for both Node.js and Deno
 *
 * This file runs an Express server that works in both environments.
 * It provides CLI endpoints for the React CLI and integrates with the A2A server.
 */

import express from "express";
import { loadAppConfig } from "./utils.js";
import { listModels } from "./api/modelsApi.js";
import { listContexts } from "./api/contextsApi.js";
import { handleListAgents, handleAgentRequest } from "./api/agentsApi.js";
import { listApiKeys } from "./api/settings/apiKeysApi.js";
import { listMcpServers } from "./api/settings/mcpServersApi.js";
import { listModelProviders } from "./api/settings/modelProvidersApi.js";
import { listTraces } from "./api/tracesApi.js";
import { listTools } from "./api/toolsApi.js";
import { TimestepAIAgentExecutor } from "./core/agent_executor.js";
import { Task } from "@a2a-js/sdk";
import { TaskStore } from "@a2a-js/sdk/server";

// Get app config
const appConfig = loadAppConfig();

// Custom task store with detailed logging
class LoggingTaskStore implements TaskStore {
  private store: Map<string, Task> = new Map();

  load(taskId: string): Promise<Task | undefined> {
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
      return Promise.resolve({...entry});
    } else {
      console.log(`📋 TaskStore.load(${taskId}) -> NOT FOUND`);
      console.log(`📋 TaskStore current keys:`, Array.from(this.store.keys()));
      return Promise.resolve(undefined);
    }
  }

  save(task: Task): Promise<void> {
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
    return Promise.resolve();
  }
}

// Create Express app for CLI endpoints and A2A server
const app = express();

// A2A server components
const agentExecutor = new TimestepAIAgentExecutor();
const sharedTaskStore = new LoggingTaskStore();

// Add CORS middleware
app.use((_req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.header("Access-Control-Allow-Headers", "Content-Type");

  // Handle OPTIONS requests in middleware
  if (_req.method === 'OPTIONS') {
    res.sendStatus(200);
    return;
  }

  next();
});

// Chats endpoint
app.get("/chats", async (_req, res) => {
  try {
    const contextsResponse = await listContexts();
    res.json(contextsResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch contexts"
    });
  }
});

// Models endpoint
app.get("/models", async (_req, res) => {
  try {
    const modelsResponse = await listModels();
    res.json(modelsResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch models"
    });
  }
});

// Tools endpoint
app.get("/tools", async (_req, res) => {
  try {
    const toolsResponse = await listTools();
    res.json(toolsResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch tools"
    });
  }
});

// Traces endpoint
app.get("/traces", async (_req, res) => {
  try {
    const tracesResponse = await listTraces();
    res.json(tracesResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch traces"
    });
  }
});

// API Keys endpoint
app.get("/settings/api-keys", async (_req, res) => {
  try {
    const apiKeysResponse = await listApiKeys();
    res.json(apiKeysResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch API keys"
    });
  }
});

// MCP Servers endpoint
app.get("/settings/mcp-servers", async (_req, res) => {
  try {
    const mcpServersResponse = await listMcpServers();
    res.json(mcpServersResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch MCP servers"
    });
  }
});

// Model Providers endpoint
app.get("/settings/model-providers", async (_req, res) => {
  try {
    const modelProvidersResponse = await listModelProviders();
    res.json(modelProvidersResponse.data);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to fetch model providers"
    });
  }
});

// A2A Server Routes
// Add debugging middleware
app.use((req, _res, next) => {
  console.log(`🔍 Request received: ${req.method} ${req.path}`);
  next();
});

// Test route first
app.get('/test-agent', (_req, res) => {
  console.log(`🔍 Test route called`);
  res.json({ message: 'Test route working' });
});

// Dynamic agent route handler - use middleware to catch all paths under /agents/:agentId
app.use('/agents/:agentId', async (req, res, next) => {
  console.log(`🔍 A2A route handler called for: ${req.method} ${req.path} (originalUrl: ${req.originalUrl})`);
  await handleAgentRequest(req, res, next, sharedTaskStore, agentExecutor, appConfig.appPort!);
});

// Agents list endpoint - must come after dynamic routes to avoid conflicts
app.get("/agents", handleListAgents);

// Start the unified server
app.listen(appConfig.appPort, () => {
  console.log(`🌐 Unified server running on http://localhost:${appConfig.appPort}`);
  console.log(`📚 CLI endpoints available at http://localhost:${appConfig.appPort}/`);
  console.log(`🤖 A2A agents available at http://localhost:${appConfig.appPort}/agents/{agentId}/`);
  console.log(`📚 Dynamic agent routing enabled - agents loaded on-demand`);
});

// Import and start the MCP server
const { StatefulMCPServer } = await import("./api/mcp_server.js");

// Start the MCP server
const mcpServer = new StatefulMCPServer(appConfig.mcpServerPort!);
mcpServer.run().catch((error: Error) => {
  console.error("Failed to start MCP server:", error);
});