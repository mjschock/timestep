#!/usr/bin/env -S deno run --allow-net --allow-read --allow-write --allow-env

/**
 * Deno wrapper for the Express A2A Server
 * 
 * This file runs the Express server from a2a_server.ts using Deno's Node.js compatibility.
 * This approach leverages the existing, fully-functional A2A protocol implementation
 * while running in the Deno runtime.
 */

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