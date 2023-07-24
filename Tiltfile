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
        'src/timestep/conf/blocks.py',
        'src/timestep/infra/stacks/main/stack.py',
        'src/timestep/infra/stacks/main/constructs/cloud_init_config/construct.py',
        'src/timestep/infra/stacks/main/constructs/cloud_instance/construct.py',
        'src/timestep/infra/stacks/main/constructs/cloud_instance_domain/construct.py',
        'src/timestep/infra/stacks/main/constructs/domain_name_registrar/construct.py',
        'src/timestep/infra/stacks/main/constructs/kube_config/construct.py',
        'src/timestep/infra/stacks/main/constructs/kubernetes_cluster_ingress/construct.py',
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

local_resource(
    'hostctl watch',
    serve_cmd='cat $HOSTS_FILE_PATH | sudo $(which hostctl) add $PRIMARY_DOMAIN_NAME --wait 0',
    deps=[
        '$HOSTS_FILE_PATH',
        '.env',
        os.getenv('CDKTF_OUTPUT') + "/stacks/" + os.getenv('PRIMARY_DOMAIN_NAME') + "/hosts",
    ],
    labels=['release'],
    links=[
        "https://" + str(local(command='echo $PRIMARY_DOMAIN_NAME')).strip(),
    ],
    resource_deps=[
        'poetry run cdktf deploy',
    ],
    serve_env={
        "PRIMARY_DOMAIN_NAME": os.getenv('PRIMARY_DOMAIN_NAME'),
        "HOSTS_FILE_PATH": os.getenv('CDKTF_OUTPUT') + "/stacks/" + os.getenv('PRIMARY_DOMAIN_NAME') + "/hosts",
    },
)

# # k8s_resource('docker-registry', port_forwards=5000)
# port_forward(5000, host='registry.timestep.local')
# # port_forward(local_port=5000, container_port=5000, name="docker-registry")
# k8s_yaml("registry.yml")
# default_registry(
#     # 'localhost:5000',
#     host='registry.timestep.local:5000',
#     host_from_cluster='docker-registry:5000'
# )

include('./src/timestep/projects/www/Tiltfile')
