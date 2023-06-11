load('ext://dotenv', 'dotenv')
load('ext://uibutton', 'cmd_button', 'bool_input', 'location', 'text_input')

dotenv('.env')

# local_resource(
#     'ssh-keygen',
#     cmd='mkdir -p dist/.ssh && ssh-keygen -t rsa -C timestep-ai-$TARGET_ENVIRONMENT -f dist/.ssh/id_rsa.timestep-ai-$TARGET_ENVIRONMENT -N "" || true',
#     env={
#         'TARGET_ENVIRONMENT': os.getenv('TARGET_ENVIRONMENT'),
#     },
#     labels=['build'],
# )

# local_resource(
#     'kompose convert',
#     # cmd='rm -rf dist/deploy/k8s && kompose convert --build local --chart --out dist/deploy/k8s/charts/timestep-ai-platform --push-image --push-image-registry registry.timestep.local --secrets-as-files',
#     cmd='rm -rf dist/deploy/k8s && kompose convert --build local --chart --out dist/deploy/k8s/charts/timestep-ai-platform --push-image-registry registry.timestep.local --secrets-as-files',
#     deps=[
#         'docker-compose.yml',
#     ],
#     labels=['build'],
# )

local_resource(
    'cdktf deploy base',
    cmd='poetry run cdktf deploy --auto-approve timestep.local-base-stack',
    deps=[
        'src/timestep/__main__.py',
        'src/timestep/conf.py',
        'src/timestep/infra/stacks/base',
    ],
    labels=['deploy']
)

cmd_button('cdktf deploy base:cdktf destroy base',
    argv=['sh', '-c', 'cdktf destroy --auto-approve timestep.local-base-stack'],
    icon_name='delete',
    resource='cdktf deploy base',
    text='cdktf destroy base',
)

allow_k8s_contexts([
    'timestep-ai-k3s-cluster',
])

# local_resource(
#     'k3sup get kubeconfig',
#     cmd="k3sup install --context timestep-ai-k3s-cluster --ip $local_ip --local-path $local_path --skip-install --ssh-key $ssh_key_path --user ubuntu",
#     deps=[
#         'src/timestep/__main__.py',
#         'src/timestep/conf.py',
#         'src/timestep/infra/stacks/base',
#     ],
#     env={
#         'local_ip': local(command="multipass list | grep timestep-ai | awk '{print $3}'"),
#         'local_path': os.getenv('KUBECONFIG'),
#         'ssh_key_path': os.getenv('SSH_KEY_PATH'),
#     },
#     labels=['deploy'],
#     resource_deps=['cdktf deploy base']
# )

# local_resource(
#     'cdktf deploy k8s',
#     cmd='poetry run cdktf deploy --auto-approve timestep-ai-local-k8s-stack',
#     deps=[
#         # 'src/timestep/__main__.py',
#         'src/timestep/infra/stacks/kubernetes',
#     ],
#     labels=['deploy'],
#     resource_deps=['cdktf deploy base', 'k3sup get kubeconfig']
# )

# cmd_button('cdktf deploy k8s:cdktf destroy k8s',
#     argv=['sh', '-c', 'cdktf destroy --auto-approve timestep-ai-local-k8s-stack'],
#     icon_name='delete',
#     resource='cdktf deploy k8s',
#     text='cdktf destroy k8s',
# )

# local_resource(
#     'cdktf deploy platform',
#     cmd='poetry run cdktf deploy --auto-approve timestep-ai-local-platform-stack',
#     deps=[
#         'dist/deploy/k8s/charts/timestep-ai-platform',
#         # 'src/timestep/__main__.py',
#         'src/timestep/infra/stacks/platform',
#     ],
#     labels=['deploy'],
#     resource_deps=['cdktf deploy k8s']
# )

# cmd_button('cdktf deploy platform:cdktf destroy platform',
#     argv=['sh', '-c', 'cdktf destroy --auto-approve timestep-ai-local-platform-stack'],
#     icon_name='delete',
#     resource='cdktf deploy platform',
#     text='cdktf destroy platform',
# )

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

# local_resource(
#     'hostctl add domains',
#     cmd='echo sudo /home/mjschock/.arkade/bin/hostctl remove timestep-ai && echo sudo /home/mjschock/.arkade/bin/hostctl add domains timestep-ai timestep.local registry.timestep.local www.timestep.local --ip $local_ip',
#     env={
#         'local_ip': local(command="multipass list | grep timestep-ai | awk '{print $3}'"),
#     },
#     labels=['release'],
#     # resource_deps=['ingress']
# )

# if os.path.exists('dist/deploy/k8s/charts/timestep-ai-platform'):
#     k8s_yaml(
#         helm(
#             './dist/deploy/k8s/charts/timestep-ai-platform',
#             name='timestep-ai-platform',
#             namespace='default',
#         )
#     )

# k8s_yaml(
#     listdir('src/timestep/ingress')
# )
