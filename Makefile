.PHONY: default

default:
	rm -rf \
		__pycache__ \
		.pytest_cache \
		build \
		data \
		docs \
		htmlcov \
		logs \
		mlruns \
		test_outputs

	rm .coverage* || true

	uv run ruff format .
	uv run ruff check --fix . --ignore C901,S110,B018,B007
	uv run toml-sort -ai pyproject.toml
	uv run pytest --cov=src/backend --cov-report=term-missing --cov-fail-under=42

	mkdir docs && uv run pyreverse src/backend/ \
		--colorized \
		--no-standalone \
		--only-classnames \
		--output-directory docs \
		--project backend \
		--source-roots src

test-agents-sdk-anthropic-skip-local:
	uv run pytest \
		tests/test_agents_sdk.py \
		--api-key=$$ANTHROPIC_API_KEY \
		--base-url=https://api.anthropic.com/v1 \
		--model-name=claude-opus-4-0 \
		--skip-local-server

test-agents-sdk-deepseek-skip-local:
	uv run pytest \
		tests/test_agents_sdk.py \
		--api-key=$$DEEPSEEK_API_KEY \
		--base-url=https://api.deepseek.com/v1 \
		--model-name=deepseek-chat \
		--skip-local-server

test-agents-sdk-openai-skip-local:
	uv run pytest \
		tests/test_agents_sdk.py \
		--api-key=$$OPENAI_API_KEY \
		--base-url=https://api.openai.com/v1 \
		--model-name=gpt-4.1-mini \
		--skip-local-server

up:
	PYTHONPATH=src uv run uvicorn src.backend.main:app --host 0.0.0.0 --port 8000

up-local:
	uv run transformers chat localhost:8000 --model-name-or-path HuggingFaceTB/SmolVLM2-256M-Video-Instruct
