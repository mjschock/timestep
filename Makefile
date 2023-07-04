default:
	./tilt-up.sh

clean:
	rm -rf dist
	rm -rf src/timestep/infra/imports

imports:
	poetry run cdktf get --force --language python --log-level $CDKTF_LOG_LEVEL --output src/timestep/infra/imports

pretty:
	poetry run toml-sort -ai pyproject.toml
	poetry run pre-commit run --all-files
	poetry run pyreverse --all-ancestors --all-associated --module-names y --colorized --output html --output-directory dist/docs src.timestep
