default: build

apis:
	rm -rf build && mkdir -p build
	rm -rf src/timestep/api/openai/v1 && mkdir -p src/timestep/api/openai
	echo '{\n  "allowUnicodeIdentifiers": true,\n  "ensureUniqueParams": false,\n  "flattenSpec": false,\n  "sortParamsByRequiredFlag": false\n}' > build/openapi-yaml.json

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
		--generator-name python-fastapi \
		--input-spec /local/build/openai/openapi-yaml/openapi.yaml \
		-o /local/build/openai/python-fastapi \
		--additional-properties packageName=timestep.api.openai.v1

	mv build/openai/python-fastapi/src/timestep/api/openai/v1 src/timestep/api/openai/v1

build:
	$$SHELL ./scripts/build.sh

clean:
	$$SHELL ./scripts/clean.sh
