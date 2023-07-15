default: clean
	./tilt-up.sh

clean:
	rm -rf */**/__pycache__
	rm -rf cdktf.out
	rm -rf docs
	rm -rf src/timestep/infra/imports

imports:
	poetry run cdktf get --force --language python --log-level ${CDKTF_LOG_LEVEL} --output src/timestep/infra/imports

k3s-cluster:
	k3sup install --context timestep.local --ip 10.159.189.238 --k3s-extra-args '--disable traefik' --local-path kubeconfig --skip-install --ssh-key ./.ssh/id_ed25519 --user ubuntu
	k3sup install --context timestep.ai --ip 146.190.169.137 --k3s-extra-args '--disable traefik' --local-path kubeconfig --merge --skip-install --ssh-key ./.ssh/id_ed25519 --user ubuntu

pre-commit:
	poetry run pre-commit run --all-files

pyreverse:
	rm -rf docs && rm -rf */**/__pycache__ && mkdir docs && poetry run pyreverse --all-ancestors --all-associated --module-names y --colorized --output html --output-directory docs src.timestep

ssh:
	ssh -i .ssh/id_ed25519 -o IdentitiesOnly=yes ubuntu@10.159.189.238
	ssh -i .ssh/id_ed25519 -o IdentitiesOnly=yes ubuntu@146.190.169.137
