/**
 * Default Model Providers Configuration
 *
 * Centralized configuration for default model providers that can be used by
 * any repository implementation (JSONL, Supabase, etc.)
 */

import {ModelProvider} from '../api/modelProvidersApi.js';

/**
 * Generate default model providers configuration
 */
export function getDefaultModelProviders(): ModelProvider[] {
	return [
		{
			id: '00000000-0000-0000-0000-000000000000',
			provider: 'ollama',
			apiKey: undefined,
			baseUrl: 'https://ollama.com',
			modelsUrl: 'https://ollama.com/api/tags',
		},
		{
			id: '11111111-1111-1111-1111-111111111111',
			provider: 'openai',
			apiKey: undefined,
			baseUrl: 'https://api.openai.com/v1',
			modelsUrl: 'https://api.openai.com/v1/models',
		},
		{
			id: '22222222-2222-2222-2222-222222222222',
			provider: 'anthropic',
			apiKey: undefined,
			baseUrl: 'https://api.anthropic.com/v1/',
			modelsUrl: 'https://api.anthropic.com/v1/models',
		},
	];
}
