SHELL := /usr/bin/env bash

default:
	npx supabase start

local: default
	docker compose -f compose.yaml build \
		--build-arg="API_URL=https://timestep.local" \
		--build-arg="DEPLOY_URL=http://0.0.0.0:3000" \
		--push
	pulumi stack select local
	pulumi config set kubernetes:context timestep.local
	mkcert -install
	mkcert -cert-file tls.crt -key-file tls.key $(shell pulumi config get primary_domain_name) *.$(shell pulumi config get primary_domain_name)
	pulumi up
	cat .etchosts | sudo $(shell which hostctl) add ephemeral --wait 0

prod: default
	docker compose -f compose.yaml build \
		--build-arg="API_URL=https://timestep.ai" \
		--push
	pulumi stack select dev
	pulumi config set kubernetes:context timestep.ai
	pulumi up
