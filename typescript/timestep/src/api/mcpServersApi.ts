/**
 * MCP Servers API
 *
 * This module provides TypeScript interfaces and functions for managing MCP (Model Context Protocol)
 * servers in the Timestep application. It uses the MCP server service pattern for data operations.
 */

import {McpServerService} from '../services/mcpServerService.js';
import {
	RepositoryContainer,
	DefaultRepositoryContainer,
} from '../services/backing/repositoryContainer.js';

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
export async function listMcpServers(
	repositories: RepositoryContainer = new DefaultRepositoryContainer(),
): Promise<ListMcpServersResponse> {
	const mcpServerService = new McpServerService(repositories.mcpServers);

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
 * @param repositories Optional repository for dependency injection. Defaults to DefaultRepositoryContainer
 * @returns The MCP server if found, null otherwise
 */
export async function getMcpServer(
	serverId: string,
	repositories: RepositoryContainer = new DefaultRepositoryContainer(),
): Promise<McpServer | null> {
	const mcpServerService = new McpServerService(repositories.mcpServers);

	try {
		return await mcpServerService.getMcpServer(serverId);
	} catch (error) {
		throw new Error(`Failed to get MCP server: ${error}`);
	}
}

/**
 * Save an MCP server using the MCP server service
 */
export async function saveMcpServer(
	server: McpServer,
	repositories: RepositoryContainer = new DefaultRepositoryContainer(),
): Promise<void> {
	const mcpServerService = new McpServerService(repositories.mcpServers);

	try {
		return await mcpServerService.saveMcpServer(server);
	} catch (error) {
		throw new Error(`Failed to save MCP server: ${error}`);
	}
}

/**
 * Delete an MCP server using the MCP server service
 */
export async function deleteMcpServer(
	serverId: string,
	repositories: RepositoryContainer = new DefaultRepositoryContainer(),
): Promise<void> {
	const mcpServerService = new McpServerService(repositories.mcpServers);

	try {
		return await mcpServerService.deleteMcpServer(serverId);
	} catch (error) {
		throw new Error(`Failed to delete MCP server: ${error}`);
	}
}

/**
 * Handle MCP server requests - delegates to built-in server or proxies to remote server
 */
export async function handleMcpServerRequest(
	serverId: string,
	request: any,
	repositories: RepositoryContainer = new DefaultRepositoryContainer(),
): Promise<any> {
	const mcpServerService = new McpServerService(repositories.mcpServers);

	try {
		return await mcpServerService.handleMcpServerRequest(serverId, request);
	} catch (error) {
		throw new Error(`Failed to handle MCP server request: ${error}`);
	}
}

/**
 * Call a tool on a specific MCP server
 */
export async function callMcpTool(
	serverId: string,
	name: string,
	args: any = {},
	id: string = 'tools-call',
	repositories: RepositoryContainer = new DefaultRepositoryContainer(),
): Promise<any> {
	const mcpServerService = new McpServerService(repositories.mcpServers);

	try {
		return await mcpServerService.handleMcpServerRequest(serverId, {
			jsonrpc: '2.0',
			method: 'tools/call',
			params: {name, arguments: args},
			id,
		});
	} catch (error) {
		throw new Error(`Failed to call MCP tool: ${error}`);
	}
}
