load('ext://dotenv', 'dotenv')
load('ext://git_resource', 'git_checkout')

dotenv('.env')

tiltfile_path = config.main_path

local_resource(
    'ssh-keygen',
    auto_init=False,
    cmd='ssh-keygen -t rsa -C timestep-ai-$TARGET_ENVIRONMENT -f $HOME/.ssh/id_rsa.timestep-ai-$TARGET_ENVIRONMENT -N ""',
    env={
        'TARGET_ENVIRONMENT': os.getenv('TARGET_ENVIRONMENT'),
    },
    labels=['build'],
    trigger_mode=TRIGGER_MODE_MANUAL,
)

allow_k8s_contexts([
    'timestep-ai-k3s-cluster',
])

local_resource(
    'cdktf deploy base',
    cmd='poetry run cdktf deploy --auto-approve timestep-ai-local',
    deps=[
        'src/timestep/__main__.py',
    ],
    labels=['deploy']
)

local_ip=local(
    command="multipass list | grep timestep-ai | awk '{print $3}'"
)

local_resource(
    'k3sup get kubeconfig',
    cmd="k3sup install --context timestep-ai-k3s-cluster --ip $local_ip --local-path $HOME/.kube/config --merge --skip-install --user ubuntu",
    env={
        'local_ip': local_ip,
    },
    labels=['deploy'],
    resource_deps=['cdktf deploy base']
)

local_resource(
    'cdktf deploy k8s',
    cmd='poetry run cdktf deploy --auto-approve timestep-ai-local timestep-ai-local-k8s-stack',
    deps=[
        'src/timestep/__main__.py',
    ],
    labels=['deploy'],
    resource_deps=['cdktf deploy base']
)

k8s_yaml(listdir('dist/deploy/ingress/kubernetes/sample'))

k8s_resource(
    'example1',
    labels=['deploy'],
    new_name='agent',
)

k8s_resource(
    'example2',
    labels=['deploy'],
    new_name='env',
)

k8s_resource(
    labels=['deploy'],
    new_name='ingress',
    objects=[
        'caddy-global-options:configmap',
        'example:ingress',
    ]
)

local_resource(
    'hostctl add domains',
    cmd='echo sudo /home/mjschock/.arkade/bin/hostctl add domains timestep-ai mjschock.timestep.local www.timestep.local --ip $local_ip',
    env={
        'local_ip': local_ip,
    },
    labels=['release'],
    resource_deps=['agent', 'env', 'ingress']
)

# # k8s_resource allows customization where necessary such as adding port forwards and labels
# # https://docs.tilt.dev/api.html#api.k8s_resource
# k8s_resource(
#     'api',
#     port_forwards='5734:5000',
#     labels=['backend']
# )

# # k8s_yaml automatically creates resources in Tilt for the entities
# # and will inject any images referenced in the Tiltfile when deploying
# # https://docs.tilt.dev/api.html#api.k8s_yaml
# k8s_yaml('deploy/web.yaml')

# # k8s_resource allows customization where necessary such as adding port forwards and labels
# # https://docs.tilt.dev/api.html#api.k8s_resource
# k8s_resource(
#     'web',
#     port_forwards='5735:5173', # 5173 is the port Vite listens on in the container
#     labels=['frontend']
# )
