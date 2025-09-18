/**
 * API Keys API
 * 
 * This module provides TypeScript interfaces and functions for managing API keys
 * in the Timestep application.
 */

// TypeScript interfaces for API Keys

/**
 * Represents an API key configuration
 */
export interface ApiKey {
  /** Unique identifier for the API key */
  id: string;
  /** The name/label for the API key */
  name: string;
  /** The provider this API key is for (e.g., 'openai', 'ollama', 'anthropic') */
  provider: string;
  /** The actual API key value (may be masked in responses) */
  key: string;
  /** Whether the API key is currently active */
  active: boolean;
  /** When the API key was created */
  created_at: number;
  /** When the API key was last used */
  last_used_at?: number;
}

/**
 * Response from the list API keys endpoint
 */
export interface ListApiKeysResponse {
  /** The object type, which is always "list" */
  object: 'list';
  /** Array of API key objects */
  data: ApiKey[];
}


/**
 * List all configured API keys
 *
 * @param repositories Optional repository container for dependency injection. Defaults to DefaultRepositoryContainer
 * @returns Promise resolving to the list of API keys
 */
export async function listApiKeys(repositories: any = {}): Promise<ListApiKeysResponse> {
  const apiKeys: ApiKey[] = [];

  try {
    const { listModelProviders } = await import('./modelProvidersApi.js');
    const response = await listModelProviders(repositories);

    for (const provider of response.data) {
      const apiKey: ApiKey = {
        id: provider.provider || 'unknown',
        name: provider.provider || 'Unknown Provider',
        provider: provider.provider || 'unknown',
        key: provider.api_key ? `${provider.api_key.substring(0, 10)}...` : 'Not configured',
        active: !!provider.api_key,
        created_at: Date.now(), // We don't have this info, use current time
        last_used_at: undefined // We don't track this
      };
      apiKeys.push(apiKey);
    }
  } catch (error) {
    console.warn('Failed to load model providers for API keys:', error);
  }

  return {
    object: 'list',
    data: apiKeys,
  };
}
