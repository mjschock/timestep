/**
 * OpenAI Models API
 * 
 * This module provides TypeScript interfaces and functions for interacting with
 * the OpenAI Models API endpoints as defined in the OpenAPI specification.
 * 
 * Endpoints:
 * - GET /models - List all available models
 * - GET /models/{model} - Retrieve a specific model
 * - DELETE /models/{model} - Delete a fine-tuned model
 */

// TypeScript interfaces based on OpenAI OpenAPI specification

/**
 * Represents an OpenAI model offering that can be used with the API
 */
export interface Model {
  /** The model identifier, which can be referenced in the API endpoints */
  id: string;
  /** The Unix timestamp (in seconds) when the model was created */
  created: number;
  /** The object type, which is always "model" */
  object: 'model';
  /** The organization that owns the model */
  owned_by: string;
}

/**
 * Response from the list models endpoint
 */
export interface ListModelsResponse {
  /** The object type, which is always "list" */
  object: 'list';
  /** Array of model objects */
  data: Model[];
}

/**
 * Response from the delete model endpoint
 */
export interface DeleteModelResponse {
  /** The ID of the deleted model */
  id: string;
  /** Whether the model was successfully deleted */
  deleted: boolean;
  /** The object type */
  object: string;
}

import { getTimestepPaths } from "../utils.ts";

/**
 * List all available models from all configured providers
 *
 * @returns Promise resolving to the list of models
 */
export async function listModels(): Promise<ListModelsResponse> {
  const timestepPaths = getTimestepPaths();

  try {
    const modelProvidersContent = await Deno.readTextFile(timestepPaths.modelProviders);
    const lines = modelProvidersContent.split('\n').filter(line => line.trim());
    const providers = lines.map(line => {
      try {
        return JSON.parse(line);
      } catch {
        return null;
      }
    }).filter(Boolean);

    const allModels: Model[] = [];

    // Fetch models from each provider
    for (const provider of providers) {
      try {
        const headers: Record<string, string> = {
          'Content-Type': 'application/json',
        };

        if (provider.api_key) {
          headers['Authorization'] = `Bearer ${provider.api_key}`;
        }

        const response = await fetch(provider.models_url, { headers });

        if (response.ok) {
          const data = await response.json();

          let models: Model[] = [];
          if (provider.provider === 'openai') {
            models = data.data?.map((model: any) => ({
              id: `${provider.provider}/${model.id}`,
              created: model.created,
              object: model.object,
              owned_by: model.owned_by,
            })) || [];
          } else if (provider.provider === 'ollama') {
            models = data.models?.map((model: any) => ({
              id: `${provider.provider}/${model.name}`,
              created: Math.floor(new Date(model.modified_at).getTime() / 1000),
              object: 'model' as const,
              owned_by: provider.provider,
            })) || [];
          }

          allModels.push(...models);
        }
      } catch (error) {
        console.warn(`Error fetching models from ${provider.provider}:`, error);
      }
    }

    return {
      object: 'list',
      data: allModels,
    };
  } catch (error) {
    throw new Error(`Failed to read model providers: ${error}`);
  }
}

/**
 * Retrieve a specific model by ID
 * 
 * @param model - The ID of the model to retrieve
 * @returns Promise resolving to the model details
 */
export function retrieveModel(_model: string): Promise<Model> {
  // This is a stub implementation
  // In a real implementation, you would make an HTTP GET request to /models/{model}
  throw new Error('retrieveModel not implemented - this is a stub');
}

/**
 * Delete a fine-tuned model
 * 
 * @param model - The ID of the model to delete
 * @returns Promise resolving to the deletion confirmation
 */
export function deleteModel(_model: string): Promise<DeleteModelResponse> {
  // This is a stub implementation
  // In a real implementation, you would make an HTTP DELETE request to /models/{model}
  throw new Error('deleteModel not implemented - this is a stub');
}

