default:
	git submodule update --init --recursive

	cd 3rdparty/llama-cpp-python/vendor/llama.cpp && make -j

	docker run --rm \
		-v ${PWD}:/local \
		swaggerapi/swagger-codegen-cli-v3 \
		generate \
		--config /local/openapi-yaml.json \
		--input-spec /local/3rdparty/openai-openapi/openapi.yaml \
		--lang openapi-yaml \
		-o /local/tmp/swagger-codegen-cli-v3/openapi-yaml

	./scripts/set_yaml_indent.py tmp/swagger-codegen-cli-v3/openapi-yaml/openapi.yaml

	docker run --rm \
		-v ${PWD}:/local \
		openapitools/openapi-generator-cli \
		validate \
		--input-spec /local/tmp/swagger-codegen-cli-v3/openapi-yaml/openapi.yaml \
		--recommend

	cp tmp/swagger-codegen-cli-v3/openapi-yaml/openapi.yaml timestep/apis/openai/openapi/openai-openapi.yaml

	poetry install

scaffold:
	rm -rf tmp/openapi-generator-cli/python-flask

	docker run --rm \
		-v ${PWD}:/local \
		openapitools/openapi-generator-cli \
		generate \
		--config /local/python-flask-config.yaml \
		--generator-name python-flask \
		--input-spec /local/tmp/swagger-codegen-cli-v3/openapi-yaml/openapi.yaml \
		-o /local/tmp/openapi-generator-cli/python-flask

	mv tmp/openapi-generator-cli/python-flask/timestep/apis/openai timestep/apis/openai

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

chat:
	./3rdparty/llama-cpp-python/vendor/llama.cpp/llama-cli \
		--color \
		--conversation \
		--interactive \
		--model 3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf \
		--prompt 'You are a friendly chatbot named Reflex. Respond in markdown.'

chat-with-lora:
	./3rdparty/llama-cpp-python/vendor/llama.cpp/llama-cli \
		--color \
		--conversation \
		--interactive \
		--lora workspace/lora-TinyLLama-v0.1-5M-F16-shakespeare-LATEST.bin \
		--model 3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf \
		--prompt 'You are a friendly chatbot named Reflex. Respond in markdown.'

run:
	uvicorn timestep.run:app --reload

run-prod:
	gunicorn -k uvicorn.workers.UvicornWorker timestep.run:app

serve:
	# poetry run python3 -m llama_cpp.server --config_file config.json
	# TODO: 3rdparty/llama-cpp-python/examples/high_level_api/fastapi_server.py
	timestep_serve \
		--model 3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf \
		--model_alias TinyLLama-v0.1-5M-F16 \
		--n_ctx 16192

serve-with-embeddings:
	timestep_serve \
		--embedding true \
		--model 3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf \
		--model_alias TinyLLama-v0.1-5M-F16 \
		--n_ctx 16192

serve-with-lora:
	timestep_serve \
		--lora workspace/lora-TinyLLama-v0.1-5M-F16-shakespeare-LATEST.bin \
		--model 3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf \
		--model_alias TinyLLama-v0.1-5M-F16 \
		--n_ctx 16192

train:
	./3rdparty/llama-cpp-python/vendor/llama.cpp/llama-finetune \
		--checkpoint-in workspace/chk-lora-TinyLLama-v0.1-5M-F16-shakespeare-LATEST.gguf \
		--checkpoint-out workspace/chk-lora-TinyLLama-v0.1-5M-F16-shakespeare-ITERATION.gguf \
		--lora-out workspace/lora-TinyLLama-v0.1-5M-F16-shakespeare-ITERATION.bin \
		--model-base 3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf \
		--save-every 10 \
		--threads 6 --adam-iter 30 --batch 4 --ctx 64 \
		--train-data data/shakespeare.txt \
		--use-checkpointing
