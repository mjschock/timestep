#!/usr/bin/env bash
set -e # exit on first error

echo
echo "Username: admin"
echo "Password: $(kubectl -n default get secret argocd-secret -o jsonpath="{.data.clearPassword}" | base64 -d)"
echo
