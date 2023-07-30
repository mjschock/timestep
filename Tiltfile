load('ext://dotenv', 'dotenv')
load('ext://kubectl_build', 'kubectl_build')
load('ext://uibutton', 'cmd_button', 'bool_input', 'location', 'text_input')

dotenv('.env')

local_resource(
    'poetry install',
    cmd='poetry install',
    deps=[
        'pyproject.toml',
        'poetry.lock',
    ],
    labels=['build'],
)

local_resource(
    'poetry run cdktf get',
    auto_init=False,
    cmd='make imports',
    deps=[
        'cdktf.json',
    ],
    labels=['build'],
    resource_deps=['poetry install'],
)

local_resource(
    'poetry run pytest',
    auto_init=False,
    cmd='poetry run pytest',
    labels=['test'],
    resource_deps=['poetry install'],
    trigger_mode=TRIGGER_MODE_MANUAL,
)

local_resource(
    'poetry run cdktf deploy',
    cmd='poetry run cdktf deploy --auto-approve $STACK_ID',
    deps=[
        '.env',
        'cdktf.json',
        'pyproject.toml',
        'poetry.lock',
        'src/timestep/__main__.py',
        'src/timestep/config.py',
        'src/timestep/infra/stacks/main/stack.py',
        'src/timestep/infra/stacks/main/constructs/cloud_init_config/construct.py',
        'src/timestep/infra/stacks/main/constructs/cloud_instance/construct.py',
        'src/timestep/infra/stacks/main/constructs/cloud_instance_domain/construct.py',
        'src/timestep/infra/stacks/main/constructs/domain_name_registrar/construct.py',
        'src/timestep/infra/stacks/main/constructs/kube_config/construct.py',
        'src/timestep/infra/stacks/main/constructs/kubernetes_cluster_ingress/construct.py',
        'src/timestep/infra/stacks/main/constructs/prefect/construct.py',
        'src/timestep/infra/stacks/main/constructs/registry/construct.py',
    ],
    env={
        'STACK_ID': os.getenv('PRIMARY_DOMAIN_NAME'),
    },
    labels=['deploy'],
    resource_deps=[
    ]
)

cmd_button('poetry run cdktf destroy',
    argv=['sh', '-c', 'poetry run cdktf destroy $AUTO_APPROVE $STACK_ID'],
    env=[
        'STACK_ID=' + os.getenv('PRIMARY_DOMAIN_NAME'),
    ],
    icon_name='delete',
    inputs=[
        bool_input('AUTO_APPROVE', true_string='--auto-approve', false_string='', default=True),
    ],
    resource='poetry run cdktf deploy',
    text='poetry run cdktf destroy',
)

allow_k8s_contexts(
    os.getenv('KUBECONTEXT'),
)

# local_resource(
#     'hostctl watch',
#     serve_cmd='cat $HOSTS_FILE_PATH | sudo $(which hostctl) add $PRIMARY_DOMAIN_NAME --wait 0',
#     deps=[
#         '$HOSTS_FILE_PATH',
#         '.env',
#         os.getenv('CDKTF_OUTPUT') + "/stacks/" + os.getenv('PRIMARY_DOMAIN_NAME') + "/hosts",
#     ],
#     labels=['release'],
#     links=[
#         "https://" + str(local(command='echo $PRIMARY_DOMAIN_NAME')).strip(),
#     ],
#     resource_deps=[
#         'poetry run cdktf deploy',
#     ],
#     serve_env={
#         "PRIMARY_DOMAIN_NAME": os.getenv('PRIMARY_DOMAIN_NAME'),
#         "HOSTS_FILE_PATH": os.getenv('CDKTF_OUTPUT') + "/stacks/" + os.getenv('PRIMARY_DOMAIN_NAME') + "/hosts",
#     },
# )

# # k8s_resource('docker-registry', port_forwards=5000)
# port_forward(5000, host='registry.timestep.local')
# # port_forward(local_port=5000, container_port=5000, name="docker-registry")
# k8s_yaml("registry.yml")
# default_registry(
#     # 'localhost:5000',
#     host='registry.timestep.local:5000',
#     host_from_cluster='docker-registry:5000'
# )

# include('./src/timestep/projects/www/Tiltfile')

# docker_compose('docker-compose.yml')

# default_registry('ttl.sh/timestep-ai-6d8f0d30-2e75-11ee-9912-7f207c4fda56')
default_registry('registry.gitlab.com/timestep-ai/timestep')

# docker_build(
#     'tilt-avatar-api',
#     context='.',
#     dockerfile='./deploy/api.dockerfile',
#     only=['./api/'],
#     live_update=[
#         sync('./api/', '/app/api/'),
#         run(
#             'pip install -r /app/requirements.txt',
#             trigger=['./api/requirements.txt']
#         )
#     ]
# )

# # k8s_yaml automatically creates resources in Tilt for the entities
# # and will inject any images referenced in the Tiltfile when deploying
# # https://docs.tilt.dev/api.html#api.k8s_yaml
# k8s_yaml('deploy/api.yaml')

# # k8s_resource allows customization where necessary such as adding port forwards and labels
# # https://docs.tilt.dev/api.html#api.k8s_resource
# k8s_resource(
#     'api',
#     port_forwards='5734:5000',
#     labels=['backend']
# )


# # tilt-avatar-web is the frontend (ReactJS/vite app)
# # live_update syncs changed source files to the correct place for vite to pick up
# # and runs yarn (JS dependency manager) to update dependencies when changed
# # if vite.config.js changes, a full rebuild is performed because it cannot be
# # changed dynamically at runtime
# # https://docs.tilt.dev/api.html#api.docker_build
# # https://docs.tilt.dev/live_update_reference.html
# docker_build(
#     'tilt-avatar-web',
#     context='.',
#     dockerfile='./deploy/web.dockerfile',
#     only=['./web/'],
#     ignore=['./web/dist/'],
#     live_update=[
#         fall_back_on('./web/vite.config.js'),
#         sync('./web/', '/app/'),
#         run(
#             'yarn install',
#             trigger=['./web/package.json', './web/yarn.lock']
#         )
#     ]
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

# docker_build(
#     'tilt-avatar-www',
#     context='.',
#     dockerfile='./deploy/www.dockerfile',
#     only=['./www/'],
#     ignore=['./www/dist/'],
#     live_update=[
#         fall_back_on('./www/quasar.config.js'),
#         sync('./www/', '/app/'),
#         run(
#             'npm install',
#             trigger=['./www/package.json', './www/package-lock.json']
#         )
#     ]
# )

# k8s_yaml('deploy/www.yaml')

# k8s_resource(
#     'www',
#     port_forwards='5736:9000', # 5173 is the port Vite listens on in the container
#     labels=['frontend']
# )

docker_build(
    'rps',
    context='.',
    dockerfile='./deploy/rps.dockerfile',
    only=['./rps/'],
    ignore=['./rps/dist/'],
)

k8s_yaml('deploy/rps.yaml')

k8s_resource(
    'rps',
    port_forwards='9999:11345', # 5173 is the port Vite listens on in the container
    labels=['frontend', 'backend']
)

local_resource(
    'kompose convert',
    cmd='kompose convert --file docker-compose.yml --out deploy/rps.yaml --secrets-as-files',
    deps=[
        'docker-compose.yml',
    ],
)
