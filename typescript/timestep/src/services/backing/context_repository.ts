import { Context } from '../../domain/context.ts';

/**
 * Repository interface for Context persistence operations.
 */
export interface ContextRepository {
    /**
     * Get or create a context by ID
     */
    getOrCreate(agentId: string, contextId: string): Promise<Context>;
    
    /**
     * Save a context
     */
    save(context: Context): Promise<void>;
    
    /**
     * Load a context by ID, returns null if not found
     */
    load(contextId: string): Promise<Context | null>;
}