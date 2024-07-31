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
echo "POETRY_VIRTUALENVS_IN_PROJECT = $POETRY_VIRTUALENVS_IN_PROJECT"
echo "POETRY_VIRTUALENVS_IN_PROJECT_TEST = $POETRY_VIRTUALENVS_IN_PROJECT_TEST"
echo "POETRY_VIRTUALENVS_PREFER_ACTIVE_PYTHON = $POETRY_VIRTUALENVS_PREFER_ACTIVE_PYTHON"

make

poetry run pytest
poetry publish --build --no-interaction --repository=testpypi -vvv

# make up
