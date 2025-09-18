/**
 * Model Providers API
 *
 * This module provides functions for managing model provider configurations.
 * It uses the model provider service pattern for data operations.
 */

import { ModelProviderService } from "../../services/modelProviderService.js";
import { RepositoryContainer, DefaultRepositoryContainer } from "../../services/backing/repositoryContainer.js";

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


/**
 * List all available model providers using the model provider service
 *
 * @param repositories Optional repository container for dependency injection. Defaults to DefaultRepositoryContainer
 * @returns Promise resolving to the list of model providers
 */
export async function listModelProviders(repositories: RepositoryContainer = new DefaultRepositoryContainer()): Promise<ListModelProvidersResponse> {
  const modelProviderService = new ModelProviderService(repositories.modelProviders);

  try {
    const modelProviders = await modelProviderService.listModelProviders();
    return {
      object: 'list',
      data: modelProviders,
    };
  } catch (error) {
    throw new Error(`Failed to list model providers: ${error}`);
  }
}

/**
 * Retrieve a specific model provider by ID using the model provider service
 *
 * @param providerId - The ID of the model provider to retrieve
 * @param repositories Optional repository container for dependency injection. Defaults to DefaultRepositoryContainer
 * @returns Promise resolving to the model provider details or null if not found
 */
export async function getModelProvider(providerId: string, repositories: RepositoryContainer = new DefaultRepositoryContainer()): Promise<ModelProvider | null> {
  const modelProviderService = new ModelProviderService(repositories.modelProviders);

  try {
    return await modelProviderService.getModelProvider(providerId);
  } catch (error) {
    throw new Error(`Failed to get model provider: ${error}`);
  }
}