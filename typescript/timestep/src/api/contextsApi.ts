/**
 * Contexts API
 *
 * This module provides TypeScript interfaces and functions for managing
 * conversation contexts and chat sessions.
 *
 * Functions:
 * - listContexts() - List all contexts from contexts.jsonl
 */

import { getTimestepPaths } from "../utils.ts";
import { Context } from "../domain/context.ts";
import * as fs from 'node:fs';

/**
 * Response from the list contexts endpoint
 */
export interface ListContextsResponse {
  /** Array of context objects */
  data: Context[];
}

/**
 * List all contexts from the contexts.jsonl file
 *
 * @returns Promise resolving to the list of contexts
 */
export async function listContexts(): Promise<ListContextsResponse> {
  const timestepPaths = getTimestepPaths();

  try {
    const contextsContent = fs.readFileSync(timestepPaths.contexts, 'utf8');
    const lines = contextsContent.split('\n').filter((line: string) => line.trim());

    const contexts: Context[] = [];

    for (const line of lines) {
      try {
        const contextData = JSON.parse(line);
        const context = Context.fromJSON(contextData);
        contexts.push(context);
      } catch (error) {
        console.warn('Failed to parse context line:', line, error);
      }
    }

    return {
      data: contexts,
    };
  } catch (error) {
    throw new Error(`Failed to read contexts: ${error}`);
  }
}