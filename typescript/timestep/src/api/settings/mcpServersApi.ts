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
  /** The command to start the MCP server */
  command: string;
  /** Command line arguments for the MCP server */
  args: string[];
  /** Environment variables for the MCP server */
  env?: Record<string, string>;
  /** Whether the MCP server is currently active */
  active: boolean;
  /** The port the MCP server is running on (if applicable) */
  port?: number;
  /** When the MCP server was created */
  created_at: number;
  /** When the MCP server was last started */
  last_started_at?: number;
  /** Current status of the MCP server */
  status: 'stopped' | 'starting' | 'running' | 'error';
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

import { getTimestepPaths } from "../../utils.ts";

/**
 * List all configured MCP servers
 *
 * @returns Promise resolving to the list of MCP servers
 */
export async function listMcpServers(): Promise<ListMcpServersResponse> {
  const timestepPaths = getTimestepPaths();

  try {
    const mcpServersContent = await Deno.readTextFile(timestepPaths.mcpServers);
    const lines = mcpServersContent.split('\n').filter(line => line.trim());

    const mcpServers: McpServer[] = [];

    for (const line of lines) {
      try {
        const serverConfig = JSON.parse(line);
        const mcpServer: McpServer = {
          id: serverConfig.name || 'unknown',
          name: serverConfig.name || 'Unknown Server',
          command: serverConfig.command || '',
          args: serverConfig.args || [],
          env: serverConfig.env || {},
          active: true, // Assume active if configured
          port: serverConfig.port || undefined,
          created_at: Date.now(), // We don't have this info, use current time
          last_started_at: undefined, // We don't track this
          status: 'stopped' // Default status
        };
        mcpServers.push(mcpServer);
      } catch (error) {
        console.warn('Failed to parse MCP server line:', line, error);
      }
    }

    return {
      object: 'list',
      data: mcpServers,
    };
  } catch (error) {
    throw new Error(`Failed to read MCP servers: ${error}`);
  }
}
