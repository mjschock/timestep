default:
	git submodule update --init --recursive
	poetry install

apis:
	rm -rf build && mkdir -p build
	rm -rf timestep/api/ap/v1 && mkdir -p timestep/api/ap
	rm -rf timestep/api/openai/v1 && mkdir -p timestep/api/openai
	echo '{\n  "allowUnicodeIdentifiers": true,\n  "ensureUniqueParams": false,\n  "flattenSpec": false,\n  "sortParamsByRequiredFlag": false\n}' > build/openapi-yaml.json

	docker run --rm \
		-v ${PWD}:/local \
		swaggerapi/swagger-codegen-cli-v3 \
		generate \
		--config /local/build/openapi-yaml.json \
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
		--config /local/build/openapi-yaml.json \
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

clean:
	rm -rf .venv 3rdparty build data dist models work database.db

publish:
	poetry install
	poetry run toml-sort -ai pyproject.toml
	poetry run typer timestep.main utils docs --name timestep --output README.md --title "Timestep AI"
	poetry publish --build
