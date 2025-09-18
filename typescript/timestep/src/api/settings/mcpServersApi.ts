/**
 * MCP Servers API
 *
 * This module provides TypeScript interfaces and functions for managing MCP (Model Context Protocol)
 * servers in the Timestep application. It uses the MCP server service pattern for data operations.
 */

import { McpServerService } from "../../services/mcpServerService.js";
import { RepositoryContainer, DefaultRepositoryContainer } from "../../services/backing/repositoryContainer.js";

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


/**
 * List all configured MCP servers using the MCP server service
 *
 * @param repositories Optional repository container for dependency injection. Defaults to DefaultRepositoryContainer
 * @returns Promise resolving to the list of MCP servers
 */
export async function listMcpServers(repositories?: RepositoryContainer): Promise<ListMcpServersResponse> {
  const repos = repositories || new DefaultRepositoryContainer();
  const mcpServerService = new McpServerService(repos.mcpServers);

  try {
    const mcpServers = await mcpServerService.listMcpServers();
    return {
      object: 'list',
      data: mcpServers,
    };
  } catch (error) {
    throw new Error(`Failed to list MCP servers: ${error}`);
  }
}

/**
 * Get a specific MCP server by ID using the MCP server service
 * @param serverId The ID of the MCP server to retrieve
 * @param repository Optional repository for dependency injection. Defaults to JsonlMcpServerRepository
 * @returns The MCP server if found, null otherwise
 */
export async function getMcpServer(serverId: string, repositories?: RepositoryContainer): Promise<McpServer | null> {
  const repos = repositories || new DefaultRepositoryContainer();
  const mcpServerService = new McpServerService(repos.mcpServers);

  try {
    return await mcpServerService.getMcpServer(serverId);
  } catch (error) {
    throw new Error(`Failed to get MCP server: ${error}`);
  }
}
