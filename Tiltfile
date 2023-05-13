# local_resource('install-multipass',
#     cmd='which multipasses > /dev/null || echo "Install Multipass"',
#     links=['https://multipass.run/install'],
# )

# local_resource('kompose',
#     auto_init=False,
#     cmd='docker run --rm --name kompose -v $PWD:/src femtopixel/kompose convert --chart --out /src/deploy/k8s --secrets-as-files --verbose --file docker-compose.yaml',
#     deps=['docker-compose.yaml'],
#     trigger_mode=TRIGGER_MODE_AUTO,
# )

# local_resource('terraform plan',
#     auto_init=False,
#     cmd='docker run --rm --name terraform -v $PWD:/src -w /src hashicorp/terraform:latest plan -out=deploy/infra/terraform.tfplan',
#     trigger_mode=TRIGGER_MODE_AUTO,
# )

# local_resource('terraform init -upgrade',
#     auto_init=False,
#     cmd='docker run --rm --name terraform -v $PWD:/src -w /src hashicorp/terraform:latest init -upgrade',
#     trigger_mode=TRIGGER_MODE_AUTO,
# )

# local_resource('terraform apply',
#     auto_init=False,
#     cmd='docker run --rm --name terraform -v $PWD:/src -v $(which multipass):/bin/multipass -w /src hashicorp/terraform:latest apply deploy/infra/terraform.tfplan',
#     trigger_mode=TRIGGER_MODE_AUTO,
# )

# local_resource(
#     auto_init=True,
#     name="start-prefect-server",
#     cmd="prefect server start --host 127.0.0.1 --port 4200",
# )

# local_resource(
#     auto_init=True,
#     name="local-prefect-server",
#     serve_cmd="prefect server start --host 127.0.0.1 --port 4200",
# )

# local_resource(
#     auto_init=True,
#     name="local-prefect-server",
#     serve_cmd="prefect worker start --type process --pool local-work"
# )

# local_resource(
#     auto_init=True,
#     serve_cmd="prefect worker start --type process --pool local-work"
# )

# docker_compose("./docker-compose.yaml")
