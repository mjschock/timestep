#! /usr/bin/env bash

set -e

source .venv/bin/activate

timestep up --clean

export MLFLOW_TRACKING_PASSWORD=$(kubectl get secret --namespace mlflow mlflow-tracking -o jsonpath="{.data.admin-password }" | base64 -d)

sky launch \
    --cluster cluster \
    --env HF_TOKEN \
    --env MLFLOW_TRACKING_PASSWORD \
    src/timestep/platform/ml/task.yaml

# kubectl port-forward pod/cluster-63c1-head 8000:8000 &
# python query.py
# python src/timestep/server.py
