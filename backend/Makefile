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
	uv run ruff check --fix . --ignore C901
	uv run toml-sort -ai pyproject.toml
	uv run pytest

	mkdir docs && uv run pyreverse src/backend/ \
		--colorized \
		--no-standalone \
		--only-classnames \
		--output-directory docs \
		--project backend \
		--source-roots src
