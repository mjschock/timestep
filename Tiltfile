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
    'kompose convert',
    cmd='rm -rf $PLATFORM_CHART_PATH && kompose convert --build local --chart --out $PLATFORM_CHART_PATH --push-image --push-image-registry registry.timestep.local',
    deps=[
        'docker-compose.yml',
    ],
    env={
        "PLATFORM_CHART_PATH": os.getenv('PLATFORM_CHART_PATH', 'dist/charts/platform'),
    },
    labels=['build'],
)

local_resource(
    'poetry run cdktf deploy',
    cmd='poetry run cdktf deploy --auto-approve $DOMAIN-base-stack',
    deps=[
        'src/timestep/__main__.py',
        'src/timestep/conf.py',
        'src/timestep/infra/stacks/base/stack.py',
    ],
    env={
        "DOMAIN": os.getenv('DOMAIN', 'timestep.local'),
    },
    labels=['deploy'],
    resource_deps=['poetry install']
)

cmd_button('poetry run cdktf destroy',
    argv=['sh', '-c', 'poetry run cdktf destroy $AUTO_APPROVE $DOMAIN-base-stack'],
    icon_name='delete',
    inputs=[
        bool_input('AUTO_APPROVE', true_string='--auto-approve', false_string='', default=True),
        text_input('DOMAIN', default=os.getenv('DOMAIN', 'timestep.local')),
    ],
    resource='poetry run cdktf deploy',
    text='poetry run cdktf destroy',
)

local_resource(
    'hostctl watch',
    serve_cmd='cat dist/.etchosts | sudo $(which hostctl) add timestep-ai --wait 0',
    deps=[
        'dist/.etchosts',
    ],
)
