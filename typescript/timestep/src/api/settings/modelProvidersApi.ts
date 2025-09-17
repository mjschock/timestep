/**
 * Model Providers API
 *
 * This module provides functions for managing model provider configurations.
 * It handles loading providers from configuration files and provides defaults
 * when configuration is not available.
 */

import { getTimestepPaths } from "../../utils.js";
import * as fs from 'node:fs';
import * as path from 'node:path';

/**
 * Represents a model provider configuration
 */
export interface ModelProvider {
  /** The provider identifier */
  id: string;
  /** The provider name */
  provider: string;
  /** API key for the provider */
  api_key?: string;
  /** Base URL for the provider */
  base_url: string;
  /** Models endpoint URL for the provider */
  models_url: string;
}

/**
 * Response from the list model providers endpoint
 */
export interface ListModelProvidersResponse {
  /** The object type, which is always "list" */
  object: 'list';
  /** Array of model provider objects */
  data: ModelProvider[];
}

// Default model providers configuration
const DEFAULT_MODEL_PROVIDERS: ModelProvider[] = [
  {
    "id": "00000000-0000-0000-0000-000000000000",
    "provider": "ollama",
    "api_key": undefined,
    "base_url": "https://ollama.com",
    "models_url": "https://ollama.com/api/tags"
  },
  {
    "id": "11111111-1111-1111-1111-111111111111",
    "provider": "openai",
    "api_key": undefined,
    "base_url": "https://api.openai.com/v1",
    "models_url": "https://api.openai.com/v1/models"
  },
  {
    "id": "22222222-2222-2222-2222-222222222222",
    "provider": "anthropic",
    "api_key": undefined,
    "base_url": "https://api.anthropic.com/v1/",
    "models_url": "https://api.anthropic.com/v1/models"
  }
];

/**
 * Create the model providers configuration file with default providers
 *
 * @param modelProvidersPath - Path to the model providers configuration file
 */
function createDefaultModelProvidersFile(modelProvidersPath: string): void {
  try {
    // Ensure the directory exists
    const dir = path.dirname(modelProvidersPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    // Write the default model providers as JSONL
    const content = DEFAULT_MODEL_PROVIDERS.map(provider => JSON.stringify(provider)).join('\n');
    fs.writeFileSync(modelProvidersPath, content, 'utf8');
    console.log(`🤖 Created default model providers configuration at: ${modelProvidersPath}`);
  } catch (error) {
    console.warn(`Failed to create default model providers configuration at '${modelProvidersPath}': ${error}`);
  }
}

/**
 * List all available model providers
 *
 * @returns Promise resolving to the list of model providers
 */
export async function listModelProviders(): Promise<ListModelProvidersResponse> {
  const timestepPaths = getTimestepPaths();
  const modelProvidersPath = timestepPaths.modelProviders;

  let modelProviders: ModelProvider[] = [];

  try {
    if (fs.existsSync(modelProvidersPath)) {
      try {
        const content = fs.readFileSync(modelProvidersPath, 'utf8');
        const lines = content.split('\n').filter(line => line.trim());

        modelProviders = lines.map(line => {
          try {
            return JSON.parse(line) as ModelProvider;
          } catch (err) {
            console.warn(`Failed to parse model provider line: ${line}`, err);
            return null;
          }
        }).filter(Boolean) as ModelProvider[];

        console.log(`🤖 Loaded ${modelProviders.length} model providers from ${modelProvidersPath}`);
      } catch (error) {
        console.warn(`Failed to read model providers configuration from '${modelProvidersPath}': ${error}. Creating default configuration.`);
        createDefaultModelProvidersFile(modelProvidersPath);
        modelProviders = DEFAULT_MODEL_PROVIDERS;
      }
    } else {
      console.warn(`Model providers configuration file not found at: ${modelProvidersPath}. Creating default configuration.`);
      createDefaultModelProvidersFile(modelProvidersPath);
      modelProviders = DEFAULT_MODEL_PROVIDERS;
    }
  } catch (error) {
    console.warn(`Error loading model providers configuration: ${error}. Using default providers.`);
    modelProviders = DEFAULT_MODEL_PROVIDERS;
  }

  return {
    object: 'list',
    data: modelProviders,
  };
}

/**
 * Retrieve a specific model provider by ID
 *
 * @param providerId - The ID of the model provider to retrieve
 * @returns Promise resolving to the model provider details or null if not found
 */
export async function getModelProvider(providerId: string): Promise<ModelProvider | null> {
  const response = await listModelProviders();
  return response.data.find(provider => provider.id === providerId) || null;
}