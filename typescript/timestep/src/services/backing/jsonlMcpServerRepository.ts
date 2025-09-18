import { Repository } from './repository.js';
import { McpServer } from '../../api/settings/mcpServersApi.js';
import { JsonlRepository } from './jsonlRepository.js';
import { getTimestepPaths } from '../../utils.js';
import * as fs from 'node:fs';
import * as path from 'node:path';

// Get timestep configuration paths
const timestepPaths = getTimestepPaths();

// Default MCP servers configuration
const DEFAULT_MCP_SERVERS: McpServer[] = [
  {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "Built-in MCP Server",
    "description": "Built-in MCP server providing weather data, document tools, and thinking capabilities",
    "serverUrl": "http://localhost:8080/mcp_servers/00000000-0000-0000-0000-000000000000",
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
 * JSONL file-based implementation of McpServerRepository.
 * Stores MCP servers as JSON objects in a .jsonl file, one server per line.
 */
export class JsonlMcpServerRepository extends JsonlRepository<McpServer, string> implements Repository<McpServer, string> {

    constructor() {
        super(timestepPaths.mcpServers);
    }

    protected serialize(server: McpServer): string {
        return JSON.stringify(server);
    }

    protected deserialize(line: string): McpServer {
        return JSON.parse(line) as McpServer;
    }

    protected getId(server: McpServer): string {
        return server.id;
    }

    override async list(): Promise<McpServer[]> {
        try {
            const servers = await super.list();
            if (servers.length > 0) {
                console.log(`🔌 Loaded ${servers.length} MCP servers from ${this.filePath}`);
                return servers;
            }
        } catch (error) {
            console.warn(`Failed to read MCP servers configuration from '${this.filePath}': ${error}. Using default configuration.`);
        }

        // If no servers found or error reading, try to create default configuration
        // In restricted environments (like Supabase Edge Functions), this will fail gracefully
        try {
            await this.createDefaultMcpServersFile();
            console.log(`🔌 Created default MCP servers configuration with ${DEFAULT_MCP_SERVERS.length} servers`);
        } catch (error) {
            console.warn(`Unable to create default configuration file (restricted environment): ${error}`);
            console.log(`🔌 Using in-memory default MCP servers configuration with ${DEFAULT_MCP_SERVERS.length} servers`);
        }

        return DEFAULT_MCP_SERVERS;
    }

    /**
     * Create the MCP servers configuration file with default servers
     */
    private async createDefaultMcpServersFile(): Promise<void> {
        try {
            // Ensure the directory exists
            const dir = path.dirname(this.filePath);
            if (!fs.existsSync(dir)) {
                fs.mkdirSync(dir, { recursive: true });
            }

            // Write the default MCP servers as JSONL
            const lines = DEFAULT_MCP_SERVERS.map(server => this.serialize(server));
            await this.writeLines(lines);
            console.log(`🔌 Created default MCP servers configuration at: ${this.filePath}`);
        } catch (error) {
            console.warn(`Failed to create default MCP servers configuration at '${this.filePath}': ${error}`);
        }
    }
}