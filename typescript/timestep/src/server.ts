#!/usr/bin/env -S deno run --allow-net --allow-read --allow-write --allow-env --allow-sys

/**
 * Express server with CLI endpoints for both Node.js and Deno
 *
 * This file runs an Express server that works in both environments.
 * It provides CLI endpoints for the React CLI and integrates with the A2A server.
 */

import express from "express";
import { readFile } from "node:fs/promises";
import { getTimestepPaths, loadAppConfig } from "./utils.js";
import { listModels } from "./api/modelsApi.js";
import { listContexts } from "./api/contextsApi.js";
import { listApiKeys } from "./api/settings/apiKeysApi.js";
import { listMcpServers } from "./api/settings/mcpServersApi.js";
import { listTraces } from "./api/tracesApi.js";
import { listTools } from "./api/toolsApi.js";

// Get timestep configuration paths and app config
const timestepPaths = getTimestepPaths();
const appConfig = loadAppConfig();

// Create Express app for CLI endpoints
const app = express();

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

// Agents endpoint
app.get("/agents", async (_req, res) => {
  try {
    const agentsContent = await readFile(timestepPaths.agentsConfig, 'utf-8');
    const lines = agentsContent.split('\n').filter(line => line.trim());
    const agents = lines.map(line => {
      try {
        return JSON.parse(line);
      } catch {
        return null;
      }
    }).filter(Boolean);

    res.json(agents);
  } catch (error) {
    res.status(404).json({
      error: `Agents configuration not found at: ${timestepPaths.agentsConfig}`
    });
  }
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

// Start the CLI endpoints server
app.listen(appConfig.cliPort, () => {
  console.log(`🌐 CLI endpoints server running on http://localhost:${appConfig.cliPort}`);
});

// Import and start the A2A server and MCP server
const { serverMain } = await import("./api/a2a_server.js");
const { StatefulMCPServer } = await import("./api/mcp_server.js");

console.log("🚀 Starting A2A Agent Server with Express");
console.log("📦 Using Express server from a2a_server.ts");

// Start the A2A server - it will use its own port configuration
serverMain();

// Start the MCP server
const mcpServer = new StatefulMCPServer(appConfig.mcpServerPort!);
mcpServer.run().catch((error: Error) => {
  console.error("Failed to start MCP server:", error);
});