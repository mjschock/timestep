import { Ollama } from "ollama";
import { OllamaModel } from "./backing/models.js";
import { Model, ModelProvider, OpenAIChatCompletionsModel, OpenAIResponsesModel } from "@openai/agents";
import * as fs from "node:fs";
import OpenAI from "openai";
import { getTimestepPaths } from "../utils.js";

type ProviderConfig = {
    id?: string;
    provider?: string;
    name?: string;
    api_key?: string;
    base_url?: string;
    models_url?: string;
};

function loadModelProviders(): Record<string, ProviderConfig> {
    const timestepPaths = getTimestepPaths();
    const modelProvidersPath = timestepPaths.modelProviders;

    let modelProviderLines: string[] = [];

    if (fs.existsSync(modelProvidersPath)) {
        try {
            const modelProvidersContent = fs.readFileSync(modelProvidersPath, 'utf8');
            modelProviderLines = modelProvidersContent.split('\n').filter((line: string) => line.trim());
        } catch (err) {
            console.warn(`Failed to read model providers from '${modelProvidersPath}': ${(err as Error).message}. Using empty configuration.`);
            modelProviderLines = [];
        }
    } else {
        console.warn(`Model providers file not found at: ${modelProvidersPath}. Using empty configuration.`);
    }

    const MODEL_PROVIDERS: Record<string, ProviderConfig> = {};

    for (const line of modelProviderLines) {
        try {
            const provider = JSON.parse(line);
            const key = provider.name || provider.provider;
            if (!key) {
                console.warn('Skipping model provider entry without a name/provider field:', provider);
                continue;
            }
            MODEL_PROVIDERS[key] = provider;
        } catch (err) {
            console.warn(`Failed to parse model provider line: ${line}`, err);
        }
    }

    return MODEL_PROVIDERS;
}

export class TimestepAIModelProvider implements ModelProvider {

    private modelProviders: Record<string, ProviderConfig>;

    constructor() {
        console.log(`Loading model providers configuration`);
        this.modelProviders = loadModelProviders();
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

        // Check if any providers are configured
        if (Object.keys(this.modelProviders).length === 0) {
            const timestepPaths = getTimestepPaths();
            throw new Error(`No model providers configured. Please set up model providers configuration file at: ${timestepPaths.modelProviders}`);
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

            // Narrow via any to avoid duplicative OpenAI type private field conflict
            return new OpenAIResponsesModel(openaiClient as any, modelId);
        } else {
            const config = this.modelProviders[modelProvider];
            if (!config) {
                throw new Error(`Model provider configuration for '${modelProvider}' not found. Available providers: ${Object.keys(this.modelProviders).join(', ')}`);
            }
            if (!config.api_key) {
                throw new Error(`Missing 'api_key' for provider '${modelProvider}' in configuration`);
            }
            const client = new OpenAI({ apiKey: config.api_key, baseURL: config.base_url }); // TODO: Use AsyncOpenAI?

            // Narrow via any to avoid duplicative OpenAI type private field conflict
            return new OpenAIChatCompletionsModel(client as any, modelId);
        }
    }
}
