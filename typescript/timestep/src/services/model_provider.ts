import { Ollama } from "ollama";
import { OllamaModel } from "./backing/models.js";
import { Model, ModelProvider, OpenAIChatCompletionsModel, OpenAIResponsesModel } from "@openai/agents";
import * as fs from "node:fs";
import OpenAI from "openai";
import { getTimestepPaths } from "../utils.js";

// Load model providers configuration
const timestepPaths = getTimestepPaths();
const modelProvidersPath = timestepPaths.modelProviders;

if (!fs.existsSync(modelProvidersPath)) {
    throw new Error(`Model providers file not found. Expected at: ${modelProvidersPath}`);
}

let modelProvidersContent = '';
try {
    modelProvidersContent = fs.readFileSync(modelProvidersPath, 'utf8');
} catch (err) {
    throw new Error(`Failed to read model providers from '${modelProvidersPath}': ${(err as Error).message}`);
}

const modelProviderLines = modelProvidersContent.split('\n').filter((line: string) => line.trim());
type ProviderConfig = {
    id?: string;
    provider?: string;
    name?: string;
    api_key?: string;
    base_url?: string;
    models_url?: string;
};

const MODEL_PROVIDERS: Record<string, ProviderConfig> = {};

for (const line of modelProviderLines) {
    const provider = JSON.parse(line);
    const key = provider.name || provider.provider;
    if (!key) {
        console.warn('Skipping model provider entry without a name/provider field:', provider);
        continue;
    }
    MODEL_PROVIDERS[key] = provider;
}

export class TimestepAIModelProvider implements ModelProvider {

    private modelProviders: Record<string, ProviderConfig>;

    constructor() {
        console.log(`Loading model providers from ${modelProvidersPath}`);
        this.modelProviders = MODEL_PROVIDERS;
        console.log(`Model providers loaded: ${JSON.stringify(this.modelProviders)}`);
    }

    getModel(_modelName?: string): Promise<Model> | Model {
        const parts = _modelName?.split('/') || [];
        const modelProvider = parts.length > 1 ? parts[0] : 'openai';
        const modelId = parts.length > 1 ? parts.slice(1).join('/') : _modelName;

        console.log(`Getting model ${modelId} from ${modelProvider}`);

        if (!modelProvider) {
            throw new Error('Model provider not specified');
        }

        if (!modelId) {
            throw new Error('Model ID not specified');
        }

        if (modelProvider === 'ollama') {
            const ollamaConfig = this.modelProviders[modelProvider];
            if (!ollamaConfig) {
                throw new Error(`Model provider configuration for '${modelProvider}' not found. Available providers: ${Object.keys(this.modelProviders).join(', ')}`);
            }
            if (!ollamaConfig.base_url) {
                throw new Error(`Missing 'base_url' for provider '${modelProvider}' in configuration`);
            }
            const ollamaClient = new Ollama({
                host: ollamaConfig.base_url,
                headers: {'Authorization': `Bearer ${ollamaConfig.api_key}`}
            });

            return new OllamaModel(ollamaClient, modelId);
        } else if (modelProvider === 'openai') {
            const openaiConfig = this.modelProviders[modelProvider];
            if (!openaiConfig) {
                throw new Error(`Model provider configuration for '${modelProvider}' not found. Available providers: ${Object.keys(this.modelProviders).join(', ')}`);
            }
            if (!openaiConfig.api_key) {
                throw new Error(`Missing 'api_key' for provider '${modelProvider}' in configuration`);
            }
            const openaiClient = new OpenAI({ apiKey: openaiConfig.api_key, baseURL: openaiConfig.base_url }); // TODO: Use AsyncOpenAI?

            // Narrow via unknown to avoid duplicative OpenAI type private field conflict
            // @ts-expect-error OpenAI client types from SDK differ from agents' expected type shape
            return new OpenAIResponsesModel(openaiClient as unknown as OpenAI, modelId);
        } else {
            const config = this.modelProviders[modelProvider];
            if (!config) {
                throw new Error(`Model provider configuration for '${modelProvider}' not found. Available providers: ${Object.keys(this.modelProviders).join(', ')}`);
            }
            if (!config.api_key) {
                throw new Error(`Missing 'api_key' for provider '${modelProvider}' in configuration`);
            }
            const client = new OpenAI({ apiKey: config.api_key, baseURL: config.base_url }); // TODO: Use AsyncOpenAI?

            // Narrow via unknown to avoid duplicative OpenAI type private field conflict
            // @ts-expect-error OpenAI client types from SDK differ from agents' expected type shape
            return new OpenAIChatCompletionsModel(client as unknown as OpenAI, modelId);
        }
    }
}
