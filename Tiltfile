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
    'poetry run cdktf deploy',
    cmd='poetry run cdktf deploy --auto-approve $DOMAIN-tf-stack',
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
    argv=['sh', '-c', 'poetry run cdktf destroy $AUTO_APPROVE $DOMAIN-tf-stack'],
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
