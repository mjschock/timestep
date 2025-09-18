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
import { RepositoryContainer, DefaultRepositoryContainer } from "../services/backing/repositoryContainer.js";

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
 * @param repositories Optional repository container for dependency injection. Defaults to DefaultRepositoryContainer
 * @returns Promise resolving to the list of contexts
 */
export async function listContexts(repositories: RepositoryContainer = new DefaultRepositoryContainer()): Promise<ListContextsResponse> {
  const contextService = new ContextService(repositories.contexts);

  try {
    const contexts = await contextService.listContexts();
    return {
      data: contexts,
    };
  } catch (error) {
    throw new Error(`Failed to read contexts: ${error}`);
  }
}