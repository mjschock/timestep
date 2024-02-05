#!/usr/bin/env bash
set -e # exit on first error
set -x # echo on

echo https://localhost:8484
kubectl port-forward -n kubeapps svc/kubeapps 8484:80
