/**
 * Tools API
 *
 * This module provides TypeScript interfaces and functions for managing tools
 * in the Timestep application.
 */

import { listAllMcpTools } from "../utils.js";

/**
 * Represents a tool available in the system
 */
export interface Tool {
  /** Namespaced tool identifier (e.g., "server1.tool_name") */
  id: string;
  /** The name of the tool */
  name: string;
  /** Description of what the tool does */
  description: string;
  /** The MCP server ID this tool belongs to */
  serverId: string;
  /** The name of the MCP server this tool belongs to */
  serverName: string;
  /** JSON schema for the tool's input parameters */
  inputSchema: any;
  /** Tool category (derived from server name/type) */
  category: string;
  /** Whether the tool is currently available */
  status: 'available' | 'unavailable';
}

/**
 * Response from the list tools endpoint
 */
export interface ListToolsResponse {
  /** The object type, which is always "list" */
  object: 'list';
  /** Array of tool objects */
  data: Tool[];
}

/**
 * List all available tools from all enabled MCP servers
 *
 * @returns Promise resolving to the list of tools
 */
export async function listTools(): Promise<ListToolsResponse> {
  try {
    const mcpTools = await listAllMcpTools();

    const tools: Tool[] = mcpTools.map(mcpTool => ({
      id: mcpTool.id,
      name: mcpTool.name,
      description: mcpTool.description,
      serverId: mcpTool.serverId,
      serverName: mcpTool.serverName,
      inputSchema: mcpTool.inputSchema,
      category: mcpTool.serverName, // Use server name as category
      status: 'available' as const
    }));

    return {
      object: 'list',
      data: tools,
    };
  } catch (error) {
    throw new Error(`Failed to list tools: ${error}`);
  }
}