/**
 * Abstract base class for JSONL file-based repositories.
 *
 * This provides common JSONL operations while allowing domain-specific
 * serialization and ID extraction logic to be implemented by subclasses.
 *
 * @template T The entity type (e.g., Agent, Context, ModelProvider)
 * @template ID The identifier type (usually string)
 */

import {Repository} from './repository.js';
import * as fs from 'node:fs';
import * as path from 'node:path';

export abstract class JsonlRepository<T, ID> implements Repository<T, ID> {
	protected readonly filePath: string;

	constructor(filePath: string) {
		this.filePath = filePath;
	}

	/**
	 * Serialize an entity to a JSON string for JSONL storage
	 * @param entity The entity to serialize
	 * @returns JSON string representation
	 */
	protected abstract serialize(entity: T): string;

	/**
	 * Deserialize a JSON string to an entity
	 * @param line JSON string from JSONL file
	 * @returns The deserialized entity
	 */
	protected abstract deserialize(line: string): T;

	/**
	 * Extract the ID from an entity
	 * @param entity The entity
	 * @returns The entity's identifier
	 */
	protected abstract getId(entity: T): ID;

	/**
	 * Ensure the directory exists and create default file if needed
	 */
	protected async ensureFileExists(): Promise<void> {
		const dir = path.dirname(this.filePath);

		try {
			await fs.promises.mkdir(dir, {recursive: true});

			// Create empty file if it doesn't exist
			try {
				await fs.promises.access(this.filePath);
			} catch {
				await fs.promises.writeFile(this.filePath, '', 'utf8');
			}
		} catch (error) {
			// In serverless environments, file operations might fail
			// This is acceptable as we'll return empty results
			console.warn(`Unable to create file ${this.filePath}:`, error);
		}
	}

	/**
	 * Read all lines from the JSONL file
	 */
	protected async readLines(): Promise<string[]> {
		try {
			await this.ensureFileExists();
			const content = await fs.promises.readFile(this.filePath, 'utf8');
			return content.split('\n').filter(line => line.trim());
		} catch (error) {
			console.warn(`Unable to read file ${this.filePath}:`, error);
			return [];
		}
	}

	/**
	 * Write lines to the JSONL file
	 */
	protected async writeLines(lines: string[]): Promise<void> {
		try {
			await this.ensureFileExists();
			await fs.promises.writeFile(
				this.filePath,
				lines.join('\n') + '\n',
				'utf8',
			);
		} catch (error) {
			console.warn(`Unable to write file ${this.filePath}:`, error);
			throw new Error(`Failed to save to ${this.filePath}: ${error}`);
		}
	}

	async list(): Promise<T[]> {
		const lines = await this.readLines();
		const entities: T[] = [];

		for (const line of lines) {
			try {
				const entity = this.deserialize(line);
				entities.push(entity);
			} catch (error) {
				console.warn(`Failed to parse line in ${this.filePath}:`, line, error);
			}
		}

		return entities;
	}

	async load(id: ID): Promise<T | null> {
		const entities = await this.list();
		return entities.find(entity => this.getId(entity) === id) || null;
	}

	async save(entity: T): Promise<void> {
		const entities = await this.list();
		const id = this.getId(entity);
		const existingIndex = entities.findIndex(e => this.getId(e) === id);

		if (existingIndex >= 0) {
			// Update existing entity
			entities[existingIndex] = entity;
		} else {
			// Add new entity
			entities.push(entity);
		}

		const lines = entities.map(e => this.serialize(e));
		await this.writeLines(lines);
	}

	async delete(id: ID): Promise<void> {
		const entities = await this.list();
		const filtered = entities.filter(entity => this.getId(entity) !== id);

		if (filtered.length === entities.length) {
			// Entity not found, nothing to delete
			return;
		}

		const lines = filtered.map(e => this.serialize(e));
		await this.writeLines(lines);
	}

	async exists(id: ID): Promise<boolean> {
		const entity = await this.load(id);
		return entity !== null;
	}

	/**
	 * Default implementation of getOrCreate - subclasses should override for entity-specific creation logic
	 */
	async getOrCreate(id: ID, ..._createArgs: any[]): Promise<T> {
		const existing = await this.load(id);
		if (existing) {
			return existing;
		}
		throw new Error(
			'getOrCreate must be implemented by subclass with entity-specific creation logic',
		);
	}
}
