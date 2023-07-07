default: clean
	./tilt-up.sh

clean:
	rm -rf dist
	rm -rf src/timestep/infra/imports

pre-commit:
	poetry run pre-commit run --all-files

pyreverse:
	poetry run pyreverse --all-ancestors --all-associated --module-names y --colorized --output html --output-directory dist src.timestep
