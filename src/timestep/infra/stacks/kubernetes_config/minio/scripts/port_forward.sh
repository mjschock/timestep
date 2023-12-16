#!/usr/bin/env bash
set -e # exit on first error
set -x # echo on

echo http://127.0.0.1:9001
kubectl port-forward svc/minio 9001:9001
