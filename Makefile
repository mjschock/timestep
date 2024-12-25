default: build

apis:
	rm -rf build && mkdir -p build
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
		--generator-name python-flask \
		--input-spec /local/build/openai/openapi-yaml/openapi.yaml \
		-o /local/build/openai/python-flask \
		--additional-properties packageName=api.v1

	mv build/openai/python-flask/api/v1 src/timestep/pipelines/machine_learning/api/v1

build:
	$$SHELL ./scripts/build.sh

clean:
	$$SHELL ./scripts/clean.sh

up:
	source .venv/bin/activate && \
		timestep up --clean && \
		export MLFLOW_TRACKING_PASSWORD=$(kubectl get secret --namespace mlflow mlflow-tracking -o jsonpath="{.data.admin-password }" | base64 -d) && \
		sky launch -c cluster --env HF_TOKEN --env MLFLOW_TRACKING_PASSWORD src/timestep/pipelines/machine_learning/task.yaml && \
		kubectl port-forward pod/cluster-63c1-head 8000:8000 & \
		python query.py && \
		python src/timestep/server.py
