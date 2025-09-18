#!/usr/bin/env -S deno run --allow-net --allow-read --allow-write --allow-env --allow-sys

/**
 * Deno-optimized Express server with CLI endpoints
 *
 * This file is specifically designed for Deno environments like Supabase Edge Functions.
 * It provides the same functionality as server.ts but with Deno-specific adaptations.
 */

// @ts-types="npm:@types/express"
import express from "express";
import type { Request, Response, NextFunction } from "express";

// Declare Deno global for TypeScript compilation
declare global {
  const Deno: any;
}

// Regular imports that work in both Node.js and Deno
import { loadAppConfig } from "./utils.js";
import { listModels } from "./api/modelsApi.js";
import { listContexts } from "./api/contextsApi.js";
import { handleListAgents, handleAgentRequest } from "./api/agentsApi.js";
import { listApiKeys } from "./api/settings/apiKeysApi.js";
import { listMcpServers } from "./api/settings/mcpServersApi.js";
import { listModelProviders } from "./api/settings/modelProvidersApi.js";
import { listTraces } from "./api/tracesApi.js";
import { listTools } from "./api/toolsApi.js";
import { TimestepAIAgentExecutor } from "./core/agentExecutor.js";
import { Task } from "@a2a-js/sdk";
import { TaskStore } from "@a2a-js/sdk/server";

// Get app config
const appConfig = loadAppConfig();

// Custom task store with detailed logging - Deno compatible
class DenoLoggingTaskStore implements TaskStore {
  private store: Map<string, Task> = new Map();

  load(taskId: string): Promise<Task | undefined> {
    console.log(`📋 DenoTaskStore.load(${taskId})`);
    const entry = this.store.get(taskId);
    if (entry) {
      console.log(`📋 DenoTaskStore.load(${taskId}) -> FOUND:`, {
        id: entry.id,
        contextId: entry.contextId,
        kind: entry.kind,
        status: entry.status
      });
      // Return copies to prevent external mutation
      return Promise.resolve({...entry});
    } else {
      console.log(`📋 DenoTaskStore.load(${taskId}) -> NOT FOUND`);
      console.log(`📋 DenoTaskStore current keys:`, Array.from(this.store.keys()));
      return Promise.resolve(undefined);
    }
  }

  save(task: Task): Promise<void> {
    console.log(`📋 DenoTaskStore.save(${task.id})`, {
      id: task.id,
      contextId: task.contextId,
      kind: task.kind,
      status: task.status
    });
    // Store copies to prevent internal mutation if caller reuses objects
    this.store.set(task.id, {...task});
    console.log(`📋 DenoTaskStore.save(${task.id}) -> SAVED`);
    console.log(`📋 DenoTaskStore current keys after save:`, Array.from(this.store.keys()));
    return Promise.resolve();
  }
}

// Create Express app for CLI endpoints and A2A server
const app = express();

// A2A server components
const agentExecutor = new TimestepAIAgentExecutor();
const sharedTaskStore = new DenoLoggingTaskStore();

// Add CORS middleware
app.use((_req: Request, res: Response, next: NextFunction) => {
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

// Parse JSON bodies
app.use(express.json());

// Version endpoint - dynamically reads from package.json
app.get("/version", async (_req: Request, res: Response) => {
  try {
    const { getVersion } = await import('./utils.js');
    const versionInfo = await getVersion();
    res.json(versionInfo);
  } catch (error) {
    res.status(500).json({
      error: error instanceof Error ? error.message : "Failed to read version information"
    });
  }
});

// Chats endpoint
app.get("/chats", async (_req: Request, res: Response) => {
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
app.get("/models", async (_req: Request, res: Response) => {
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
app.get("/tools", async (_req: Request, res: Response) => {
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
app.get("/traces", async (_req: Request, res: Response) => {
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
app.get("/settings/api-keys", async (_req: Request, res: Response) => {
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
app.get("/settings/mcp-servers", async (_req: Request, res: Response) => {
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
app.get("/settings/model-providers", async (_req: Request, res: Response) => {
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
app.use((req: Request, _res: Response, next: NextFunction) => {
  console.log(`🔍 Deno Server Request received: ${req.method} ${req.path}`);
  next();
});

// Test route first
app.get('/test-agent', (_req: Request, res: Response) => {
  console.log(`🔍 Deno test route called`);
  res.json({ message: 'Deno test route working', runtime: 'Deno' });
});

// Dynamic agent route handler - use middleware to catch all paths under /agents/:agentId
app.use('/agents/:agentId', async (req: Request, res: Response, next: NextFunction) => {
  console.log(`🔍 Deno A2A route handler called for: ${req.method} ${req.path} (originalUrl: ${req.originalUrl})`);
  await handleAgentRequest(req, res, next, sharedTaskStore, agentExecutor, appConfig.appPort!);
});

// Agents list endpoint - must come after dynamic routes to avoid conflicts
app.get("/agents", handleListAgents);

// Error handling middleware
app.use((error: Error, _req: Request, res: Response, _next: NextFunction) => {
  console.error('🔍 Deno Server Error:', error);
  res.status(500).json({
    error: error.message || "Internal server error",
    runtime: "Deno"
  });
});

// Health check endpoint for Deno environments
app.get('/health', (_req: Request, res: Response) => {
  const runtime = typeof Deno !== 'undefined' ? 'Deno' : 'Node.js';
  const version = typeof Deno !== 'undefined' ? (Deno as any).version?.deno : process.version;

  res.json({
    status: 'healthy',
    runtime,
    timestamp: new Date().toISOString(),
    version
  });
});

// Function to start the server (can be called programmatically)
export function startDenoServer(port?: number): void {
  const serverPort = port || appConfig.appPort || 8080;

  app.listen(serverPort, () => {
    console.log(`🌐 Deno Unified server running on http://localhost:${serverPort}`);
    console.log(`📚 CLI endpoints available at http://localhost:${serverPort}/`);
    console.log(`🤖 A2A agents available at http://localhost:${serverPort}/agents/{agentId}/`);
    console.log(`📚 Dynamic agent routing enabled - agents loaded on-demand`);
    const runtime = typeof Deno !== 'undefined' ? 'Deno' : 'Node.js';
    const version = typeof Deno !== 'undefined' ? (Deno as any).version?.deno : process.version;
    console.log(`🦕 Runtime: ${runtime} ${version}`);
    console.log(`⚡ Health check: http://localhost:${serverPort}/health`);
  });
}

// Export the Express app for use in other modules (like Supabase Edge Functions)
export { app as denoApp };

// Auto-start server if run directly
if (import.meta.main) {
  console.log('🦕 Starting Timestep Deno Server...');

  // Start the main Express server
  startDenoServer();

  // MCP server is now integrated into the main server, no separate server needed
}