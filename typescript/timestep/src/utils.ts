import { homedir } from 'node:os';
import { join } from 'node:path';
import * as fs from 'node:fs';

function posixify(appName: string): string {
  return appName.toLowerCase().replace(/\s+/g, '-');
}

/**
 * Returns the config folder for the application. The default behavior
 * is to return whatever is most appropriate for the operating system.
 *
 * Based on Python Click's get_app_dir function:
 * https://github.com/pallets/click/blob/2a0e3ba907927ade6951d5732b775f11b54cb766/src/click/utils.py#L449
 *
 * @param appName - the application name. This should be properly capitalized and can contain whitespace.
 * @param roaming - controls if the folder should be roaming or not on Windows. Has no effect otherwise.
 * @param forcePosix - if this is set to true then on any POSIX system the folder will be stored in the home folder with a leading dot instead of the XDG config home or darwin's application support folder.
 */
export function getAppDir(
  appName: string,
  roaming: boolean = true,
  forcePosix: boolean = false
): string {
  const platform = process.platform;

  if (platform === 'win32') {
    const key = roaming ? 'APPDATA' : 'LOCALAPPDATA';
    const folder = process.env[key] || homedir();
    return join(folder, appName);
  }

  if (forcePosix) {
    return join(homedir(), `.${posixify(appName)}`);
  }

  if (platform === 'darwin') {
    return join(homedir(), 'Library', 'Application Support', appName);
  }

  // Unix/Linux
  const xdgConfigHome = process.env['XDG_CONFIG_HOME'] || join(homedir(), '.config');
  return join(xdgConfigHome, posixify(appName));
}

/**
 * Get configuration paths for the timestep application
 */
export function getTimestepPaths() {
  const configDir = getAppDir('timestep');

  return {
    configDir,
    appConfig: join(configDir, 'app.json'),
    agentsConfig: join(configDir, 'agents.jsonl'),
    modelProviders: join(configDir, 'model_providers.jsonl'),
    mcpServers: join(configDir, 'mcpServers.jsonl'),
    contexts: join(configDir, 'contexts.jsonl'),
  };
}

/**
 * App configuration interface
 */
export interface AppConfig {
  appPort?: number;
  mcpServerPort?: number;
}

/**
 * Load app configuration from app.json with embedded defaults
 */
export function loadAppConfig(): AppConfig {
  const timestepPaths = getTimestepPaths();
  const appConfigPath = timestepPaths.appConfig;

  // Embedded defaults - no file dependency needed for library usage
  const defaults: AppConfig = {
    appPort: 8080,
    mcpServerPort: 8000
  };

  // Try to load user config and merge with defaults
  try {
    const userConfigContent = fs.readFileSync(appConfigPath, 'utf8');
    const userConfig = JSON.parse(userConfigContent);
    return { ...defaults, ...userConfig };
  } catch (error) {
    // Return defaults if user config doesn't exist
    return defaults;
  }
}

// MCP Server utilities
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

// loadMcpServersConfig function removed - now using MCP servers API instead

/**
 * Creates an MCP client and connects to a server
 */
export async function createMcpClient(serverUrl: string, authToken?: string): Promise<Client> {
    const transportUrl = new URL(serverUrl);
    const transportOptions: any = {};

    // Add authorization header if authToken is provided
    if (authToken) {
        transportOptions.requestInit = {
            headers: {
                'Authorization': `Bearer ${authToken}`,
                'Accept': 'application/json, text/event-stream',
                'Content-Type': 'application/json'
            }
        };
        // Use custom fetch that doesn't follow redirects for authenticated requests
        transportOptions.fetch = async (url: string | URL | Request, init?: RequestInit) => {
            return fetch(url, { ...init, redirect: 'manual' });
        };
    }

    const transport = new StreamableHTTPClientTransport(transportUrl, transportOptions);

    const client = new Client({
        name: "timestep-api-client",
        version: "1.0.0"
    }, {
        capabilities: {}
    });

    await client.connect(transport);
    return client;
}

/**
 * Lists all tools from all enabled MCP servers with namespaced IDs
 */
export async function listAllMcpTools(): Promise<Array<{
    id: string;
    name: string;
    description: string;
    serverId: string;
    serverName: string;
    inputSchema: any;
}>> {
    // Use the MCP servers API instead of direct file access
    const { listMcpServers } = await import('./api/settings/mcpServersApi.js');
    const mcpServersResponse = await listMcpServers();
    const allTools: Array<{
        id: string;
        name: string;
        description: string;
        serverId: string;
        serverName: string;
        inputSchema: any;
    }> = [];

    for (const server of mcpServersResponse.data) {
        if (!server.enabled) {
            console.log(`Skipping disabled MCP server: ${server.id}`);
            continue;
        }

        try {
            console.log(`🔌 Connecting to MCP server ${server.id} at ${server.serverUrl}`);

            const client = await createMcpClient(server.serverUrl, server.authToken);

            // List tools from this server
            const mcpTools = await client.listTools();
            await client.close();

            // Add tools with namespaced IDs
            for (const mcpTool of mcpTools.tools) {
                allTools.push({
                    id: `${server.id}.${mcpTool.name}`, // Namespaced tool ID
                    name: mcpTool.name,
                    description: mcpTool.description || 'No description available',
                    serverId: server.id,
                    serverName: server.name || server.id,
                    inputSchema: mcpTool.inputSchema
                });
            }

            console.log(`✅ Loaded ${mcpTools.tools.length} tools from MCP server ${server.id}`);
        } catch (error) {
            console.error(`❌ Error loading tools from MCP server ${server.id}:`, error);
        }
    }

    console.log(`✅ Total tools loaded: ${allTools.length} from ${mcpServersResponse.data.length} servers`);
    return allTools;
}