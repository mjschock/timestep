load('ext://dotenv', 'dotenv')
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
    cmd='poetry run cdktf get --force --language python --log-level $CDKTF_LOG_LEVEL --output src/timestep/infra/imports',
    deps=[
        'cdktf.json',
    ],
    labels=['build'],
    resource_deps=['poetry install'],
)

# local_resource(
#     'poetry run toml-sort',
#     cmd='poetry run toml-sort -ai pyproject.toml',
#     deps=[
#         'pyproject.toml',
#     ],
#     labels=['build'],
#     resource_deps=['poetry install'],
# )

local_resource(
    'prefect server',
    links=[
        'http://127.0.0.1:4200',
    ],
    resource_deps=['poetry install'],
    serve_cmd='poetry run prefect server start',
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
    cmd='poetry run cdktf deploy --auto-approve',
    deps=[
        '.env',
        'cdktf.json',
        'pyproject.toml',
        'poetry.lock',
        'src/timestep/__main__.py',
        'src/timestep/conf/blocks.py',
        'src/timestep/infra/stacks/k3s_cluster/stack.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/cloud_init_config/blocks.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/cloud_init_config/tasks.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/cloud_instance/blocks.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/cloud_instance/tasks.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/cloud_instance_domain/blocks.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/cloud_instance_domain/tasks.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/domain_name_registrar/construct.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/kube_config/blocks.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/kube_config/tasks.py',
        # 'src/timestep/infra/stacks/kubernetes_config/constructs/ingress_controller/construct.py',
    ],
    env={
    },
    labels=['deploy'],
    resource_deps=[
        # 'poetry install',
        'poetry run cdktf get',
    ]
)

cmd_button('poetry run cdktf destroy',
    argv=['sh', '-c', 'poetry run cdktf destroy $AUTO_APPROVE'],
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
    ],
    labels=['release'],
    links=[
        "https://" + str(local(command='echo $PRIMARY_DOMAIN_NAME')).strip(),
    ],
    serve_env={
        "PRIMARY_DOMAIN_NAME": os.getenv('PRIMARY_DOMAIN_NAME'),
        "HOSTS_FILE_PATH": os.getenv('CDKTF_OUTPUT') + "/stacks/" + os.getenv('PRIMARY_DOMAIN_NAME') + "/hosts",
    },
)

# k8s_yaml(listdir('src/timestep/infra/stacks/k3s_cluster/constructs/kubernetes_cluster/sample'))
