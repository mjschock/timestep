SHELL := /usr/bin/env bash

hosts:
	@echo "See https://guumaster.github.io/hostctl/docs/getting-started/#linuxmacwindows-and-permissions if you have issues."
	cat cdktf.out/stacks/timestep.local.k3s_cluster/hosts | sudo $(shell which hostctl) add ephemeral --wait 0

k3s-cluster:
	@PRIMARY_DOMAIN_NAME_IP_ADDRESS=$$(dig +short $(PRIMARY_DOMAIN_NAME)); \
	k3sup install --context $$KUBECONTEXT --ip $$PRIMARY_DOMAIN_NAME_IP_ADDRESS --local-path secrets/kubeconfig --merge --skip-install --ssh-key secrets/ssh_private_key --user ubuntu

local-tls-cert:
	mkcert -install
	mkcert -cert-file secrets/local_tls_crt -key-file secrets/local_tls_key timestep.local example1.timestep.local example2.timestep.local www.timestep.local
	kubectl create secret tls ssl-timestep.local --cert=secrets/local_tls_crt --key=secrets/local_tls_key

pre-commit:
	poetry run pre-commit run --all-files

quasar-dev-android:
	cd src/timestep/platform/client && npx quasar dev -m capacitor -T android

quasar-dev-electron:
	cd src/timestep/platform/client && npx quasar dev -m electron --devtools

quasar-dev-ios:
	cd src/timestep/platform/client && npx quasar dev -m capacitor -T ios

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
