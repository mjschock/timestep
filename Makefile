SHELL := /usr/bin/env bash

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

pre-commit:
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
	poetry run pytest
	URL=https://www.$$PRIMARY_DOMAIN_NAME/api/agents/<agent_id> bash tests/test_agent_protocol_v1.sh
	poetry run agbenchmark start --cutoff 1
