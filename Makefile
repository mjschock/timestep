default:
	curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
	tilt up

clean:
	rm -rf cdktf.out

docker-compoze-viz:
	docker run --rm -it --name dcv -v $(shell pwd):/input pmsipilot/docker-compose-viz render -m image docker-compose.yml

hosts:
	cat cdktf.out/stacks/timestep.local.k3s_cluster/hosts | sudo $(shell which hostctl) add timestep.local --wait 0

imports:
	poetry run cdktf get --force --language python --log-level ${CDKTF_LOG_LEVEL} --output src/timestep/infra/imports

k3s-cluster:
	k3sup install --context timestep.ai --ip 143.244.178.23 --local-path secrets/kubeconfig --merge --skip-install --ssh-key ./.ssh/id_ed25519 --user ubuntu

pre-commit:
	poetry run pre-commit run --all-files

pyreverse:
	rm -rf docs && rm -rf */**/__pycache__ && mkdir docs && poetry run pyreverse --all-ancestors --all-associated --module-names y --colorized --output html --output-directory docs src.timestep

quasar-dev-android:
	cd src/timestep/projects/www && npx quasar dev -m capacitor -T android

ssh:
	ssh -i .ssh/id_ed25519 -o IdentitiesOnly=yes ubuntu@143.244.178.23
