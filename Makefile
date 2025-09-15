deno-server-dev:
	@echo "🦕 Starting Deno/Oak A2A Server with auto-reload..."
	cd typescript/timestep && deno task dev

deno-server:
	@echo "🦕 Starting Deno/Oak A2A Server..."
	cd typescript/timestep && deno task start

run-a2a-insppector:
	@echo "🔍 Running A2A Inspector..."
	cd bash && ./run-a2a-inspector.sh

test-built-in-weather:
	@echo "📘 Running TypeScript A2A Client tests..."
	cd typescript/timestep && npx tsx source/api/a2a_client.ts --agentId 00000000-0000-0000-0000-000000000000 --auto-approve --user-input "What's the weather in Oakland and San Francisco?"
