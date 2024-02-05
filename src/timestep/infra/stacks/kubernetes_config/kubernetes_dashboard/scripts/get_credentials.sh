#!/usr/bin/env bash
set -e # exit on first error

echo
kubectl get --namespace kubernetes-dashboard secret admin-user -o go-template='{{.data.token | base64decode}}'
echo
