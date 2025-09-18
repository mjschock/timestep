/**
 * Repository Container Pattern
 *
 * This module provides a clean dependency injection pattern for repositories.
 * Instead of passing individual repositories everywhere, we use a container
 * that holds all repositories with clear, consistent naming.
 */

import {Repository} from './repository.js';
import {Agent} from '../../api/agentsApi.js';
import {Context} from '../../types/context.js';
import {ModelProvider} from '../../api/modelProvidersApi.js';
import {McpServer} from '../../api/mcpServersApi.js';

// Import default JSONL repositories
import {JsonlAgentRepository} from './jsonlAgentRepository.js';
import {JsonlContextRepository} from './jsonlContextRepository.js';
import {JsonlModelProviderRepository} from './jsonlModelProviderRepository.js';
import {JsonlMcpServerRepository} from './jsonlMcpServerRepository.js';

/**
 * Repository Container interface - holds all repositories with clear naming
 */
export interface RepositoryContainer {
	agents: Repository<Agent, string>;
	contexts: Repository<Context, string>;
	modelProviders: Repository<ModelProvider, string>;
	mcpServers: Repository<McpServer, string>;
	// Note: apiKeys are derived from modelProviders, no separate repository needed
}

/**
 * Default Repository Container using JSONL repositories
 */
export class DefaultRepositoryContainer implements RepositoryContainer {
	private _agents?: Repository<Agent, string>;
	private _contexts?: Repository<Context, string>;
	private _modelProviders?: Repository<ModelProvider, string>;
	private _mcpServers?: Repository<McpServer, string>;
	private baseUrl?: string;

	constructor(baseUrl?: string) {
		this.baseUrl = baseUrl;
	}

	get agents(): Repository<Agent, string> {
		if (!this._agents) {
			this._agents = new JsonlAgentRepository();
		}
		return this._agents;
	}

	get contexts(): Repository<Context, string> {
		if (!this._contexts) {
			this._contexts = new JsonlContextRepository();
		}
		return this._contexts;
	}

	get modelProviders(): Repository<ModelProvider, string> {
		if (!this._modelProviders) {
			this._modelProviders = new JsonlModelProviderRepository();
		}
		return this._modelProviders;
	}

	get mcpServers(): Repository<McpServer, string> {
		if (!this._mcpServers) {
			this._mcpServers = new JsonlMcpServerRepository(this.baseUrl);
		}
		return this._mcpServers;
	}
}
