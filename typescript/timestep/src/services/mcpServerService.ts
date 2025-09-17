import { McpServer } from '../api/settings/mcpServersApi.js';
import { Repository } from './backing/repository.js';

/**
 * Service for managing MCP server operations.
 * Handles business logic for MCP server management and delegates persistence to repository.
 */
export class McpServerService {
    constructor(private repository: Repository<McpServer, string>) {}

    /**
     * List all MCP servers
     */
    async listMcpServers(): Promise<McpServer[]> {
        return await this.repository.list();
    }

    /**
     * Get a specific MCP server by ID
     */
    async getMcpServer(serverId: string): Promise<McpServer | null> {
        return await this.repository.load(serverId);
    }

    /**
     * Check if an MCP server exists
     */
    async isMcpServerAvailable(serverId: string): Promise<boolean> {
        return await this.repository.exists(serverId);
    }

    /**
     * Save an MCP server
     */
    async saveMcpServer(server: McpServer): Promise<void> {
        await this.repository.save(server);
    }

    /**
     * Delete an MCP server
     */
    async deleteMcpServer(serverId: string): Promise<void> {
        await this.repository.delete(serverId);
    }
}