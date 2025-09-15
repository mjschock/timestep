import { ContextRepository } from './context_repository.ts';
import { Context } from '../../domain/context.ts';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { getTimestepPaths } from '../../utils.ts';

// Get timestep configuration paths
const timestepPaths = getTimestepPaths();

/**
 * JSONL file-based implementation of ContextRepository.
 * Stores contexts as JSON objects in a .jsonl file, one context per line.
 */
export class JsonlContextRepository implements ContextRepository {
    private readonly filePath: string;

    constructor() {
        this.filePath = timestepPaths.contexts;
    }

    async getOrCreate(agentId: string, contextId: string): Promise<Context> {
        const existing = await this.load(contextId);
        if (existing) {
            return existing;
        }
        
        console.log(`🔍 Creating new context ${contextId} for agent ${agentId}`);
        return new Context(contextId, agentId);
    }

    async save(context: Context): Promise<void> {
        // Ensure directory exists
        const configDir = path.dirname(this.filePath);
        if (!fs.existsSync(configDir)) {
            fs.mkdirSync(configDir, { recursive: true });
        }

        // Load existing contexts
        let contexts: any[] = [];
        if (fs.existsSync(this.filePath)) {
            const content = await fs.promises.readFile(this.filePath, 'utf-8');
            contexts = content
                .split('\n')
                .filter(line => line.trim())
                .map(line => JSON.parse(line));
        }

        // Update or add this context
        const existingIndex = contexts.findIndex(ctx => ctx.contextId === context.contextId);
        if (existingIndex >= 0) {
            contexts[existingIndex] = context.toJSON();
        } else {
            contexts.push(context.toJSON());
        }

        // Write back
        const content = contexts.map(ctx => JSON.stringify(ctx)).join('\n') + '\n';
        await fs.promises.writeFile(this.filePath, content, 'utf-8');
        
        console.log(`💾 Saved context ${context.contextId} with ${Object.keys(context.taskHistories).length} tasks`);
    }

    async load(contextId: string): Promise<Context | null> {
        try {
            if (!fs.existsSync(this.filePath)) {
                return null;
            }

            const content = await fs.promises.readFile(this.filePath, 'utf-8');
            const contexts = content
                .split('\n')
                .filter(line => line.trim())
                .map(line => JSON.parse(line));

            const contextData = contexts.find(ctx => ctx.contextId === contextId);
            
            if (!contextData) {
                return null;
            }

            console.log(`🔍 Loaded context ${contextId} with ${Object.keys(contextData.taskHistories || {}).length} tasks`);
            return Context.fromJSON(contextData);
        } catch (error) {
            console.error(`❌ Error loading context ${contextId}:`, error);
            return null;
        }
    }

    async list(): Promise<Context[]> {
        try {
            if (!fs.existsSync(this.filePath)) {
                return [];
            }

            const content = await fs.promises.readFile(this.filePath, 'utf-8');
            const contextData = content
                .split('\n')
                .filter(line => line.trim())
                .map(line => JSON.parse(line));

            return contextData.map(data => Context.fromJSON(data));
        } catch (error) {
            console.error(`❌ Error listing contexts:`, error);
            return [];
        }
    }
}