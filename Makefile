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

skip-local:
	uv run pytest \
		tests/test_agents_sdk.py \
		--api-key=$$OPENAI_API_KEY \
		--base-url=https://api.openai.com/v1 \
		--model-name=gpt-4.1-mini \
		--skip-local-server

up:
	PYTHONPATH=src uv run uvicorn src.backend.main:app --host 0.0.0.0 --port 8000
