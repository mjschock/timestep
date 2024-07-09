publish:
	poetry install
	poetry run toml-sort -ai pyproject.toml
	poetry run typer timestep/main.py utils docs --output README.md --name timestep
	poetry export -o requirements.txt --without-hashes --without-urls
	poetry run reflex export --no-zip
	poetry publish --build
