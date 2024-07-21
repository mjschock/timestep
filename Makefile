default:
	git submodule update --recursive
	poetry install

apis:
	rm -rf build && mkdir -p build
	rm -rf timestep/api/ap/v1 && mkdir -p timestep/api/ap
	rm -rf timestep/api/openai/v1 && mkdir -p timestep/api/openai

	docker run --rm \
		-v ${PWD}:/local \
		swaggerapi/swagger-codegen-cli-v3 \
		generate \
		--config /local/openapi-yaml.json \
		--input-spec https://raw.githubusercontent.com/AI-Engineer-Foundation/agent-protocol/main/schemas/openapi.yml \
		--lang openapi-yaml \
		-o /local/build/ap/openapi-yaml

	docker run --rm \
		-v ${PWD}:/local \
		openapitools/openapi-generator-cli \
		generate \
		--generator-name python-flask \
		--input-spec /local/build/ap/openapi-yaml/openapi.yaml \
		-o /local/build/ap/python-flask \
		--additional-properties packageName=timestep.api.ap.v1

	mv build/ap/python-flask/timestep/api/ap/v1 timestep/api/ap/v1

	docker run --rm \
		-v ${PWD}:/local \
		swaggerapi/swagger-codegen-cli-v3 \
		generate \
		--config /local/openapi-yaml.json \
		--input-spec https://raw.githubusercontent.com/openai/openai-openapi/master/openapi.yaml \
		--lang openapi-yaml \
		-o /local/build/openai/openapi-yaml

	docker run --rm \
		-v ${PWD}:/local \
		openapitools/openapi-generator-cli \
		generate \
		--generator-name python-flask \
		--input-spec /local/build/openai/openapi-yaml/openapi.yaml \
		-o /local/build/openai/python-flask \
		--additional-properties packageName=timestep.api.openai.v1

	mv build/openai/python-flask/timestep/api/openai/v1 timestep/api/openai/v1

dev:
	# ./3rdparty/llama.cpp/llama-server --hf-repo mjschock/TinySolar-248m-4k-code-instruct-Q4_K_M-GGUF --hf-file tinysolar-248m-4k-code-instruct-q4_k_m.gguf -c 2048 --port 8000

	# ./models/llava-v1.5-7b-q4.llamafile --nobrowser --port 8000

	# poetry run python3 -m llama_cpp.server --config_file config.json

	poetry run uvicorn timestep.__main__:app \
		--host 127.0.0.1 \
		--log-level debug \
		--loop asyncio \
		--port 8000 \
		--reload \
		--reload-dir timestep \
		--workers 1

publish:
	poetry install
	poetry run toml-sort -ai pyproject.toml
	poetry run typer timestep.main utils docs --output README.md --name timestep
	poetry publish --build
