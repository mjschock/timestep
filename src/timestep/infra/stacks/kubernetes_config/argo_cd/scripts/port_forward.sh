#!/usr/bin/env bash
set -e # exit on first error
set -x # echo on

echo https://localhost:8080
kubectl port-forward svc/argo-cd-server 8080:80
