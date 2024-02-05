#!/usr/bin/env bash
set -e # exit on first error

echo
echo "Token: $(kubectl -n default get secret kubeapps-operator-token -o go-template='{{.data.token | base64decode}}' | base64 -d)"
echo
