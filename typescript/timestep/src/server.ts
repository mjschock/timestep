#!/usr/bin/env -S deno run --allow-net --allow-read --allow-write --allow-env --allow-sys

/**
 * Express server with CLI endpoints for both Node.js and Deno
 *
 * This file runs an Express server that works in both environments.
 * It provides CLI endpoints for the React CLI and integrates with the A2A server.
 */

import express from 'express';
import {loadAppConfig} from './utils.js';
import {handleListAgents, handleAgentRequest} from './api/agentsApi.js';
import {TimestepAIAgentExecutor} from './core/agentExecutor.js';
import {Task} from '@a2a-js/sdk';
import {TaskStore} from '@a2a-js/sdk/server';
import {DefaultRepositoryContainer} from './services/backing/repositoryContainer.js';

// Get app config
const appConfig = loadAppConfig();

// Custom task store with detailed logging
class LoggingTaskStore implements TaskStore {
	private store: Map<string, Task> = new Map();

	load(taskId: string): Promise<Task | undefined> {
		console.log(`📋 TaskStore.load(${taskId})`);
		const entry = this.store.get(taskId);
		if (entry) {
			console.log(`📋 TaskStore.load(${taskId}) -> FOUND:`, {
				id: entry.id,
				contextId: entry.contextId,
				kind: entry.kind,
				status: entry.status,
			});
			// Return copies to prevent external mutation
			return Promise.resolve({...entry});
		} else {
			console.log(`📋 TaskStore.load(${taskId}) -> NOT FOUND`);
			console.log(`📋 TaskStore current keys:`, Array.from(this.store.keys()));
			return Promise.resolve(undefined);
		}
	}

	save(task: Task): Promise<void> {
		console.log(`📋 TaskStore.save(${task.id})`, {
			id: task.id,
			contextId: task.contextId,
			kind: task.kind,
			status: task.status,
		});
		// Store copies to prevent internal mutation if caller reuses objects
		this.store.set(task.id, {...task});
		console.log(`📋 TaskStore.save(${task.id}) -> SAVED`);
		console.log(
			`📋 TaskStore current keys after save:`,
			Array.from(this.store.keys()),
		);
		return Promise.resolve();
	}
}

// Create Express app for CLI endpoints and A2A server
const app = express();

// A2A server components
const repositories = new DefaultRepositoryContainer();
const agentExecutor = new TimestepAIAgentExecutor({repositories});
const taskStore = new LoggingTaskStore();

// Server components

// Parse JSON bodies for non-agent routes
app.use((req, res, next) => {
	// Skip JSON parsing for agent routes - let A2A Express app handle it
	if (req.path.startsWith('/agents/')) {
		next();
	} else {
		express.json()(req, res, next);
	}
});

// CORS middleware
app.use((_req, res, next) => {
	res.header('Access-Control-Allow-Origin', '*');
	res.header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS');
	res.header(
		'Access-Control-Allow-Headers',
		'Origin, X-Requested-With, Content-Type, Accept, Mcp-Session-Id',
	);
	next();
});

// MCP Routes
// MCP POST endpoint for specific server - delegates to API
app.post('/mcp_servers/:serverId', async (req, res) => {
	const {serverId} = req.params;

	try {
		const {handleMcpServerRequest} = await import('./api/mcpServersApi.js');
		const result = await handleMcpServerRequest(serverId, req.body);
		res.json(result);
	} catch (error) {
		console.error('Error handling MCP request:', error);
		res.status(500).json({
			jsonrpc: '2.0',
			error: {
				code: -32603,
				message:
					error instanceof Error ? error.message : 'Internal server error',
			},
			id: req.body?.id || null,
		});
	}
});

// Handle GET requests for MCP server health check
app.get('/mcp_servers/:serverId', async (req, res) => {
	const {serverId} = req.params;

	try {
		const {getMcpServer} = await import('./api/mcpServersApi.js');
		const server = await getMcpServer(serverId);

		if (!server) {
			res.status(404).json({
				error: `MCP server ${serverId} not found`,
			});
			return;
		}

		res.json({
			status: 'healthy',
			server: server.name,
			serverId: serverId,
			enabled: server.enabled,
		});
	} catch (error) {
		console.error('Error checking MCP server:', error);
		res.status(500).json({
			error: error instanceof Error ? error.message : 'Internal server error',
		});
	}
});

// Handle DELETE requests for MCP server removal
app.delete('/mcp_servers/:serverId', async (req, res) => {
	const {serverId} = req.params;

	try {
		const {deleteMcpServer} = await import('./api/mcpServersApi.js');
		await deleteMcpServer(serverId);
		res.json({success: true, message: `MCP server ${serverId} deleted`});
	} catch (error) {
		console.error('Error deleting MCP server:', error);
		res.status(500).json({
			error: error instanceof Error ? error.message : 'Internal server error',
		});
	}
});

// Version endpoint - dynamically reads from package.json
app.get('/version', async (_req, res) => {
	try {
		const {getVersion} = await import('./utils.js');
		const versionInfo = await getVersion();
		res.json(versionInfo);
	} catch (error) {
		res.status(500).json({
			error:
				error instanceof Error
					? error.message
					: 'Failed to read version information',
		});
	}
});

// Context (Chats) endpoint
app.get('/chats', async (_req, res) => {
	try {
		const {listContexts} = await import('./api/contextsApi.js');
		const result = await listContexts(repositories);
		res.json(result.data);
	} catch (error) {
		console.error('Error listing contexts:', error);
		res.status(500).json({
			error: error instanceof Error ? error.message : 'Failed to list contexts',
		});
	}
});

// Models endpoint
app.get('/models', async (_req, res) => {
	try {
		const {listModels} = await import('./api/modelsApi.js');
		const result = await listModels(repositories);
		res.json(result.data);
	} catch (error) {
		console.error('Error listing models:', error);
		res.status(500).json({
			error: error instanceof Error ? error.message : 'Failed to list models',
		});
	}
});

// Tools endpoint
app.get('/tools', async (_req, res) => {
	try {
		const {listTools} = await import('./api/toolsApi.js');
		const result = await listTools(repositories);
		res.json(result.data);
	} catch (error) {
		console.error('Error listing tools:', error);
		res.status(500).json({
			error: error instanceof Error ? error.message : 'Failed to list tools',
		});
	}
});

// Traces endpoint
app.get('/traces', async (_req, res) => {
	try {
		const {listTraces} = await import('./api/tracesApi.js');
		const result = await listTraces();
		res.json(result.data);
	} catch (error) {
		console.error('Error listing traces:', error);
		res.status(500).json({
			error: error instanceof Error ? error.message : 'Failed to list traces',
		});
	}
});

// MCP Servers endpoint
app.get('/mcp_servers', async (_req, res) => {
	try {
		const {listMcpServers} = await import('./api/mcpServersApi.js');
		const result = await listMcpServers(repositories);
		res.json(result.data);
	} catch (error) {
		console.error('Error listing MCP servers:', error);
		res.status(500).json({
			error:
				error instanceof Error ? error.message : 'Failed to list MCP servers',
		});
	}
});

// Model providers endpoint
app.get('/model_providers', async (_req, res) => {
	try {
		const {listModelProviders} = await import('./api/modelProvidersApi.js');
		const result = await listModelProviders(repositories);
		res.json(result.data);
	} catch (error) {
		console.error('Error listing model providers:', error);
		res.status(500).json({
			error:
				error instanceof Error
					? error.message
					: 'Failed to list model providers',
		});
	}
});

// Request logging middleware
app.use((req, _res, next) => {
	console.log(`Request: ${req.method} ${req.path}`);
	next();
});

// Agent routes middleware with custom repository
app.use('/agents/:agentId', async (req, res, next) => {
	await handleAgentRequest(
		req,
		res,
		next,
		taskStore,
		agentExecutor,
		appConfig.appPort,
		repositories,
	);
});

// List agents endpoint
app.get('/agents', handleListAgents);

// Start the server
app.listen(appConfig.appPort, () => {
	console.log(`🚀 Timestep server running on port ${appConfig.appPort}`);
});
