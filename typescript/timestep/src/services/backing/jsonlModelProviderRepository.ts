import { Repository } from './repository.js';
import { ModelProvider } from '../../api/settings/modelProvidersApi.js';
import { JsonlRepository } from './jsonlRepository.js';
import { getTimestepPaths } from '../../utils.js';
import * as fs from 'node:fs';
import * as path from 'node:path';

// Get timestep configuration paths
const timestepPaths = getTimestepPaths();

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
 * JSONL file-based implementation of ModelProviderRepository.
 * Stores model providers as JSON objects in a .jsonl file, one provider per line.
 */
export class JsonlModelProviderRepository extends JsonlRepository<ModelProvider, string> implements Repository<ModelProvider, string> {

    constructor() {
        super(timestepPaths.modelProviders);
    }

    protected serialize(provider: ModelProvider): string {
        return JSON.stringify(provider);
    }

    protected deserialize(line: string): ModelProvider {
        return JSON.parse(line) as ModelProvider;
    }

    protected getId(provider: ModelProvider): string {
        return provider.id;
    }

    override async list(): Promise<ModelProvider[]> {
        try {
            const providers = await super.list();
            if (providers.length > 0) {
                console.log(`🤖 Loaded ${providers.length} model providers from ${this.filePath}`);
                return providers;
            }
        } catch (error) {
            console.warn(`Failed to read model providers configuration from '${this.filePath}': ${error}. Using default configuration.`);
        }

        // If no providers found or error reading, try to create default configuration
        // In restricted environments (like Supabase Edge Functions), this will fail gracefully
        try {
            await this.createDefaultModelProvidersFile();
            console.log(`🤖 Created default model providers configuration with ${DEFAULT_MODEL_PROVIDERS.length} providers`);
        } catch (error) {
            console.warn(`Unable to create default configuration file (restricted environment): ${error}`);
            console.log(`🤖 Using in-memory default model providers configuration with ${DEFAULT_MODEL_PROVIDERS.length} providers`);
        }

        return DEFAULT_MODEL_PROVIDERS;
    }

    /**
     * Create the model providers configuration file with default providers
     */
    private async createDefaultModelProvidersFile(): Promise<void> {
        try {
            // Ensure the directory exists
            const dir = path.dirname(this.filePath);
            if (!fs.existsSync(dir)) {
                fs.mkdirSync(dir, { recursive: true });
            }

            // Write the default model providers as JSONL
            const lines = DEFAULT_MODEL_PROVIDERS.map(provider => this.serialize(provider));
            await this.writeLines(lines);
            console.log(`🤖 Created default model providers configuration at: ${this.filePath}`);
        } catch (error) {
            console.warn(`Failed to create default model providers configuration at '${this.filePath}': ${error}`);
        }
    }
}