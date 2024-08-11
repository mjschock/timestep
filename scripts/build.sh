#!/usr/bin/env bash
set -e # exit on first error

# if direnv is not installed, install it
command -v direnv >/dev/null 2>&1 || curl -sfL https://direnv.net/install.sh | bash
eval "$(direnv dotenv bash .env)"

# if in Termux, install packages
if [ -n "$TERMUX_VERSION" ]; then
  pkg upgrade
  pkg install  binutils-is-llvm build-essential cmake clang libopenblas libandroid-execinfo libzmq ninja patchelf python python-pip python-pyarrow python-scipy tur-repo
  pip3 install cython meson-python packaging pyproject_metadata ruamel.yaml.clib setuptools setuptools_rust scikit-build-core versioneer wheel
  MATHLIB=m LDFLAGS="-lpython3.11" pip3 install --no-build-isolation --no-cache-dir numpy==1.26.4
  LDFLAGS="-lpython3.11" pip3 install --no-build-isolation --no-cache-dir pandas==2.2.2
fi

# git submodule update --init --recursive

if [ -n "$POETRY_REPOSITORIES_TESTPYPI_URL" ]; then
  poetry config repositories.testpypi "$POETRY_REPOSITORIES_TESTPYPI_URL"
fi

poetry install
poetry run black timestep
poetry run isort timestep # https://pycqa.github.io/isort/docs/configuration/black_compatibility.html#integration-with-pre-commit
poetry run pytest
poetry run toml-sort -ai pyproject.toml
poetry run typer timestep.main utils docs --name timestep --output README.md --title "Timestep AI"
