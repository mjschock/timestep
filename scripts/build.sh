#!/usr/bin/env bash
set -e # exit on first error

curl -sfL https://direnv.net/install.sh | bash

eval "$(direnv dotenv bash .env)"

# python3 -m pip install --upgrade pip
# python3 -m pip install --user pipx
# python3 -m pipx ensurepath
# pipx install poetry==1.8.3 # TODO: Put the version in the environment
# cp .env.example .env
# sudo apt-get update -y
# sudo apt-get install direnv -y
# eval "$(direnv hook bash)"
# direnv allow
echo "POETRY_REPOSITORIES_TESTPYPI_URL = $POETRY_REPOSITORIES_TESTPYPI_URL"
echo "POETRY_VIRTUALENVS_IN_PROJECT = $POETRY_VIRTUALENVS_IN_PROJECT"
echo "POETRY_VIRTUALENVS_PREFER_ACTIVE_PYTHON = $POETRY_VIRTUALENVS_PREFER_ACTIVE_PYTHON"

ls -al ./secrets

make

poetry run pytest

poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config -- http-basic.testpypi __token__ $(cat ./secrets/poetry_pypi_token_testpypi)
poetry config -- pypi-token.testpypi $(cat ./secrets/poetry_pypi_token_testpypi)
poetry publish --build --no-interaction --repository=testpypi -vvv

# make up
