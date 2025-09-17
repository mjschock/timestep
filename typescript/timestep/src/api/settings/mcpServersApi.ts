/**
 * MCP Servers API
 * 
 * This module provides TypeScript interfaces and functions for managing MCP (Model Context Protocol)
 * servers in the Timestep application.
 */

// TypeScript interfaces for MCP Servers

/**
 * Represents an MCP server configuration
 */
export interface McpServer {
  /** Unique identifier for the MCP server */
  id: string;
  /** The name/label for the MCP server */
  name: string;
  /** Description of the MCP server */
  description: string;
  /** The URL of the MCP server */
  serverUrl: string;
  /** Whether the MCP server is enabled */
  enabled: boolean;
  /** Authentication token for the MCP server */
  authToken?: string;
}

/**
 * Response from the list MCP servers endpoint
 */
export interface ListMcpServersResponse {
  /** The object type, which is always "list" */
  object: 'list';
  /** Array of MCP server objects */
  data: McpServer[];
}

import { getTimestepPaths } from "../../utils.js";
import * as fs from 'node:fs';
import * as path from 'node:path';

// Default MCP servers configuration
const DEFAULT_MCP_SERVERS: McpServer[] = [
  {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Built-in MCP Server",
    "description": "Built-in MCP server providing weather data, document tools, and thinking capabilities",
    "serverUrl": "http://localhost:8000/mcp",
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

/**
 * Create the MCP servers configuration file with default servers
 *
 * @param mcpServersPath - Path to the MCP servers configuration file
 */
function createDefaultMcpServersFile(mcpServersPath: string): void {
  try {
    // Ensure the directory exists
    const dir = path.dirname(mcpServersPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    // Write the default MCP servers as JSONL
    const content = DEFAULT_MCP_SERVERS.map(server => JSON.stringify(server)).join('\n');
    fs.writeFileSync(mcpServersPath, content, 'utf8');
    console.log(`🔌 Created default MCP servers configuration at: ${mcpServersPath}`);
  } catch (error) {
    console.warn(`Failed to create default MCP servers configuration at '${mcpServersPath}': ${error}`);
  }
}

/**
 * List all configured MCP servers
 *
 * @returns Promise resolving to the list of MCP servers
 */
export async function listMcpServers(): Promise<ListMcpServersResponse> {
  const timestepPaths = getTimestepPaths();
  const mcpServersPath = timestepPaths.mcpServers;

  let mcpServers: McpServer[] = [];

  try {
    if (fs.existsSync(mcpServersPath)) {
      try {
        const content = fs.readFileSync(mcpServersPath, 'utf8');
        const lines = content.split('\n').filter(line => line.trim());

        mcpServers = lines.map(line => {
          try {
            return JSON.parse(line) as McpServer;
          } catch (err) {
            console.warn(`Failed to parse MCP server line: ${line}`, err);
            return null;
          }
        }).filter(Boolean) as McpServer[];

        console.log(`🔌 Loaded ${mcpServers.length} MCP servers from ${mcpServersPath}`);
      } catch (error) {
        console.warn(`Failed to read MCP servers configuration from '${mcpServersPath}': ${error}. Creating default configuration.`);
        createDefaultMcpServersFile(mcpServersPath);
        mcpServers = DEFAULT_MCP_SERVERS;
      }
    } else {
      console.warn(`MCP servers configuration file not found at: ${mcpServersPath}. Creating default configuration.`);
      createDefaultMcpServersFile(mcpServersPath);
      mcpServers = DEFAULT_MCP_SERVERS;
    }
  } catch (error) {
    console.warn(`Error loading MCP servers configuration: ${error}. Using default servers.`);
    mcpServers = DEFAULT_MCP_SERVERS;
  }

  return {
    object: 'list',
    data: mcpServers,
  };
}

/**
 * Get a specific MCP server by ID
 * @param serverId The ID of the MCP server to retrieve
 * @returns The MCP server if found, undefined otherwise
 */
export async function getMcpServer(serverId: string): Promise<McpServer | undefined> {
  const response = await listMcpServers();
  return response.data.find(server => server.id === serverId);
}
