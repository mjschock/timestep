#!/usr/bin/env bash
set -e # exit on first error

# if direnv is not installed, install it
command -v direnv >/dev/null 2>&1 || curl -sfL https://direnv.net/install.sh | bash
eval "$(direnv dotenv bash .env)"

# if in Termux, install packages
if [ -n "$TERMUX_VERSION" ]; then
  ./scripts/build_termux.sh
fi

echo 'TODO: Move the `make pre-commit` commands to a pre-commit hook'
git submodule update --init --recursive
poetry config repositories.testpypi $POETRY_REPOSITORIES_TESTPYPI_URL
poetry install
poetry run black timestep
poetry run isort timestep # https://pycqa.github.io/isort/docs/configuration/black_compatibility.html#integration-with-pre-commit
poetry run pytest
poetry run toml-sort -ai pyproject.toml
poetry run typer timestep.main utils docs --name timestep --output README.md --title "Timestep AI"
