load('ext://dotenv', 'dotenv')
load('ext://git_resource', 'git_checkout')
load('ext://helm_resource', 'helm_resource', 'helm_repo')
load('ext://kubectl_build', 'kubectl_build')
load('ext://uibutton', 'cmd_button', 'bool_input', 'location', 'text_input')

dotenv('.env')

local_resource(
    'npm install -g cdktf-cli',
    cmd='npm install -g cdktf-cli@$CDKTF_CLI_VERSION',
    env={
        'PRIMARY_DOMAIN_NAME': os.getenv('CDKTF_CLI_VERSION'),
    },
    labels=['build'],
)

local_resource(
    'poetry install',
    cmd='poetry install',
    deps=[
        'pyproject.toml',
        'poetry.lock',
    ],
    labels=['build'],
    resource_deps=[
        'npm install -g cdktf-cli',
    ],
)

local_resource(
    'poetry add cdktf',
    cmd='poetry add cdktf@$CDKTF_LIB_VERSION',
    env={
        'PRIMARY_DOMAIN_NAME': os.getenv('CDKTF_LIB_VERSION'),
    },
    labels=['build'],
    resource_deps=[
        'poetry install',
    ],
)

local_resource(
    'prefect server start',
    auto_init=False,
    serve_cmd='poetry run prefect server start',
    resource_deps=[
        'poetry install',
    ],
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
    cmd='poetry run cdktf deploy --auto-approve $PRIMARY_DOMAIN_NAME.k3s_cluster $PRIMARY_DOMAIN_NAME.kubernetes_config',
    deps=[
        '.env',
        'cdktf.json',
        'pyproject.toml',
        'poetry.lock',
        'src/timestep/__main__.py',
        'src/timestep/config.py',
        'src/timestep/infra/stacks/k3s_cluster/stack.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/cloud_init_config/construct.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/cloud_instance/construct.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/cloud_instance_domain/construct.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/domain_name_registrar/construct.py',
        'src/timestep/infra/stacks/k3s_cluster/constructs/kube_config/construct.py',
        'src/timestep/infra/stacks/kubernetes_config/stack.py',
        'src/timestep/infra/stacks/kubernetes_config/constructs/kubernetes_cluster_ingress/construct.py',
        'src/timestep/infra/stacks/kubernetes_config/constructs/kubernetes_dashboard/construct.py',
        'src/timestep/infra/stacks/kubernetes_config/constructs/minio/construct.py',
        'src/timestep/infra/stacks/kubernetes_config/constructs/prefect/construct.py',
        'src/timestep/infra/stacks/kubernetes_config/constructs/registry/construct.py',
        'src/timestep/infra/stacks/kubernetes_config/constructs/timestep_ai/construct.py',
        'timestep-ai',
        'timestep-ai-0.0.1.tgz',
    ],
    env={
        'PRIMARY_DOMAIN_NAME': os.getenv('PRIMARY_DOMAIN_NAME'),
    },
    labels=['deploy'],
    resource_deps=[
    ]
)

cmd_button('poetry run cdktf destroy',
    argv=['sh', '-c', 'poetry run cdktf destroy $AUTO_APPROVE $PRIMARY_DOMAIN_NAME.k3s_cluster $PRIMARY_DOMAIN_NAME.kubernetes_config'],
    env=[
        'PRIMARY_DOMAIN_NAME=' + os.getenv('PRIMARY_DOMAIN_NAME'),
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
#     'kompose convert',
#     cmd='rm -rf timestep-ai/templates && kompose convert --chart --file docker-compose.yml --out timestep-ai --secrets-as-files --verbose',
#     deps=[
#         '.env',
#         'docker-compose.yml',
#     ],
#     labels=['build'],
# )

watch_file('timestep-ai')

if os.path.exists('timestep-ai'):
    local_resource(
        'helm package',
        cmd='helm package timestep-ai --destination dist --version $VERSION',
        deps=['timestep-ai'],
        labels=['build'],
        # resource_deps=[
        #     'kompose convert',
        # ]
    )

    custom_build(
        'registry.gitlab.com/timestep-ai/timestep/caddy',
        command='docker build -t $EXPECTED_REF src/timestep/services/caddy',
        deps=['src/timestep/services/caddy'],
        disable_push=True,
        live_update=[
            sync('./src/timestep/services/caddy/', '/etc/caddy/'),
            run(
                'caddy reload --config /etc/caddy/Caddyfile --adapter caddyfile',
                trigger=['./src/timestep/services/caddy/Caddyfile']
            )
        ],
        skips_local_docker=True,
        tag=str(local(command='echo $VERSION')).strip(),
    )

    # docker_build(
    #     'registry.gitlab.com/timestep-ai/timestep/api',
    #     context='./src/timestep/services/api',
    #     dockerfile='./src/timestep/services/api/Dockerfile',
    #     extra_tag=['dev'],
    #     pull=True,
    # )

    custom_build(
        'registry.gitlab.com/timestep-ai/timestep/api',
        # command='docker build --build-arg DOCKER_IMAGE_REF=$EXPECTED_REF -t $EXPECTED_REF src/timestep/services/api && tilt dump image-deploy-ref $EXPECTED_REF',
        command='docker build -t $EXPECTED_REF src/timestep/services/api',
        deps=['src/timestep/services/api'],
        # entrypoint=["poetry", "run", "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000", "--reload"],
        entrypoint="poetry run uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 5000 --reload",
        # env={
        #     # 'CI_TAG': '1.2.0',
        #     'CI_TAG': '$EXPECTED_REF',
        # },
        # disable_push=True,
        live_update=[
            sync('./src/timestep/services/api/app/', '/home/ubuntu/src/timestep/services/api/app/'),
            # run(
            #     'caddy reload --config /etc/caddy/Caddyfile --adapter caddyfile',
            #     trigger=['./src/timestep/services/caddy/Caddyfile']
            # )
        ],
        # match_in_env_vars=True,
        # skips_local_docker=True,
        # tag=str(local(command='echo $VERSION')).strip(),
    )

    docker_build(
        'registry.gitlab.com/timestep-ai/timestep/www',
        build_args={
         'NODENV_VERSION': os.getenv('NODENV_VERSION'),
        },
        context='src/timestep/services/www',
        dockerfile='src/timestep/services/www/Dockerfile',
        entrypoint='quasar dev -m spa -p 9000',
        only=['.'],
        ignore=['./dist/', './src-capacitor/', './src-electron/'],
        live_update=[
            fall_back_on('./src/timestep/services/www/quasar.config.js'),
            sync('./src/timestep/services/www/', '/home/node/app'),
            run(
                'npm install',
                trigger=['./src/timestep/services/www/package.json', './src/timestep/services/www/package-lock.json']
            )
        ],
        pull=True,
    )

    k8s_yaml(local('helm template timestep-ai'))
