#!/usr/bin/env -S deno run --allow-net --allow-read --allow-write --allow-env --allow-sys

/**
 * Deno wrapper for the Express A2A Server with CLI endpoints
 *
 * This file runs the Express server from a2a_server.ts using Deno's Node.js compatibility.
 * This approach leverages the existing, fully-functional A2A protocol implementation
 * while running in the Deno runtime. Also provides CLI endpoints for the React CLI.
 */

import { getTimestepPaths } from "./utils.ts";
import { listModels } from "./api/modelsApi.ts";
import { listContexts } from "./api/contextsApi.ts";
import { listApiKeys } from "./api/settings/apiKeysApi.ts";
import { listMcpServers } from "./api/settings/mcpServersApi.ts";
import { listTraces } from "./api/tracesApi.ts";
import { listTools } from "./api/toolsApi.ts";

// Get timestep configuration paths
const timestepPaths = getTimestepPaths();

// Start CLI endpoints server for the React CLI
const cliPort = 3000;
console.log(`🌐 Starting CLI endpoints server on port ${cliPort}`);

Deno.serve({ port: cliPort }, async (req: Request) => {
  const url = new URL(req.url);

  // Add CORS headers
  const headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Content-Type": "application/json",
  };

  if (req.method === "OPTIONS") {
    return new Response(null, { status: 200, headers });
  }

  try {
    if (url.pathname === "/agents") {
      // Read agents from timestep config
      try {
        const agentsContent = await Deno.readTextFile(timestepPaths.agentsConfig);
        const lines = agentsContent.split('\n').filter(line => line.trim());
        const agents = lines.map(line => {
          try {
            return JSON.parse(line);
          } catch {
            return null;
          }
        }).filter(Boolean);

        return new Response(JSON.stringify(agents), {
          status: 200,
          headers
        });
      } catch (error) {
        return new Response(JSON.stringify({
          error: `Agents configuration not found at: ${timestepPaths.agentsConfig}`
        }), {
          status: 404,
          headers
        });
      }
    }

    // For other endpoints, return placeholder data
    if (url.pathname === "/chats") {
      try {
        const contextsResponse = await listContexts();
        return new Response(JSON.stringify(contextsResponse.data), {
          status: 200,
          headers
        });
      } catch (error) {
        return new Response(JSON.stringify({
          error: error instanceof Error ? error.message : "Failed to fetch contexts"
        }), {
          status: 500,
          headers
        });
      }
    }

    if (url.pathname === "/models") {
      try {
        const modelsResponse = await listModels();
        return new Response(JSON.stringify(modelsResponse.data), {
          status: 200,
          headers
        });
      } catch (error) {
        return new Response(JSON.stringify({
          error: error instanceof Error ? error.message : "Failed to fetch models"
        }), {
          status: 500,
          headers
        });
      }
    }

    if (url.pathname === "/tools") {
      try {
        const toolsResponse = await listTools();
        return new Response(JSON.stringify(toolsResponse.data), {
          status: 200,
          headers
        });
      } catch (error) {
        return new Response(JSON.stringify({
          error: error instanceof Error ? error.message : "Failed to fetch tools"
        }), {
          status: 500,
          headers
        });
      }
    }

    if (url.pathname === "/traces") {
      try {
        const tracesResponse = await listTraces();
        return new Response(JSON.stringify(tracesResponse.data), {
          status: 200,
          headers
        });
      } catch (error) {
        return new Response(JSON.stringify({
          error: error instanceof Error ? error.message : "Failed to fetch traces"
        }), {
          status: 500,
          headers
        });
      }
    }

    if (url.pathname === "/settings/api-keys") {
      try {
        const apiKeysResponse = await listApiKeys();
        return new Response(JSON.stringify(apiKeysResponse.data), {
          status: 200,
          headers
        });
      } catch (error) {
        return new Response(JSON.stringify({
          error: error instanceof Error ? error.message : "Failed to fetch API keys"
        }), {
          status: 500,
          headers
        });
      }
    }

    if (url.pathname === "/settings/mcp-servers") {
      try {
        const mcpServersResponse = await listMcpServers();
        return new Response(JSON.stringify(mcpServersResponse.data), {
          status: 200,
          headers
        });
      } catch (error) {
        return new Response(JSON.stringify({
          error: error instanceof Error ? error.message : "Failed to fetch MCP servers"
        }), {
          status: 500,
          headers
        });
      }
    }

    return new Response("Not found", { status: 404, headers });
  } catch (error) {
    return new Response(JSON.stringify({
      error: error instanceof Error ? error.message : "Internal server error"
    }), {
      status: 500,
      headers
    });
  }
});

// Import the Express app from a2a_server.ts
// Note: We need to use dynamic import since a2a_server.ts uses ES modules
const { serverMain } = await import("./api/a2a_server.ts");
// Import the MCP server class
const { StatefulMCPServer } = await import("./api/mcp_server.ts");

console.log("🚀 Starting A2A Agent Server with Deno + Express");
console.log("📦 Using Express server from a2a_server.ts");

// Start the A2A server
serverMain();

// Start the MCP server
const mcpPort = Number(Deno.env.get("MCP_SERVER_PORT") ?? 8000);
const mcpServer = new StatefulMCPServer(mcpPort);
mcpServer.run().catch((error: Error) => {
  console.error("Failed to start MCP server:", error);
});