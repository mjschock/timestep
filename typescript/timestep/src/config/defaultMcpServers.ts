/**
 * Default MCP Servers Configuration
 *
 * Centralized configuration for default MCP servers that can be used by
 * any repository implementation (JSONL, Supabase, etc.)
 */

import { McpServer } from "../api/settings/mcpServersApi.js";

/**
 * Generate default MCP servers configuration with dynamic base URL
 */
export function getDefaultMcpServers(baseUrl?: string): McpServer[] {
  // Default to localhost:8080 if no base URL provided (for backward compatibility)
  const builtinServerUrl = baseUrl
    ? `${baseUrl}/mcp_servers/00000000-0000-0000-0000-000000000000`
    : "http://localhost:8080/mcp_servers/00000000-0000-0000-0000-000000000000";

  return [
    {
      "id": "00000000-0000-0000-0000-000000000000",
      "name": "Built-in MCP Server",
      "description": "Built-in MCP server providing weather data, document tools, and thinking capabilities",
      "serverUrl": builtinServerUrl,
      "enabled": true
    },
    {
      "id": "11111111-1111-1111-1111-111111111111",
      "name": "Rube MCP Server",
      "description": "Rube MCP server for advanced automation and workflow tools",
      "serverUrl": "https://rube.app/mcp",
      "enabled": false,
      "authToken": undefined
    },
    {
      "id": "22222222-2222-2222-2222-222222222222",
      "name": "Beeper Desktop MCP Server",
      "description": "Beeper Desktop MCP server for messaging and communication tools",
      "serverUrl": "http://localhost:23373/v0/mcp",
      "enabled": false,
      "authToken": undefined
    }
  ];
}

/**
 * Get just the built-in MCP server configuration
 */
export function getBuiltinMcpServer(baseUrl?: string): McpServer {
  const builtinServerUrl = baseUrl
    ? `${baseUrl}/mcp_servers/00000000-0000-0000-0000-000000000000`
    : "http://localhost:8080/mcp_servers/00000000-0000-0000-0000-000000000000";

  return {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Built-in MCP Server",
    "description": "Built-in MCP server providing weather data, document tools, and thinking capabilities",
    "serverUrl": builtinServerUrl,
    "enabled": true
  };
}