import { ModelProvider } from '../api/settings/modelProvidersApi.js';
import { Repository } from './backing/repository.js';

/**
 * Service for managing model provider operations.
 * Handles business logic for model provider management and delegates persistence to repository.
 */
export class ModelProviderService {
    constructor(private repository: Repository<ModelProvider, string>) {}

    /**
     * List all model providers
     */
    async listModelProviders(): Promise<ModelProvider[]> {
        return await this.repository.list();
    }

    /**
     * Get a specific model provider by ID
     */
    async getModelProvider(providerId: string): Promise<ModelProvider | null> {
        return await this.repository.load(providerId);
    }

    /**
     * Check if a model provider exists
     */
    async isModelProviderAvailable(providerId: string): Promise<boolean> {
        return await this.repository.exists(providerId);
    }

    /**
     * Save a model provider
     */
    async saveModelProvider(provider: ModelProvider): Promise<void> {
        await this.repository.save(provider);
    }

    /**
     * Delete a model provider
     */
    async deleteModelProvider(providerId: string): Promise<void> {
        await this.repository.delete(providerId);
    }
}