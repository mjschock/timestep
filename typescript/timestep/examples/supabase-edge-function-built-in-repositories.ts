/**
 * Supabase Edge Function with Built-in Repositories
 *
 * This demonstrates how to build a complete Timestep server using the built-in JSONL repositories.
 * This is the simplest approach - just import the library functions and use them directly.
 * Data will be stored in JSONL files in the default Timestep configuration directory.
 *
 * Place this file in your Supabase project at: supabase/functions/timestep-server/index.ts
 *
 * To set up this function:
 * 1. deno add npm:@timestep-ai/timestep
 * 2. Copy this code to supabase/functions/timestep-server/index.ts
 * 3. Deploy with: supabase functions deploy timestep-server
 *
 * For custom Supabase database storage, see: supabase-edge-function-custom-repositories.ts
 */

import "https://deno.land/x/xhr@0.1.0/mod.ts";
import {
  listAgents,
  listModels,
  listTools,
  listTraces,
  listContexts,
  listApiKeys,
  listMcpServers,
  listModelProviders,
  handleAgentRequest,
  TimestepAIAgentExecutor} from 'npm:@timestep-ai/timestep@latest';

// Custom task store for Supabase environment
class SupabaseTaskStore {
  private store: Map<string, any> = new Map();

  async load(taskId: string): Promise<any | undefined> {
    console.log(`📋 SupabaseTaskStore.load(${taskId})`);
    const entry = this.store.get(taskId);
    if (entry) {
      console.log(`📋 SupabaseTaskStore.load(${taskId}) -> FOUND`);
      return {...entry};
    } else {
      console.log(`📋 SupabaseTaskStore.load(${taskId}) -> NOT FOUND`);
      return undefined;
    }
  }

  async save(task: any): Promise<void> {
    console.log(`📋 SupabaseTaskStore.save(${task.id})`);
    this.store.set(task.id, {...task});
    console.log(`📋 SupabaseTaskStore.save(${task.id}) -> SAVED`);
  }
}

// Initialize components
const agentExecutor = new TimestepAIAgentExecutor();
const taskStore = new SupabaseTaskStore();

// Configure the port from environment or default
const port = parseInt(Deno.env.get("PORT") || "3000");

console.log("🦕 Starting Timestep Server in Supabase Edge Function (Built-in Repositories)");
console.log(`🌐 Server will run on port ${port}`);

// Start the server with manual request handling
Deno.serve({ port }, async (request: Request) => {
  const url = new URL(request.url);

  const headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Content-Type": "application/json",
    "X-Runtime": "Supabase-Edge-Function-Built-in-Repositories",
    "X-Deployment-ID": Deno.env.get("DENO_DEPLOYMENT_ID") || "local"
  };

  if (request.method === "OPTIONS") {
    return new Response(null, { status: 200, headers });
  }

  try {
    // Health check endpoints
    if (url.pathname === "/health" || url.pathname === "/supabase-health") {
      return new Response(JSON.stringify({
        status: 'healthy',
        runtime: 'Supabase Edge Function (Built-in Repositories)',
        timestamp: new Date().toISOString(),
        denoVersion: Deno.version.deno,
        deploymentId: Deno.env.get("DENO_DEPLOYMENT_ID") || "local",
        region: Deno.env.get("DENO_REGION") || "unknown",
        path: url.pathname
      }), { status: 200, headers });
    }

    // API endpoints using individual library functions
    if (url.pathname === "/agents") {
      const result = await listAgents();
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/models") {
      const result = await listModels();
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/tools") {
      const result = await listTools();
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/traces") {
      const result = await listTraces();
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/chats") {
      const result = await listContexts();
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/settings/api-keys") {
      const result = await listApiKeys();
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/settings/mcp-servers") {
      const result = await listMcpServers();
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/settings/model-providers") {
      const result = await listModelProviders();
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    // Handle dynamic agent routes
    const agentMatch = url.pathname.match(/^\/agents\/([^\/]+)(?:\/.*)?$/);
    if (agentMatch) {
      // Create a mock Express-style request object
      const mockReq = {
        method: request.method,
        path: url.pathname,
        originalUrl: url.pathname + url.search,
        params: { agentId: agentMatch[1] },
        body: request.method !== 'GET' ? await request.json().catch(() => ({})) : {},
        headers: Object.fromEntries(Array.from(request.headers.entries()))
      };

      try {
        const result = await handleAgentRequest(mockReq, null, null, taskStore, agentExecutor, port);
        return new Response(JSON.stringify(result), { status: 200, headers });
      } catch (error) {
        console.error('Error in agent request handler:', error);
        return new Response(JSON.stringify({
          error: error instanceof Error ? error.message : "Failed to handle agent request"
        }), { status: 500, headers });
      }
    }

    return new Response("Not found", { status: 404, headers });
  } catch (error) {
    console.error('Error in Supabase Edge Function:', error);
    return new Response(JSON.stringify({
      error: error instanceof Error ? error.message : "Internal server error"
    }), { status: 500, headers });
  }
});

console.log("🚀 Timestep Server running in Supabase Edge Function (Built-in Repositories)");
console.log("📚 Available endpoints:");
console.log("  - GET /health - Health check");
console.log("  - GET /supabase-health - Supabase-specific health check");
console.log("  - GET /agents - List agents");
console.log("  - GET /models - List models");
console.log("  - GET /tools - List tools");
console.log("  - GET /traces - List traces");
console.log("  - GET /chats - List chats");
console.log("  - GET /settings/api-keys - List API keys");
console.log("  - GET /settings/mcp-servers - List MCP servers");
console.log("  - GET /settings/model-providers - List model providers");
console.log("  - /agents/{agentId}/* - Dynamic agent A2A endpoints");