SHELL := /usr/bin/env bash

autogenstudio:
	poetry run autogenstudio ui

hosts:
	@echo "See https://guumaster.github.io/hostctl/docs/getting-started/#linuxmacwindows-and-permissions if you have issues."
	cat cdktf.out/stacks/timestep.local.k3s_cluster/hosts | sudo $(shell which hostctl) add ephemeral --wait 0

k3s-cluster:
	@PRIMARY_DOMAIN_NAME_IP_ADDRESS=$$(dig +short $(PRIMARY_DOMAIN_NAME)); \
	k3sup install --context $$KUBECONTEXT --ip $$PRIMARY_DOMAIN_NAME_IP_ADDRESS --local-path secrets/kubeconfig --merge --skip-install --ssh-key secrets/ssh_private_key --user ubuntu

local-tls-cert:
	mkcert -install
	mkcert -cert-file secrets/local_tls_crt -key-file secrets/local_tls_key timestep.local *.timestep.local
	kubectl create secret tls ssl-timestep.local --cert=secrets/local_tls_crt --key=secrets/local_tls_key

ngrok:
	ngrok http --host-header=rewrite https://$$PRIMARY_DOMAIN_NAME

pre-commit:
	pushd src/timestep/platform/app && poetry export --without-hashes --without-urls -o requirements.txt && popd
	poetry run pre-commit run --all-files

runner:
	test -f ~/actions-runner/run.sh || ark system install actions-runner
	~/actions-runner/run.sh

sky-clear:
	kubectl delete all -l parent=skypilot

ssh:
	@PRIMARY_DOMAIN_NAME_IP_ADDRESS=$$(dig +short $(PRIMARY_DOMAIN_NAME)); \
	ssh -i secrets/ssh_private_key -o IdentitiesOnly=yes ubuntu@$$PRIMARY_DOMAIN_NAME_IP_ADDRESS

ssh-keygen:
	ssh-keygen -t ed25519 -C "timestep.ai" -f secrets/ssh_private_key -N ""
	chmod 400 secrets/ssh_private_key

test:
	poetry run pytest tests
	URL="https://$$PRIMARY_DOMAIN_NAME/api/agents/$$DEFAULT_AGENT_ID" bash tests/test_agent_protocol_v1.sh
	poetry run agbenchmark start --cutoff 1

test-load:
	poetry run locust -f tests/locustfile.py --host=https://$$PRIMARY_DOMAIN_NAME
