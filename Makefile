default: clean
	./tilt-up.sh

clean:
	rm -rf docs
	rm -rf dist
	rm -rf src/timestep/infra/imports

pre-commit:
	poetry run pre-commit run --all-files

pyreverse:
	mkdir docs && poetry run pyreverse --all-ancestors --all-associated --module-names y --colorized --output html --output-directory docs src.timestep
