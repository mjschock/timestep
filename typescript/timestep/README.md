# @timestep-ai/timestep

A comprehensive TypeScript library and CLI for building AI agent systems with A2A (Agent-to-Agent) protocol support. Works seamlessly in both Node.js and Deno environments.

## Features

- 🤖 **Agent Management** - Create, configure, and manage AI agents with JSONL-based configuration
- 🔄 **A2A Protocol** - Full Agent-to-Agent protocol implementation with streaming support
- 🛠️ **Tool Integration** - MCP (Model Context Protocol) server support for external tools
- 🌐 **Multi-Runtime** - Works in Node.js, Deno, and Supabase Edge Functions
- 📊 **Model Provider Support** - Supports OpenAI, Anthropic, Ollama, and custom providers
- 🎛️ **CLI Interface** - Beautiful terminal UI for agent interaction and management
- 📚 **API Server** - RESTful API server with Express.js
- 💾 **Context Management** - Persistent conversation contexts and task tracking
- 🔍 **Tracing & Debugging** - Built-in execution tracing and logging

## Installation

### Global CLI Installation

```bash
npm install --global @timestep-ai/timestep
```

### Library Installation

```bash
# Node.js/npm
npm install @timestep-ai/timestep

# Deno
deno add npm:@timestep-ai/timestep
```

## Quick Start

### CLI Usage

```bash
# Start the server
timestep server

# List available agents
timestep list-agents

# Start an interactive chat
timestep chat

# List all available commands
timestep --help
```

### Library Usage (Node.js)

```typescript
import {
  listAgents,
  TimestepAIAgentExecutor,
  startDenoServer
} from '@timestep-ai/timestep';

// List configured agents
const agents = await listAgents();
console.log(agents.data);

// Create an agent executor for A2A protocol
const executor = new TimestepAIAgentExecutor();

// Start the API server
startDenoServer(3000);
```

### Library Usage (Deno/Supabase)

```typescript
// Simple approach - use pre-built Express app
import { denoApp } from 'npm:@timestep-ai/timestep@latest';

const port = parseInt(Deno.env.get("PORT") || "3000");
Deno.serve({ port }, denoApp);
```

```typescript
// Advanced approach - use individual functions
import {
  listAgents,
  listModels,
  handleAgentRequest
} from 'npm:@timestep-ai/timestep@latest';

Deno.serve({ port }, async (request: Request) => {
  const url = new URL(request.url);

  if (url.pathname === "/agents") {
    const result = await listAgents();
    return new Response(JSON.stringify(result.data));
  }
  // Handle other endpoints...
});
```

## API Endpoints

When running the server, the following endpoints are available:

### Core Endpoints
- `GET /agents` - List available agents
- `GET /models` - List available models
- `GET /tools` - List available tools
- `GET /traces` - List execution traces
- `GET /chats` - List chat contexts

### Settings Endpoints
- `GET /settings/api-keys` - List API keys
- `GET /settings/mcp-servers` - List MCP servers
- `GET /settings/model-providers` - List model providers

### A2A Protocol Endpoints
- `/agents/{agentId}/*` - Dynamic agent endpoints following A2A protocol

### Utility Endpoints
- `GET /health` - Health check
- `GET /test-agent` - Test endpoint

## Configuration

Timestep uses a configuration directory structure:

```
~/.config/timestep/           # Linux/macOS
%APPDATA%/timestep/           # Windows
~/Library/Application Support/timestep/  # macOS

├── app.json                  # App configuration (ports, etc.)
├── agents.jsonl             # Agent configurations
├── model_providers.jsonl    # Model provider settings
├── mcp_servers.jsonl       # MCP server configurations
└── contexts.jsonl          # Chat contexts and history
```

### Example Agent Configuration

```json
{"id":"assistant","name":"General Assistant","instructions":"You are a helpful AI assistant.","toolIds":["web_search","file_operations"],"model":"gpt-4","modelSettings":{"temperature":0.7}}
```

### Example Model Provider Configuration

```json
{"id":"openai","provider":"openai","api_key":"your-api-key","base_url":"https://api.openai.com/v1","models_url":"https://api.openai.com/v1/models"}
```

## Deno Support

Timestep has first-class Deno support with optimized imports and compatibility:

### Running in Deno

```bash
# Add dependencies
deno add npm:express npm:@a2a-js/sdk

# Run the Deno server
deno task deno-server

# Development mode with auto-reload
deno task deno-server:dev
```

### Supabase Edge Functions

Two approaches for Supabase deployment:

**Automatic (Recommended):**
```typescript
import { denoApp } from 'npm:@timestep-ai/timestep@latest';
Deno.serve({ port }, denoApp);
```

**Manual (Custom Control):**
```typescript
import { listAgents, handleAgentRequest } from 'npm:@timestep-ai/timestep@latest';
// Custom request handling...
```

See `examples/supabase-edge-function-automatic.ts` and `examples/supabase-edge-function-manual.ts` for complete examples.

## Development

### Node.js Development

```bash
# Clone the repository
git clone https://github.com/timestep-ai/timestep.git
cd timestep/typescript/timestep

# Install dependencies
npm install

# Build the project
npm run build

# Run the CLI locally
node dist/cli.js --help

# Start the server
node dist/server.js
```

### Deno Development

```bash
# Run with Deno
deno task deno-server

# Development mode
deno task deno-server:dev

# Run original server with Deno
deno task server
```

### Available Scripts

- `npm run build` - Build TypeScript to JavaScript
- `npm run dev` - Development mode with file watching
- `deno task deno-server` - Start Deno-optimized server
- `deno task deno-server:dev` - Deno server with file watching

## Architecture

### Core Components

- **Agent Executor** - Handles A2A protocol execution and tool calling
- **Context Service** - Manages conversation contexts and task history
- **Model Provider** - Abstracts different AI model APIs
- **Agent Factory** - Creates and configures agents from JSON definitions
- **MCP Integration** - Connects to external tool servers via MCP protocol

### File Structure

```
src/
├── api/                     # API endpoints and handlers
│   ├── agentsApi.ts        # Agent management endpoints
│   ├── modelsApi.ts        # Model listing endpoints
│   └── settings/           # Settings API endpoints
├── core/                   # Core business logic
│   ├── agent_executor.ts   # A2A protocol implementation
│   └── context_service.ts  # Context management
├── services/               # Service layer
│   ├── agent_factory.ts    # Agent creation and configuration
│   └── model_provider.ts   # Model provider abstraction
├── types/                  # TypeScript type definitions
├── utils.ts               # Utility functions
├── server.ts              # Node.js/Express server
├── denoServer.ts          # Deno-optimized server
├── app.tsx                # CLI React interface
└── cli.ts                 # CLI entry point
```

## Examples

The `examples/` directory contains:

- `supabase-edge-function-automatic.ts` - Simple Supabase deployment using pre-built Express app
- `supabase-edge-function-manual.ts` - Advanced Supabase deployment with custom request handling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT © [Timestep AI](https://github.com/timestep-ai)
