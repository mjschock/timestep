default:
	ark get tilt@v${TILT_VERSION}
	tilt up

clean:
	multipass delete timestep-ai --purge || true
	rm -rf cdktf.out

hosts:
	cat cdktf.out/stacks/timestep.local.k3s_cluster/hosts | sudo $(shell which hostctl) add timestep.local --wait 0

info:
	watch multipass info timestep-ai

imports:
	poetry run cdktf get --force --language python --log-level ${CDKTF_LOG_LEVEL} --output src/timestep/infra/imports

k3s-cluster:
	k3sup install --context timestep.ai --ip 146.190.45.80 --local-path secrets/kubeconfig --merge --skip-install --ssh-key ./.ssh/id_ed25519 --user ubuntu

kubeapps-port-forward:
	echo "Kubeapps URL: http://localhost:8484"
	kubectl port-forward --namespace kubeapps service/kubeapps 8484:80

kubeapps-token:
	kubectl get --namespace default secret kubeapps-operator-token -o go-template='{{.data.token | base64decode}}' && echo

kubernetes-dashboard-port-forward:
	src/timestep/infra/stacks/kubernetes_config/kubernetes_dashboard/kubernetes_dashboard_port_forward.sh

kubernetes-dashboard-token:
	src/timestep/infra/stacks/kubernetes_config/kubernetes_dashboard/kubernetes_dashboard_token.sh

local-tls-cert:
	ark get mkcert
	mkcert -install
	mkcert -cert-file secrets/local_tls_crt -key-file secrets/local_tls_key timestep.local www.timestep.local

# nvidia:
# 	ssh -i .ssh/id_ed25519 -o IdentitiesOnly=yes ubuntu@10.61.136.131 'bash -s' < src/timestep/infra/cicd/nvidia.sh

pre-commit:
	poetry run pre-commit run --all-files

pyreverse:
	rm -rf docs/Architecture && rm -rf */**/__pycache__ && mkdir docs/Architecture && poetry run pyreverse --all-ancestors --all-associated --module-names y --colorized --output html --output-directory docs/Architecture src.timestep

quasar-dev-android:
	cd src/timestep/services/frontend && npx quasar dev -m capacitor -T android

quasar-dev-electron:
	cd src/timestep/services/frontend && npx quasar dev -m electron --devtools

quasar-dev-ios:
	cd src/timestep/services/frontend && npx quasar dev -m capacitor -T ios

runner:
	cd actions-runner && ./run.sh

ssh:
	ssh -i .ssh/id_ed25519 -o IdentitiesOnly=yes ubuntu@146.190.45.80
