/**
 * Contexts API
 *
 * This module provides TypeScript interfaces and functions for managing
 * conversation contexts and chat sessions.
 *
 * Functions:
 * - listContexts() - List all contexts using the context service
 */

import { Context } from "../types/context.js";
import { ContextService } from "../services/contextService.js";
import { JsonlContextRepository } from "../services/backing/jsonlContextRepository.js";
import { Repository } from "../services/backing/repository.js";

/**
 * Response from the list contexts endpoint
 */
export interface ListContextsResponse {
  /** Array of context objects */
  data: Context[];
}

/**
 * List all contexts using the context service
 *
 * @param repository Optional repository for dependency injection. Defaults to JsonlContextRepository
 * @returns Promise resolving to the list of contexts
 */
export async function listContexts(repository?: Repository<Context, string>): Promise<ListContextsResponse> {
  const repo = repository || new JsonlContextRepository();
  const contextService = new ContextService(repo);

  try {
    const contexts = await contextService.listContexts();
    return {
      data: contexts,
    };
  } catch (error) {
    throw new Error(`Failed to read contexts: ${error}`);
  }
}