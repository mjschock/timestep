# Timestep AI Engine

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

Timestep AI Engine is a TypeScript/Node.js CLI tool and server application that provides an Agent-to-Agent (A2A) protocol implementation with React/Ink CLI interface. It supports both Node.js and Deno runtimes, includes built-in MCP (Model Context Protocol) servers, and provides weather tools and agent coordination capabilities.

## Working Effectively

### Repository Bootstrap and Build Process
Always perform these steps in order after cloning:

```bash
# Navigate to the main TypeScript project
cd typescript/timestep

# Install dependencies
npm install
# Takes approximately 25 seconds. NEVER CANCEL. Set timeout to 60+ seconds.

# Build the project
npm run build
# Takes approximately 4 seconds. NEVER CANCEL. Set timeout to 30+ seconds.
```

### Development and Testing Commands
```bash
# Start the server (fastest method)
node dist/cli.js server
# Takes less than 1 second. Server runs on http://localhost:8080

# Stop the server
node dist/cli.js stop

# Test CLI functionality
node dist/cli.js --help
node dist/cli.js get-version
node dist/cli.js list-agents
node dist/cli.js list-tools
node dist/cli.js list-chats
node dist/cli.js list-traces
node dist/cli.js list-mcp-servers
node dist/cli.js list-model-providers

# Alternative: Use Makefile commands (from repository root)
make timestep-cli-server          # Build and start server (takes ~7 seconds total)
make timestep-cli-list-all        # Run all list commands
make timestep-cli-get-version     # Get version info
```

### Running Tests
```bash
# Note: Tests have configuration issues but application builds and runs correctly
npm run test
# Includes prettier, xo (linting), and ava tests
# Linting will show many style violations but these don't prevent functionality

# Run only the actual tests (skip linting)
npx ava
# Note: May have ts-node configuration issues in current state
```

## Validation

### CRITICAL: Manual Validation Requirements
Always manually validate changes by running these complete scenarios:

**Basic CLI Validation:**
1. Start the server: `node dist/cli.js server`
2. Verify server responds: Check for "Timestep Agents Server started!" message
3. Test all list commands:
   - `node dist/cli.js list-agents` - Should show 8 predefined agents
   - `node dist/cli.js list-tools` - Should show 4 built-in tools (get-alerts, get-forecast, markdownToPdf, think)
   - `node dist/cli.js list-mcp-servers` - Should show 3 MCP servers (1 enabled, 2 disabled)
4. Stop the server: `node dist/cli.js stop`

**Agent Interaction Validation (Limited):**
- Note: Full agent chat functionality requires external APIs (Ollama, OpenAI, Anthropic) which may fail in restricted network environments
- Error "Missing 'base_url' for provider 'ollama'" is expected when external APIs are unavailable
- Focus validation on CLI commands and server startup/shutdown

### Known Network Dependencies and Limitations
- External model providers (Ollama, OpenAI, Anthropic) require internet access and API keys
- Weather tools require external weather API access
- In restricted environments, focus on testing local functionality (CLI commands, server management, agent listing)

## Project Structure and Navigation

### Key Directories
```
/
├── typescript/timestep/          # Main TypeScript application
│   ├── src/                      # Source code
│   │   ├── cli.tsx              # CLI entry point (React/Ink)
│   │   ├── server.ts            # Express server
│   │   ├── api/                 # API endpoints
│   │   ├── core/                # Core business logic (A2A protocol)
│   │   └── services/            # Service layer
│   ├── dist/                    # Compiled JavaScript (after npm run build)
│   ├── examples/                # Example implementations
│   └── package.json             # Dependencies and scripts
├── bash/                        # Shell scripts
│   ├── bump-version.sh          # Version management
│   └── run-a2a-inspector.sh     # A2A Inspector tool
└── Makefile                     # Build and task automation
```

### Important Files to Monitor
- `typescript/timestep/package.json` - Dependencies and version information
- `typescript/timestep/src/cli.tsx` - CLI command definitions
- `typescript/timestep/src/api/` - API endpoint implementations
- `typescript/timestep/src/core/agentExecutor.ts` - Core A2A protocol logic

## Common Tasks

### Build and Development Workflow
```bash
# Full development cycle
cd typescript/timestep
npm install && npm run build && node dist/cli.js server
# Total time: ~30 seconds

# Quick rebuild during development
npm run build && node dist/cli.js stop && node dist/cli.js server
# Time: ~5 seconds

# Check for formatting/style issues (optional - doesn't affect functionality)
npx prettier --check .
npx xo
```

### Version Management
```bash
# From repository root
./bash/bump-version.sh
# Automatically updates version using timestamp format (yyyy.m.ddhhmm)
# Includes automated build testing before version bump
```

### Deno Support
```bash
# Deno is supported but not available in all environments
# If Deno is available:
cd typescript/timestep
deno task start          # Start Deno server
deno task dev           # Development mode with auto-reload
```

## Timing Expectations and Timeouts

### NEVER CANCEL Commands - Set Appropriate Timeouts:
- `npm install` - Takes 25 seconds. Set timeout to 60+ seconds minimum.
- `npm run build` - Takes 4 seconds. Set timeout to 30+ seconds minimum.
- `make timestep-cli-server` - Takes 7 seconds total. Set timeout to 30+ seconds minimum.
- `node dist/cli.js server` - Takes less than 1 second. Set timeout to 10+ seconds minimum.

### Expected Output Validation
**Successful server start should show:**
```
✅ Timestep Agents Server started!
CLI server is available at: http://localhost:8080
Agents endpoint: http://localhost:8080/agents
Use 'timestep list-agents' to fetch agents
```

**Successful agent listing should show 8 agents:**
- Personal Assistant (ID: 00000000...)
- Administrative Assistant (ID: 11111111...)
- Communications Coordinator (ID: 22222222...)
- Content Creator (ID: 33333333...)
- Project Manager (ID: 44444444...)
- Research Assistant (ID: 55555555...)
- Scheduling Coordinator (ID: 66666666...)
- Weather Assistant (ID: 77777777...)

## Troubleshooting

### Common Issues and Solutions
- **"Module not found" errors**: Ensure you're in `typescript/timestep/` directory and have run `npm run build`
- **Server port conflicts**: Run `node dist/cli.js stop` before starting server
- **External API failures**: Expected in restricted networks; focus on local CLI functionality
- **Linting failures**: Style violations don't prevent functionality; fix if required for CI

### Pre-commit Validation Checklist
1. Build completes successfully: `npm run build`
2. Server starts and stops cleanly: `node dist/cli.js server` then `node dist/cli.js stop`
3. All list commands return data: `make timestep-cli-list-all`
4. Version info displays correctly: `node dist/cli.js get-version`

Always test both individual CLI commands and the complete server lifecycle when making changes.