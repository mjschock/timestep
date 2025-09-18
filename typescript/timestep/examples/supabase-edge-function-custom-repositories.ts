/**
 * Supabase Edge Function with Custom Repositories
 *
 * This demonstrates how to replace the built-in JSONL repositories with custom
 * Supabase database repositories. This approach stores all data in your Supabase
 * database instead of JSONL files.
 *
 * This example shows the complete integration of:
 * 1. Custom Supabase repository implementations for all entities
 * 2. Dependency injection to replace built-in repositories
 * 3. Full Supabase Edge Function setup with database storage
 * 4. SQL schema for required database tables
 *
 * Place this file in your Supabase project at: supabase/functions/timestep-server/index.ts
 *
 * To set up this function:
 * 1. deno add npm:@timestep-ai/timestep
 * 2. Run the SQL schema (provided at bottom) in your Supabase SQL editor
 * 3. Copy this code to supabase/functions/timestep-server/index.ts
 * 4. Deploy with: supabase functions deploy timestep-server
 *
 * For simpler setup with built-in repositories, see: supabase-edge-function-built-in-repositories.ts
 */

import "https://deno.land/x/xhr@0.1.0/mod.ts";
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';
import {
  listAgents,
  listModels,
  listTools,
  listTraces,
  listContexts,
  listMcpServers,
  listModelProviders,
  handleAgentRequest,
  TimestepAIAgentExecutor,
  Context,
  getVersion,
  type RepositoryContainer,
  type Repository,
  type Agent,
  type ModelProvider,
  type McpServer} from 'npm:@timestep-ai/timestep@2025.9.180831';

/**
 * Supabase Agent Repository Implementation
 */
class SupabaseAgentRepository implements Repository<Agent, string> {
  constructor(private supabase: any) {}

  async list(): Promise<Agent[]> {
    const { data, error } = await this.supabase
      .from('agents')
      .select('*');

    if (error) throw new Error(`Failed to list agents: ${error.message}`);
    return data || [];
  }

  async load(id: string): Promise<Agent | null> {
    const { data, error } = await this.supabase
      .from('agents')
      .select('*')
      .eq('id', id)
      .single();

    if (error && error.code !== 'PGRST116') {
      throw new Error(`Failed to load agent: ${error.message}`);
    }
    return data || null;
  }

  async save(agent: Agent): Promise<void> {
    const { error } = await this.supabase
      .from('agents')
      .upsert([agent]);

    if (error) throw new Error(`Failed to save agent: ${error.message}`);
  }

  async delete(id: string): Promise<void> {
    const { error } = await this.supabase
      .from('agents')
      .delete()
      .eq('id', id);

    if (error) throw new Error(`Failed to delete agent: ${error.message}`);
  }

  async exists(id: string): Promise<boolean> {
    const agent = await this.load(id);
    return agent !== null;
  }

  async getOrCreate(id: string, ...createArgs: any[]): Promise<Agent> {
    const existing = await this.load(id);
    if (existing) {
      return existing;
    }

    // For demonstration - in real implementation, you'd create a proper agent
    // based on createArgs or throw an error for agents since they shouldn't be auto-created
    throw new Error('Auto-creation of agents not supported - please create agents explicitly');
  }
}

/**
 * Supabase Context Repository Implementation
 */
class SupabaseContextRepository implements Repository<Context, string> {
  constructor(private supabase: any) {}

  async list(): Promise<Context[]> {
    const { data, error } = await this.supabase
      .from('contexts')
      .select('*');

    if (error) throw new Error(`Failed to list contexts: ${error.message}`);
    return (data || []).map((item: any) => {
      const context = new Context(item.context_id, item.agent_id);
      context.taskHistories = item.task_histories || {};
      context.taskStates = item.task_states || {};
      context.tasks = item.tasks || [];
      return context;
    });
  }

  async load(id: string): Promise<Context | null> {
    const { data, error } = await this.supabase
      .from('contexts')
      .select('*')
      .eq('context_id', id)
      .single();

    if (error && error.code !== 'PGRST116') {
      throw new Error(`Failed to load context: ${error.message}`);
    }
    if (!data) return null;

    const context = new Context(data.context_id, data.agent_id);
    context.taskHistories = data.task_histories || {};
    context.taskStates = data.task_states || {};
    context.tasks = data.tasks || [];
    return context;
  }

  async save(context: Context): Promise<void> {
    const { error } = await this.supabase
      .from('contexts')
      .upsert([{
        context_id: context.contextId,
        agent_id: context.agentId,
        task_histories: context.taskHistories,
        created_at: new Date().toISOString()
      }]);

    if (error) throw new Error(`Failed to save context: ${error.message}`);
  }

  async delete(id: string): Promise<void> {
    const { error } = await this.supabase
      .from('contexts')
      .delete()
      .eq('context_id', id);

    if (error) throw new Error(`Failed to delete context: ${error.message}`);
  }

  async exists(id: string): Promise<boolean> {
    const context = await this.load(id);
    return context !== null;
  }

  async getOrCreate(contextId: string, agentId: string): Promise<Context> {
    const existing = await this.load(contextId);
    if (existing) {
      return existing;
    }

    const newContext = new Context(contextId, agentId);
    await this.save(newContext);
    return newContext;
  }
}

/**
 * Supabase Model Provider Repository Implementation
 */
class SupabaseModelProviderRepository implements Repository<ModelProvider, string> {
  constructor(private supabase: any) {}

  async list(): Promise<ModelProvider[]> {
    const { data, error } = await this.supabase
      .from('model_providers')
      .select('*');

    if (error) throw new Error(`Failed to list model providers: ${error.message}`);
    return data || [];
  }

  async load(id: string): Promise<ModelProvider | null> {
    const { data, error } = await this.supabase
      .from('model_providers')
      .select('*')
      .eq('id', id)
      .single();

    if (error && error.code !== 'PGRST116') {
      throw new Error(`Failed to load model provider: ${error.message}`);
    }
    return data || null;
  }

  async save(provider: ModelProvider): Promise<void> {
    const { error } = await this.supabase
      .from('model_providers')
      .upsert([provider]);

    if (error) throw new Error(`Failed to save model provider: ${error.message}`);
  }

  async delete(id: string): Promise<void> {
    const { error } = await this.supabase
      .from('model_providers')
      .delete()
      .eq('id', id);

    if (error) throw new Error(`Failed to delete model provider: ${error.message}`);
  }

  async exists(id: string): Promise<boolean> {
    const provider = await this.load(id);
    return provider !== null;
  }

  async getOrCreate(id: string, ...createArgs: any[]): Promise<ModelProvider> {
    const existing = await this.load(id);
    if (existing) {
      return existing;
    }

    // For demonstration - in real implementation, you'd create a proper model provider
    // based on createArgs or throw an error since they usually shouldn't be auto-created
    throw new Error('Auto-creation of model providers not supported - please create providers explicitly');
  }
}

/**
 * Supabase MCP Server Repository Implementation
 */
class SupabaseMcpServerRepository implements Repository<McpServer, string> {
  constructor(private supabase: any) {}

  async list(): Promise<McpServer[]> {
    const { data, error } = await this.supabase
      .from('mcp_servers')
      .select('*');

    if (error) throw new Error(`Failed to list MCP servers: ${error.message}`);
    return data || [];
  }

  async load(id: string): Promise<McpServer | null> {
    const { data, error } = await this.supabase
      .from('mcp_servers')
      .select('*')
      .eq('id', id)
      .single();

    if (error && error.code !== 'PGRST116') {
      throw new Error(`Failed to load MCP server: ${error.message}`);
    }
    return data || null;
  }

  async save(server: McpServer): Promise<void> {
    const { error } = await this.supabase
      .from('mcp_servers')
      .upsert([server]);

    if (error) throw new Error(`Failed to save MCP server: ${error.message}`);
  }

  async delete(id: string): Promise<void> {
    const { error } = await this.supabase
      .from('mcp_servers')
      .delete()
      .eq('id', id);

    if (error) throw new Error(`Failed to delete MCP server: ${error.message}`);
  }

  async exists(id: string): Promise<boolean> {
    const server = await this.load(id);
    return server !== null;
  }

  async getOrCreate(id: string, ...createArgs: any[]): Promise<McpServer> {
    const existing = await this.load(id);
    if (existing) {
      return existing;
    }

    throw new Error('Auto-creation of MCP servers not supported - please create servers explicitly');
  }
}


/**
 * Custom task store for Supabase environment
 */
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

/**
 * Supabase Repository Container Implementation
 */
class SupabaseRepositoryContainer implements RepositoryContainer {
  constructor(private supabase: any) {}

  get agents() { return new SupabaseAgentRepository(this.supabase); }
  get contexts() { return new SupabaseContextRepository(this.supabase); }
  get modelProviders() { return new SupabaseModelProviderRepository(this.supabase); }
  get mcpServers() { return new SupabaseMcpServerRepository(this.supabase); }
}

// Initialize Supabase client
const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
const supabaseAnonKey = Deno.env.get("SUPABASE_ANON_KEY")!;
const supabase = createClient(supabaseUrl, supabaseAnonKey);

// Create repository container
const repositories = new SupabaseRepositoryContainer(supabase);

// Initialize components
const agentExecutor = new TimestepAIAgentExecutor({
  repositories: repositories
});
const taskStore = new SupabaseTaskStore();

// Configure the port from environment or default
const port = parseInt(Deno.env.get("PORT") || "3000");

console.log("🦕 Starting Timestep Server with Custom Supabase Repositories");
console.log(`🌐 Server will run on port ${port}`);

// Start the server with custom repositories
Deno.serve({ port }, async (request: Request) => {
  const url = new URL(request.url);

  const headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Content-Type": "application/json",
    "X-Runtime": "Supabase-Edge-Function-Custom-Repositories",
    "X-Deployment-ID": Deno.env.get("DENO_DEPLOYMENT_ID") || "local"
  };

  if (request.method === "OPTIONS") {
    return new Response(null, { status: 200, headers });
  }

  try {
    // Version endpoint - returns timestep package version info
    if (url.pathname === "/version") {
      try {
        const versionInfo = await getVersion();
        return new Response(JSON.stringify({
          ...versionInfo,
          runtime: "Supabase Edge Function with Custom Repositories"
        }), { status: 200, headers });
      } catch (error) {
        return new Response(JSON.stringify({
          error: error instanceof Error ? error.message : "Failed to read version information"
        }), { status: 500, headers });
      }
    }

    // Health check endpoints
    if (url.pathname === "/health" || url.pathname === "/supabase-health") {
      return new Response(JSON.stringify({
        status: 'healthy',
        runtime: 'Supabase Edge Function with Custom Repositories',
        timestamp: new Date().toISOString(),
        denoVersion: Deno.version.deno,
        deploymentId: Deno.env.get("DENO_DEPLOYMENT_ID") || "local",
        region: Deno.env.get("DENO_REGION") || "unknown",
        path: url.pathname,
        repositories: ['agents', 'contexts', 'model_providers', 'mcp_servers']
      }), { status: 200, headers });
    }

    // API endpoints using custom repositories
    if (url.pathname === "/agents") {
      const result = await listAgents(repositories);
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/chats") {
      const result = await listContexts(repositories);
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/settings/model-providers") {
      const result = await listModelProviders(repositories);
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/settings/mcp-servers") {
      const result = await listMcpServers(repositories);
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }


    if (url.pathname === "/tools") {
      const result = await listTools(repositories);
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/traces") {
      const result = await listTraces();
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    if (url.pathname === "/models") {
      const result = await listModels(repositories);
      return new Response(JSON.stringify(result.data), { status: 200, headers });
    }

    // Handle dynamic agent routes with custom repository
    const agentMatch = url.pathname.match(/^\/agents\/([^\/]+)(?:\/.*)?$/);
    if (agentMatch) {
      // Create a mock Express-style request object that satisfies the Request interface
      const mockReq = {
        method: request.method,
        path: url.pathname,
        originalUrl: url.pathname + url.search,
        params: { agentId: agentMatch[1] },
        body: request.method !== 'GET' ? await request.json().catch(() => ({})) : {},
        headers: Object.fromEntries(Array.from(request.headers.entries())),
        // Add required Express Request methods as stubs
        get: (name: string) => request.headers.get(name),
        header: (name: string) => request.headers.get(name),
        accepts: () => false,
        acceptsCharsets: () => false,
        acceptsEncodings: () => false,
        acceptsLanguages: () => false,
        range: () => undefined,
        param: (name: string) => name === 'agentId' ? agentMatch[1] : undefined,
        is: () => false,
        protocol: 'https',
        secure: true,
        ip: '127.0.0.1',
        ips: [],
        subdomains: [],
        hostname: url.hostname,
        fresh: false,
        stale: true,
        xhr: false,
        route: undefined,
        signedCookies: {},
        url: url.pathname + url.search,
        baseUrl: '',
        app: {} as any,
        res: {} as any,
        next: (() => {}) as any,
        query: Object.fromEntries(url.searchParams),
        cookies: {},
        secret: undefined
      } as any;

      // Create a mock response object
      const mockRes = {
        status: (code: number) => ({ json: (data: any) => data }),
        json: (data: any) => data,
        send: (data: any) => data,
        end: () => {},
        setHeader: () => {},
        getHeader: () => undefined,
        removeHeader: () => {},
        locals: {},
        append: () => {},
        attachment: () => {},
        cookie: () => {},
        clearCookie: () => {},
        download: () => {},
        format: () => {},
        get: () => undefined,
        header: () => {},
        links: () => {},
        location: () => {},
        redirect: () => {},
        render: () => {},
        sendFile: () => {},
        sendStatus: () => {},
        set: () => {},
        type: () => {},
        vary: () => {}
      } as any;

      const mockNext = () => {};

      try {
        await handleAgentRequest(mockReq, mockRes, mockNext, taskStore, agentExecutor, port, repositories);
        return new Response(JSON.stringify({ success: true }), { status: 200, headers });
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

console.log("🚀 Timestep Server running with Custom Supabase Repositories");
console.log("📚 Available endpoints:");
console.log("  - GET /version - Timestep package version information");
console.log("  - GET /health - Health check with repository info");
console.log("  - GET /agents - List agents (using SupabaseAgentRepository)");
console.log("  - GET /chats - List chats (using SupabaseContextRepository)");
console.log("  - GET /settings/model-providers - List model providers (using SupabaseModelProviderRepository)");
console.log("  - GET /settings/mcp-servers - List MCP servers (using SupabaseMcpServerRepository)");
console.log("  - GET /tools - List tools (via SupabaseMcpServerRepository)");
console.log("  - GET /models - List models (via SupabaseModelProviderRepository)");
console.log("  - GET /traces - List traces (using default hardcoded data)");
console.log("  - /agents/{agentId}/* - Dynamic agent A2A endpoints");

/*
 * SQL Schema for Supabase Tables
 *
 * Run these commands in your Supabase SQL editor to create the required tables:
 */
export const supabaseSchemaSQL = `
-- Create agents table
CREATE TABLE agents (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  instructions TEXT NOT NULL,
  handoff_description TEXT,
  handoff_ids JSONB,
  tool_ids JSONB NOT NULL,
  model TEXT NOT NULL,
  model_settings JSONB NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create contexts table
CREATE TABLE contexts (
  context_id TEXT PRIMARY KEY,
  agent_id TEXT NOT NULL,
  task_histories JSONB DEFAULT '{}',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create model_providers table
CREATE TABLE model_providers (
  id TEXT PRIMARY KEY,
  provider TEXT NOT NULL,
  api_key TEXT,
  base_url TEXT NOT NULL,
  models_url TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create mcp_servers table
CREATE TABLE mcp_servers (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  command TEXT NOT NULL,
  args JSONB,
  env JSONB,
  disabled BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create api_keys table
CREATE TABLE api_keys (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  key_value TEXT NOT NULL,
  service TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX idx_agents_name ON agents(name);
CREATE INDEX idx_contexts_agent_id ON contexts(agent_id);
CREATE INDEX idx_model_providers_provider ON model_providers(provider);
CREATE INDEX idx_mcp_servers_name ON mcp_servers(name);
CREATE INDEX idx_api_keys_service ON api_keys(service);

-- Enable Row Level Security (optional)
ALTER TABLE agents ENABLE ROW LEVEL SECURITY;
ALTER TABLE contexts ENABLE ROW LEVEL SECURITY;
ALTER TABLE model_providers ENABLE ROW LEVEL SECURITY;
ALTER TABLE mcp_servers ENABLE ROW LEVEL SECURITY;
ALTER TABLE api_keys ENABLE ROW LEVEL SECURITY;

-- Create policies for authenticated users (optional)
CREATE POLICY "Users can access agents" ON agents FOR ALL TO authenticated USING (true);
CREATE POLICY "Users can access contexts" ON contexts FOR ALL TO authenticated USING (true);
CREATE POLICY "Users can access model_providers" ON model_providers FOR ALL TO authenticated USING (true);
CREATE POLICY "Users can access mcp_servers" ON mcp_servers FOR ALL TO authenticated USING (true);
CREATE POLICY "Users can access api_keys" ON api_keys FOR ALL TO authenticated USING (true);
`;

/*
 * Environment Variables Required:
 *
 * Set these in your Supabase Edge Function environment:
 * - SUPABASE_URL: Your Supabase project URL
 * - SUPABASE_ANON_KEY: Your Supabase anon key
 * - PORT: Server port (optional, defaults to 3000)
 * - DENO_DEPLOYMENT_ID: Deployment identifier (auto-set by Supabase)
 * - DENO_REGION: Deployment region (auto-set by Supabase)
 */