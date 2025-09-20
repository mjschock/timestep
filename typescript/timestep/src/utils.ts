import {homedir} from 'node:os';
import {join} from 'node:path';
import * as fs from 'node:fs';

/**
 * Get version information from package.json
 */
export async function getVersion(): Promise<{
	version: string;
	name: string;
	description: string;
	timestamp: string;
}> {
	try {
		// Read package.json to get the current version
		const {readFile} = await import('fs/promises');
		const {join} = await import('path');
		const {fileURLToPath} = await import('url');
		const {dirname} = await import('path');

		// Get the directory of the current module
		const __filename = fileURLToPath(import.meta.url);
		const __dirname = dirname(__filename);

		// Read package.json from the project root
		const packageJsonPath = join(__dirname, '..', 'package.json');
		const packageJsonContent = await readFile(packageJsonPath, 'utf-8');
		const packageJson = JSON.parse(packageJsonContent);

		return {
			version: packageJson.version,
			name: packageJson.name,
			description: packageJson.description,
			timestamp: new Date().toISOString(),
		};
	} catch (error) {
		// Fallback if we can't read package.json
		return {
			version: 'unknown',
			name: '@timestep-ai/timestep',
			description: 'A CLI tool built with Ink and React',
			timestamp: new Date().toISOString(),
		};
	}
}

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
	forcePosix: boolean = false,
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
	const xdgConfigHome =
		process.env['XDG_CONFIG_HOME'] || join(homedir(), '.config');
	return join(xdgConfigHome, posixify(appName));
}

/**
 * Get configuration paths for the timestep application
 */
export function getTimestepPaths() {
	const baseDir = getAppDir('timestep');
	// Optional per-user scoping for local dev
	let userDir = baseDir;
	const explicit = process.env['TIMESTEP_USER_ID'];
	if (explicit && explicit.trim() !== '') {
		userDir = join(baseDir, 'users', explicit.trim());
	}

	return {
		configDir: userDir,
		appConfig: join(userDir, 'app.json'),
		agentsConfig: join(userDir, 'agents.jsonl'),
		modelProviders: join(userDir, 'modelProviders.jsonl'),
		mcpServers: join(userDir, 'mcpServers.jsonl'),
		contexts: join(userDir, 'contexts.jsonl'),
	};
}

/**
 * Get current user ID (for RLS and per-user scoping)
 * Priority: TIMESTEP_USER_ID env > OS username
 */
export function getCurrentUserId(): string {
	const fromEnv = process.env['TIMESTEP_USER_ID'];
	if (fromEnv && fromEnv.trim() !== '') return fromEnv.trim();
	try {
		const osUser = process.env['USER'] || process.env['USERNAME'] || 'unknown';
		return osUser;
	} catch {
		return 'unknown';
	}
}

/**
 * App configuration interface
 */
export interface AppConfig {
	appPort?: number;
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
	};

	// Try to load user config and merge with defaults
	try {
		const userConfigContent = fs.readFileSync(appConfigPath, 'utf8');
		const userConfig = JSON.parse(userConfigContent);
		return {...defaults, ...userConfig};
	} catch (error) {
		// Return defaults if user config doesn't exist
		return defaults;
	}
}

// MCP Server utilities
import {Client} from '@modelcontextprotocol/sdk/client/index.js';
import {StreamableHTTPClientTransport} from '@modelcontextprotocol/sdk/client/streamableHttp.js';

// loadMcpServersConfig function removed - now using MCP servers API instead

/**
 * Creates an MCP client and connects to a server
 */
export async function createMcpClient(
	serverUrl: string,
	authToken?: string,
): Promise<Client> {
	// Decrypt auth token if it is encrypted
	if (authToken && isEncryptedSecret(authToken)) {
		try {
			authToken = await decryptSecret(authToken);
		} catch (error) {
			console.warn('Failed to decrypt MCP server auth token:', error);
		}
	}
	const transportUrl = new URL(serverUrl);
	const transportOptions: any = {};

	// Add authorization header if authToken is provided
	if (authToken) {
		transportOptions.requestInit = {
			headers: {
				Authorization: `Bearer ${authToken}`,
				Accept: 'application/json, text/event-stream',
				'Content-Type': 'application/json',
			},
		};
		// Use custom fetch that doesn't follow redirects for authenticated requests
		transportOptions.fetch = async (
			url: string | URL | Request,
			init?: RequestInit,
		) => {
			return fetch(url, {...init, redirect: 'manual'});
		};
	}

	const transport = new StreamableHTTPClientTransport(
		transportUrl,
		transportOptions,
	);

	const client = new Client(
		{
			name: 'timestep-api-client',
			version: '1.0.0',
		},
		{
			capabilities: {},
		},
	);

	await client.connect(transport);
	return client;
}

/**
 * Lists all tools from all enabled MCP servers with namespaced IDs
 */
export async function listAllMcpTools(mcpServerRepository?: any): Promise<
	Array<{
		id: string;
		name: string;
		description: string;
		serverId: string;
		serverName: string;
		inputSchema: any;
	}>
> {
	// Use the MCP servers API instead of direct file access
	const {listMcpServers, handleMcpServerRequest} = await import(
		'./api/mcpServersApi.js'
	);
	const {getBuiltinMcpServer} = await import('./config/defaultMcpServers.js');
	const mcpServersResponse = await listMcpServers(mcpServerRepository);
	const allTools: Array<{
		id: string;
		name: string;
		description: string;
		serverId: string;
		serverName: string;
		inputSchema: any;
	}> = [];

	const builtinServer = getBuiltinMcpServer();

	for (const server of mcpServersResponse.data) {
		if (!server.enabled) {
			console.log(`Skipping disabled MCP server: ${server.id}`);
			continue;
		}

		// Skip non-built-in servers without a valid URL
		const isBuiltin = server.id === builtinServer.id;
		if (!isBuiltin) {
			const url = (server as any).serverUrl as string | undefined;
			if (!url || url.trim() === '') {
				console.warn(`Skipping MCP server ${server.id} - missing serverUrl`);
				continue;
			}
		}

		try {
			let mcpTools: any;

			if (server.id === builtinServer.id) {
				// Handle built-in MCP server - call handleMcpServerRequest directly
				const response = await handleMcpServerRequest(
					server.id,
					{
						jsonrpc: '2.0',
						method: 'tools/list',
						id: 'list-tools-request',
					},
					mcpServerRepository,
				);
				mcpTools = response.result;
			} else {
				// Handle remote MCP server - connect via HTTP
				console.log(
					`🔌 Connecting to MCP server ${server.id} at ${server.serverUrl}`,
				);

				const client = await createMcpClient(
					server.serverUrl,
					server.authToken,
				);

				// List tools from this server
				mcpTools = await client.listTools();
				await client.close();
			}

			// Add tools with namespaced IDs
			for (const mcpTool of mcpTools.tools) {
				allTools.push({
					id: `${server.id}.${mcpTool.name}`, // Namespaced tool ID
					name: mcpTool.name,
					description: mcpTool.description || 'No description available',
					serverId: server.id,
					serverName: server.name || server.id,
					inputSchema: mcpTool.inputSchema,
				});
			}

			console.log(
				`✅ Loaded ${mcpTools.tools.length} tools from MCP server ${server.id}`,
			);
		} catch (error) {
			console.error(
				`❌ Error loading tools from MCP server ${server.id}:`,
				error,
			);
		}
	}

	console.log(
		`✅ Total tools loaded: ${allTools.length} from ${mcpServersResponse.data.length} servers`,
	);
	return allTools;
}

// Secret encryption utilities (Node and Deno compatible)

function getCrypto(): Crypto {
	// @ts-ignore - Deno provides globalThis.crypto
	if (typeof globalThis !== 'undefined' && (globalThis as any).crypto) {
		// @ts-ignore
		return (globalThis as any).crypto as Crypto;
	}
	throw new Error('Web Crypto API is not available in this runtime');
}

function getPassphrase(): string {
	try {
		const denoEnvGet = (globalThis as any)?.Deno?.env?.get?.bind(
			(globalThis as any)?.Deno?.env,
		);
		if (typeof denoEnvGet === 'function') {
			const v = denoEnvGet('ENCRYPTION_PASSPHRASE');
			if (v) return v;
		}
	} catch {}
	if (typeof process !== 'undefined' && process.env) {
		const v = process.env['ENCRYPTION_PASSPHRASE'];
		if (v) return v;
	}
	throw new Error('ENCRYPTION_PASSPHRASE is not set');
}

function utf8Encode(input: string): Uint8Array {
	return new TextEncoder().encode(input);
}

function utf8Decode(bytes: ArrayBuffer): string {
	return new TextDecoder().decode(bytes);
}

async function deriveKey(
	passphrase: string,
	salt: Uint8Array,
): Promise<CryptoKey> {
	const crypto = getCrypto();
	const keyMaterial = await crypto.subtle.importKey(
		'raw',
		utf8Encode(passphrase).buffer as ArrayBuffer,
		{name: 'PBKDF2'},
		false,
		['deriveKey'],
	);
	return crypto.subtle.deriveKey(
		{
			name: 'PBKDF2',
			// deno dom types can be picky about BufferSource
			salt: salt.buffer as ArrayBuffer,
			iterations: 100_000,
			hash: 'SHA-256',
		},
		keyMaterial,
		{name: 'AES-GCM', length: 256},
		false,
		['encrypt', 'decrypt'],
	);
}

function b64(bytes: ArrayBuffer | Uint8Array): string {
	const arr = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
	// Browser and Deno have btoa on strings; Node 18 has Buffer
	const maybeBuffer = (globalThis as any).Buffer as
		| {from: (data: Uint8Array, encoding?: string) => any}
		| undefined;
	if (maybeBuffer) {
		return maybeBuffer.from(arr).toString('base64');
	}
	let binary = '';
	for (let i = 0; i < arr.byteLength; i++)
		binary += String.fromCharCode(arr[i]);
	// @ts-ignore
	return btoa(binary);
}

function fromB64(data: string): Uint8Array {
	const maybeBuffer = (globalThis as any).Buffer as
		| {from: (data: string, encoding: string) => any}
		| undefined;
	if (maybeBuffer) {
		return new Uint8Array(maybeBuffer.from(data, 'base64'));
	}
	// @ts-ignore
	const binary = atob(data);
	const arr = new Uint8Array(binary.length);
	for (let i = 0; i < binary.length; i++) arr[i] = binary.charCodeAt(i);
	return arr;
}

export function isEncryptedSecret(value: string): boolean {
	return typeof value === 'string' && value.startsWith('enc.v1.');
}

export async function encryptSecret(plaintext: string): Promise<string> {
	const crypto = getCrypto();
	const passphrase = getPassphrase();
	const salt = new Uint8Array(16);
	crypto.getRandomValues(salt);
	const key = await deriveKey(passphrase, salt);
	const iv = new Uint8Array(12);
	crypto.getRandomValues(iv);
	const ct = await crypto.subtle.encrypt(
		{name: 'AES-GCM', iv: iv.buffer as ArrayBuffer},
		key,
		utf8Encode(plaintext).buffer as ArrayBuffer,
	);
	return `enc.v1.${b64(salt)}.${b64(iv)}.${b64(ct)}`;
}

export async function decryptSecret(encoded: string): Promise<string> {
	if (!isEncryptedSecret(encoded)) return encoded;
	const parts = encoded.split('.');
	if (parts.length !== 5) throw new Error('Invalid encrypted secret format');
	const [, , saltB64, ivB64, ctB64] = parts;
	const salt = fromB64(saltB64);
	const iv = fromB64(ivB64);
	const ct = fromB64(ctB64);
	const key = await deriveKey(getPassphrase(), salt);
	const pt = await getCrypto().subtle.decrypt(
		{name: 'AES-GCM', iv: iv.buffer as ArrayBuffer},
		key,
		ct.buffer as ArrayBuffer,
	);
	return utf8Decode(pt);
}

export function maskSecret(value?: string): string | undefined {
	if (!value) return undefined;
	if (!isEncryptedSecret(value)) {
		const tail = value.slice(-4);
		return `****${tail}`;
	}
	// Use ciphertext tail to avoid decryption
	const parts = value.split('.');
	const tailB64 = parts[4] || '';
	const tail = tailB64.slice(-4);
	return `****${tail}`;
}
