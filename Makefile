deno-server-dev:
	@echo "🦕 Starting Deno/Oak A2A Server with auto-reload..."
	cd typescript/timestep && deno task dev

deno-server:
	@echo "🦕 Starting Deno/Oak A2A Server..."
	cd typescript/timestep && deno task start

timestep-cli-server:
	@echo "🚀 Starting Timestep cli server..."
	cd typescript/timestep && npx tsx src/cli.tsx stop
	cd typescript/timestep && npx tsx src/cli.tsx server

timestep-cli-chat:
	@echo "🚀 Starting Timestep cli chat..."
	cd typescript/timestep && npx tsx src/cli.tsx chat

timestep-cli-list-agents:
	@echo "🚀 Starting Timestep cli list-agents..."
	cd typescript/timestep && npx tsx src/cli.tsx list-agents

timestep-cli-list-chats:
	@echo "🚀 Starting Timestep cli list-chats..."
	cd typescript/timestep && npx tsx src/cli.tsx list-chats

timestep-cli-list-models:
	@echo "🚀 Starting Timestep cli list-models..."
	cd typescript/timestep && npx tsx src/cli.tsx list-models

timestep-cli-list-tools:
	@echo "🚀 Starting Timestep cli list-tools..."
	cd typescript/timestep && npx tsx src/cli.tsx list-tools

timestep-cli-list-traces:
	@echo "🚀 Starting Timestep cli list-traces..."
	cd typescript/timestep && npx tsx src/cli.tsx list-traces

timestep-cli-list-settings-api-keys:
	@echo "🚀 Starting Timestep cli list-settings-api-keys..."
	cd typescript/timestep && npx tsx src/cli.tsx list-settings-api-keys

timestep-cli-list-settings-mcp-servers:
	@echo "🚀 Starting Timestep cli list-settings-mcp-servers..."
	cd typescript/timestep && npx tsx src/cli.tsx list-settings-mcp-servers

run-a2a-inspector:
	@echo "🔍 Running A2A Inspector..."
	cd bash && ./run-a2a-inspector.sh

test-built-in-weather:
	@echo "📘 Running TypeScript A2A Client tests..."
	cd typescript/timestep && npx tsx src/api/a2a_client.ts --agentId 00000000-0000-0000-0000-000000000000 --auto-approve --user-input "What's the weather in Oakland and San Francisco?"
