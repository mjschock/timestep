/**
 * Generic Repository interface for data persistence operations.
 *
 * This provides a common contract for all repository implementations,
 * enabling dependency injection and different storage backends.
 *
 * @template T The entity type (e.g., Agent, Context, ModelProvider)
 * @template ID The identifier type (usually string)
 */
export interface Repository<T, ID> {
    /**
     * Load a single entity by ID
     * @param id The entity identifier
     * @returns The entity if found, null otherwise
     */
    load(id: ID): Promise<T | null>;

    /**
     * Save an entity (create or update)
     * @param entity The entity to save
     */
    save(entity: T): Promise<void>;

    /**
     * List all entities
     * @returns Array of all entities
     */
    list(): Promise<T[]>;

    /**
     * Delete an entity by ID
     * @param id The entity identifier
     */
    delete(id: ID): Promise<void>;

    /**
     * Check if an entity exists
     * @param id The entity identifier
     * @returns True if the entity exists
     */
    exists(id: ID): Promise<boolean>;

    /**
     * Get or create an entity by ID with additional context
     * @param id The entity identifier
     * @param createArgs Additional arguments for entity creation
     * @returns The existing or newly created entity
     */
    getOrCreate(id: ID, ...createArgs: any[]): Promise<T>;
}