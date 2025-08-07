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
	uv run pytest -vv \
		--cov=src/backend \
		--cov-fail-under=42 \
		--cov-report=term-missing \

	mkdir docs && uv run pyreverse src/backend/ \
		--colorized \
		--no-standalone \
		--only-classnames \
		--output-directory docs \
		--project backend \
		--source-roots src

test-github-gpt-4.1-mini-proxy:
	uv run pytest -vv \
		tests/test_agents_sdk.py -m "chat_completions" \
		--api-key=$$GITHUB_TOKEN \
		--base-url=http://localhost:8000/api/github/v1 \
		--model-name=openai/gpt-4.1-mini

test-github-gpt-4.1-mini-skip-local:
	uv run pytest -vv \
		tests/test_agents_sdk.py -m "chat_completions" \
		--api-key=$$GITHUB_TOKEN \
		--base-url=https://models.github.ai/inference \
		--model-name=openai/gpt-4.1-mini \
		--skip-local-server true

up:
	PYTHONPATH=src uv run uvicorn src.backend.main:app --host 0.0.0.0 --port 8000

up-local:
	uv run transformers chat localhost:8000 --model-name-or-path HuggingFaceTB/SmolVLM2-256M-Video-Instruct
