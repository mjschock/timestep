#!/usr/bin/env bash
set -e # exit on first error

# if direnv is not installed, install it
command -v direnv >/dev/null 2>&1 || curl -sfL https://direnv.net/install.sh | bash
eval "$(direnv dotenv bash .env)"

if [ -n "$POETRY_REPOSITORIES_TESTPYPI_URL" ]; then
  poetry config repositories.testpypi "$POETRY_REPOSITORIES_TESTPYPI_URL"
fi

poetry install
poetry run black src/timestep
poetry run isort src/timestep
poetry run pytest tests
poetry run toml-sort -ai pyproject.toml
poetry run typer timestep.main utils docs --name timestep --output README.md --title "Timestep"
