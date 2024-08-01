#!/usr/bin/env bash
set -e # exit on first error

curl -sfL https://direnv.net/install.sh | bash

eval "$(direnv dotenv bash .env)"

make

poetry config repositories.testpypi $POETRY_REPOSITORIES_TESTPYPI_URL
poetry publish --build --no-interaction --password=$(cat ./secrets/poetry_pypi_token_testpypi) --repository=testpypi --username=__token__
