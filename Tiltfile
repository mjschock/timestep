load('ext://dotenv', 'dotenv')
load('ext://uibutton', 'cmd_button', 'bool_input', 'location', 'text_input')

dotenv('.env')

local_resource(
    'ssh-keygen',
    auto_init=False,
    cmd='mkdir -p dist/.ssh && ssh-keygen -t rsa -C timestep-ai-$TARGET_ENVIRONMENT -f dist/.ssh/id_rsa.timestep-ai-$TARGET_ENVIRONMENT -N ""',
    env={
        'TARGET_ENVIRONMENT': os.getenv('TARGET_ENVIRONMENT'),
    },
    labels=['build'],
    trigger_mode=TRIGGER_MODE_MANUAL,
)

local_resource(
    'kompose convert',
    cmd='rm -rf dist/deploy/k8s && kompose convert --chart --out dist/deploy/k8s/charts/timestep-ai-platform --secrets-as-files',
    deps=[
        'docker-compose.yml',
    ],
    labels=['build'],
)

local_resource(
    'cdktf deploy base',
    cmd='poetry run cdktf deploy --auto-approve timestep-ai-local-base-stack',
    deps=[
        'src/timestep/__main__.py',
        'src/timestep/infra/stacks/base',
    ],
    labels=['deploy']
)

cmd_button('cdktf deploy base:cdktf destroy base',
    argv=['sh', '-c', 'cdktf destroy --auto-approve timestep-ai-local-base-stack'],
    icon_name='delete',
    resource='cdktf deploy base',
    text='cdktf destroy base',
)

allow_k8s_contexts([
    'timestep-ai-k3s-cluster',
])

local_ip=local(
    command="multipass list | grep timestep-ai | awk '{print $3}'"
)

print(os.getenv('KUBECONFIG'))

local_resource(
    'k3sup get kubeconfig',
    cmd="k3sup install --context timestep-ai-k3s-cluster --ip $local_ip --local-path $local_path --skip-install --user ubuntu",
    deps=[
        'src/timestep/__main__.py',
        'src/timestep/infra/stacks/base',
    ],
    env={
        'local_ip': local_ip,
        'local_path': os.getenv('KUBECONFIG'),
    },
    labels=['deploy'],
    resource_deps=['cdktf deploy base']
)

local_resource(
    'cdktf deploy k8s',
    cmd='poetry run cdktf deploy --auto-approve timestep-ai-local-k8s-stack',
    deps=[
        'src/timestep/__main__.py',
        'src/timestep/infra/stacks/k8s',
    ],
    labels=['deploy'],
    resource_deps=['cdktf deploy base', 'k3sup get kubeconfig']
)

local_resource(
    'cdktf deploy platform',
    cmd='poetry run cdktf deploy --auto-approve timestep-ai-local-platform-stack',
    deps=[
        'src/timestep/__main__.py',
        'src/timestep/infra/stacks/platform',
    ],
    labels=['deploy'],
    resource_deps=['cdktf deploy k8s']
)

# k8s_yaml(listdir('dist/deploy/ingress/kubernetes/sample'))

# k8s_resource(
#     'example1',
#     labels=['deploy'],
#     new_name='agent',
# )

# k8s_resource(
#     'example2',
#     labels=['deploy'],
#     new_name='env',
# )

# k8s_resource(
#     labels=['deploy'],
#     new_name='ingress',
#     objects=[
#         'caddy-global-options:configmap',
#         'example:ingress',
#     ]
# )

local_resource(
    'hostctl add domains',
    cmd='echo sudo /home/mjschock/.arkade/bin/hostctl add domains timestep-ai timestep.local www.timestep.local --ip $local_ip',
    env={
        'local_ip': local_ip,
    },
    labels=['release'],
    # resource_deps=['ingress']
)

# k8s_yaml(helm('./dist/deploy/k8s/charts/timestep-ai-platform'))

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
