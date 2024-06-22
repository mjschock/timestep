SHELL := /usr/bin/env bash

default:
	python -m venv .venv && \
	source .venv/bin/activate && \
	poetry install && \
	poetry run pre-commit install && \
	poetry run pytest && \
	poetry run timestep && \
	poetry run toml-sort -ai pyproject.toml && \
	poetry run ruff check --unsafe-fixes --fix && \
	poetry run pre-commit run -a
