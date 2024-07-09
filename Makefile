publish:
	poetry install
	poetry run toml-sort -ai pyproject.toml
	poetry run typer src/timestep/main.py utils docs --output README.md --name timestep
	poetry publish --build
