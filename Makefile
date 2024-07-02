SHELL := /usr/bin/env bash

# default:
	# npx supabase start

create:
	npx supabase start
	docker build --build-arg="API_URL=https://timestep.local" --build-arg="DEPLOY_URL=http://0.0.0.0:3000" --push --tag mschock/reflex-app --tag mschock/webserver .
	pulumi stack select local
	mkcert -install
	mkcert -cert-file tls.crt -key-file tls.key $(shell pulumi config get primary_domain_name) *.$(shell pulumi config get primary_domain_name)
	pulumi up
	cat .etchosts | sudo $(shell which hostctl) add ephemeral --wait 0

destroy:


# local: default
# 	docker build --build-arg="API_URL=https://timestep.local" --build-arg="DEPLOY_URL=http://0.0.0.0:3000" --push --tag mschock/reflex-app --tag mschock/webserver .
# 	pulumi stack select local
# 	# pulumi config set kubernetes:context timestep.local
# 	mkcert -install
# 	mkcert -cert-file tls.crt -key-file tls.key $(shell pulumi config get primary_domain_name) *.$(shell pulumi config get primary_domain_name)
# 	# PULUMI_K8S_DELETE_UNREACHABLE="true" PULUMI_K8S_ENABLE_PATCH_FORCE="true" pulumi up
# 	# pulumi up --continue-on-error --disable-integrity-checking
# 	pulumi up
# 	cat .etchosts | sudo $(shell which hostctl) add ephemeral --wait 0

# local-tilt-up:
# 	KUBECONFIG=kubeconfig tilt up

# local-down:
# 	kubectl --kubeconfig kubeconfig delete all -l parent=skypilot || true
# 	KUBECONFIG=kubeconfig tilt down || true
# 	PULUMI_K8S_DELETE_UNREACHABLE="true" pulumi destroy --continue-on-error --disable-integrity-checking
# 	multipass delete timestep-ai
# 	multipass purge

# prod: default
# 	# TODO: pulumi config env init
# 	docker build --build-arg="API_URL=https://timestep.ai" --push --tag mschock/reflex-app --tag mschock/webserver .
# 	pulumi stack select dev
# 	pulumi config set kubernetes:context timestep.ai
# 	pulumi up
