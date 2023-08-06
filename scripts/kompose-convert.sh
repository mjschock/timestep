#!/usr/bin/env bash

kompose convert --chart --file docker-compose.yml --out timestep-ai --secrets-as-files --verbose
