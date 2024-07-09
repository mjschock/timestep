publish:
	poetry install
	poetry run toml-sort -ai pyproject.toml
	poetry run typer timestep/main.py utils docs --output README.md --name timestep
	poetry export -o requirements.txt --without-hashes --without-urls
	poetry run reflex export --no-zip
	poetry publish --build

up:
	docker build -t timestep:latest .
	docker run -it --rm -p 8080:8080 --name timestep timestep:latest

up-with-gpus:
	# TODO: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode
	sudo docker build -t timestep:latest .
	sudo docker run -it --rm --gpus all -p 8080:8080 --name timestep timestep:latest

serve:
	poetry run python3 -m llama_cpp.server --config_file config.json
