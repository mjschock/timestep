load('ext://dotenv', 'dotenv')
dotenv()

local_resource('install-cdktf',
    cmd='which cdktf > /dev/null || echo "Install CDKTF"',
    labels=['cdktf'],
    links=['https://developer.hashicorp.com/terraform/tutorials/cdktf/cdktf-install#install-cdktf'],
)

# local_resource('install-multipass',
#     cmd='which multipasses > /dev/null || echo "Install Multipass"',
#     labels=['cdktf'],
#     links=['https://multipass.run/install'],
# )

# local_resource('install-terraform',
#     cmd='which terraform > /dev/null || echo "Install Terraform"', # arkade get terraform
#     labels=['cdktf'],
#     links=['https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform'],
# )

local_resource('install-k3sup',
    cmd='which k3sup > /dev/null || echo "Install k3sup"',
    labels=['k3sup'],
    links=['https://github.com/alexellis/k3sup#download-k3sup-tldr'],
)

local_resource('cdktf-deploy',
    auto_init=False,
    cmd='cdktf deploy',
    labels=['cdktf'],
    resource_deps=['install-cdktf'],
    trigger_mode=TRIGGER_MODE_MANUAL,
)

local_resource('k3sup-install',
    auto_init=False,
    cmd='PRIVATE_SSH_KEY_PATH=./.ssh/id_rsa ./src/lib/k3sup-install.sh',
    labels=['k3sup'],
    resource_deps=['install-k3sup'],
    trigger_mode=TRIGGER_MODE_MANUAL,
)

local_resource('kompose-convert',
    auto_init=False,
    cmd='docker run --rm --name kompose -v $PWD:/src femtopixel/kompose convert --chart --out /src/dist/deploy/k8s/charts/timestep --secrets-as-files --verbose --file docker-compose.yaml',
    deps=['docker-compose.yaml'],
    labels=['kompose'],
    trigger_mode=TRIGGER_MODE_AUTO,
)

allow_k8s_contexts('k3s-cluster')

load('ext://helm_resource', 'helm_resource', 'helm_repo')
helm_repo('caddy-ingress-controller', 'https://caddyserver.github.io/ingress/')
helm_resource(
    name='mycaddy',
    chart='caddy-ingress-controller',
    namespace='caddy-system',
)

# helm_resource('caddy-ingress-controller',
#     chart='caddy-ingress/caddy-ingress',
#     # values={
#     #     'controller': {
#     #         'replicas': 1,
#     #         'service': {
#     #             'type': 'LoadBalancer',
#     #         },
#     #     },
#     # },
#     labels=['caddy'],
#     # trigger_mode=TRIGGER_MODE_AUTO,
# )
