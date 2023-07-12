default: clean
	./tilt-up.sh

clean:
	rm -rf cdktf.out
	rm -rf docs
	rm -rf src/timestep/infra/imports

k3s-cluster:
	k3sup install --context timestep.local --ip 10.159.189.181 --k3s-extra-args '--disable traefik' --local-path kubeconfig --merge --ssh-key ./.ssh/id_ed25519 --user ubuntu
	k3sup install --context timestep.ai --ip 164.92.78.111 --k3s-extra-args '--disable traefik' --local-path kubeconfig --merge --ssh-key ./.ssh/id_ed25519 --user ubuntu

pre-commit:
	poetry run pre-commit run --all-files

pyreverse:
	mkdir docs && poetry run pyreverse --all-ancestors --all-associated --module-names y --colorized --output html --output-directory docs src.timestep

ssh:
	ssh -i .ssh/id_ed25519 -o IdentitiesOnly=yes ubuntu@10.159.189.181
	ssh -i .ssh/id_ed25519 -o IdentitiesOnly=yes ubuntu@164.92.78.111
