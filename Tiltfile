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
    # cmd='poetry run cdktf deploy --auto-approve --output $CDKTF_OUTDIR $STACK_ID',
    cmd='poetry run cdktf deploy --auto-approve $STACK_ID',
    deps=[
        '.env',
        'cdktf.json',
        'pyproject.toml',
        'poetry.lock',
        'src/timestep/__init__.py',
        'src/timestep/__main__.py',
        'src/timestep/conf.py',
        'src/timestep/infra/stacks/base/stack.py',
        'src/timestep/infra/stacks/base/constructs/cloud_init_config/construct.py',
        'src/timestep/infra/stacks/base/constructs/cloud_instance/construct.py',
        'src/timestep/infra/stacks/base/constructs/cloud_instance_domain/construct.py',
    ],
    env={
        # "CDKTF_OUTDIR": os.getenv('CDKTF_OUTDIR'),
        "STACK_ID": os.getenv('STACK_ID'),
    },
    labels=['deploy'],
    resource_deps=['poetry install']
)

cmd_button('poetry run cdktf destroy',
    # argv=['sh', '-c', 'poetry run cdktf destroy $AUTO_APPROVE --output $CDKTF_OUTDIR $STACK_ID'],
    argv=['sh', '-c', 'poetry run cdktf destroy $AUTO_APPROVE $STACK_ID'],
    icon_name='delete',
    inputs=[
        bool_input('AUTO_APPROVE', true_string='--auto-approve', false_string='', default=True),
        # text_input('CDKTF_OUTDIR', default=os.getenv('CDKTF_OUTDIR')),
        text_input('STACK_ID', default=os.getenv('STACK_ID')),
    ],
    resource='poetry run cdktf deploy',
    text='poetry run cdktf destroy',
)

local_resource(
    'hostctl watch',
    serve_cmd='cat $HOSTS_FILE_PATH | sudo $(which hostctl) add $STACK_ID --wait 0',
    deps=[
        '$HOSTS_FILE_PATH',
    ],
    env={
        "HOSTS_FILE_PATH": os.getenv('HOSTS_FILE_PATH'),
        "STACK_ID": os.getenv('STACK_ID'),
    },
)
