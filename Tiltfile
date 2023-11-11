load('ext://dotenv', 'dotenv')
load('ext://git_resource', 'git_checkout')
load('ext://helm_resource', 'helm_resource', 'helm_repo')
load('ext://kubectl_build', 'kubectl_build')
load('ext://uibutton', 'cmd_button', 'bool_input', 'location', 'text_input')

dotenv('.env')

local_resource(
    'npm install -g cdktf-cli',
    cmd='npm install -g cdktf-cli@$CDKTF_CLI_VERSION',
    # env={
    #     'CDKTF_CLI_VERSION': os.getenv('CDKTF_CLI_VERSION'),
    # },
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

# local_resource(
#     'poetry add cdktf',
#     cmd='poetry add cdktf@$CDKTF_LIB_VERSION',
#     env={
#         'PRIMARY_DOMAIN_NAME': os.getenv('CDKTF_LIB_VERSION'),
#     },
#     labels=['build'],
#     resource_deps=[
#         'poetry install',
#     ],
# )

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
    cmd='poetry run cdktf deploy --auto-approve $PRIMARY_DOMAIN_NAME.k3s_cluster $PRIMARY_DOMAIN_NAME.kubernetes_config $PRIMARY_DOMAIN_NAME.platform',
    deps=[
        '.env',
        'cdktf.json',
        'pyproject.toml',
        'poetry.lock',
        'src/timestep/__main__.py',
        'src/timestep/config.py',
        'src/timestep/infra/stacks/k3s_cluster',
        'src/timestep/infra/stacks/kubernetes_config',
        'src/timestep/infra/stacks/platform',
    ],
    env={
        # 'KUBERNETES_MASTER': 'https://kubernetes.default.svc',
        # 'KUBECONFIG': 'secrets/kubeconfig',
        'PRIMARY_DOMAIN_NAME': os.getenv('PRIMARY_DOMAIN_NAME'),
    },
    ignore=[
        '__pycache__',
        '*/**/__pycache__',
    ],
    labels=['deploy'],
    resource_deps=['poetry install'],
)

cmd_button('poetry run cdktf destroy',
    argv=['sh', '-c', 'poetry run cdktf destroy $AUTO_APPROVE $PRIMARY_DOMAIN_NAME.k3s_cluster $PRIMARY_DOMAIN_NAME.kubernetes_config $PRIMARY_DOMAIN_NAME.platform'],
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

# watch_file('secrets/kubeconfig')

allow_k8s_contexts(
    os.getenv('KUBECONTEXT'),
)

local_resource(
    'kubeapps',
    labels=['deploy'],
    links=['http://localhost:8484'],
    serve_cmd='make kubeapps-port-forward',
)

watch_file('src/timestep/infra/stacks/platform')

if os.path.exists('src/timestep/infra/stacks/platform'):
    docker_build(
        'registry.gitlab.com/timestep-ai/timestep/caddy',
        context='src/timestep/services/caddy',
        live_update=[
            sync('src/timestep/services/caddy/src', '/home/ubuntu/app/src'),
            run(
                'caddy reload --config /home/ubuntu/app/src/Caddyfile --adapter caddyfile',
                trigger=['src/timestep/services/caddy/src/Caddyfile']
            )
        ],
    )

    docker_build(
        'registry.gitlab.com/timestep-ai/timestep/frontend',
        context='src/timestep/services/frontend',
        entrypoint=[
            "/home/ubuntu/docker-entrypoint.sh",
            "quasar",
            "dev",
            "-m",
            "spa"
        ],
        # entrypoint=["/home/ubuntu/docker-entrypoint.sh", "npm", "run", "dev"],
        # entrypoint="npm run dev",
        # ignore=['dist', 'node_modules', 'src-capacitor', 'src-electron'],
        live_update=[
            fall_back_on('src/timestep/services/frontend/quasar.config.js'),
            sync('src/timestep/services/frontend', '/home/ubuntu/app'),
            run(
                'npm install',
                trigger=['src/timestep/services/frontend/package.json', 'src/timestep/services/frontend/package-lock.json']
            )
        ],
        # only=['.'],
        # extra_tag=str(local(command='echo $VERSION')).strip(),
    )

    docker_build(
        'registry.gitlab.com/timestep-ai/timestep/web',
        context='src/timestep/services/web',
        entrypoint=[
            "/home/ubuntu/app/docker-entrypoint.sh",
            "poetry",
            "run",
            "uvicorn",
            "src.web.main:app",
            "--proxy-headers",
            "--host",
            "0.0.0.0",
            "--port",
            "5000",
            "--reload"
        ],
        live_update=[
            sync('src/timestep/services/web/src', '/home/ubuntu/app/src'),
        ],
    )

    # custom_build(
    # docker_build(
    #     'registry.gitlab.com/timestep-ai/timestep/caddy',
    #     cache_from='registry.gitlab.com/timestep-ai/timestep/caddy:latest',
    #     # command='docker build -t $EXPECTED_REF src/timestep/services/caddy',
    #     context='src/timestep/services/caddy',
    #     dockerfile='src/timestep/services/caddy/Dockerfile',
    #     # deps=['src/timestep/services/caddy'],
    #     # disable_push=True,
    #     live_update=[
    #         sync('./src/timestep/services/caddy/src', '/home/ubuntu/src/'),
    #         run(
    #             'caddy reload --config /home/ubuntu/src/Caddyfile --adapter caddyfile',
    #             trigger=['./src/timestep/services/caddy/src/Caddyfile']
    #         )
    #     ],
    #     # skips_local_docker=True,
    #     # tag=str(local(command='echo $VERSION')).strip(),
    # )

    # docker_build(
    #     'registry.gitlab.com/timestep-ai/timestep/frontend',
    #     build_args={
    #     #     # 'CDKTF_CLI_VERSION': os.getenv('CDKTF_CLI_VERSION'),
    #     #     # 'NODENV_VERSION': os.getenv('NODENV_VERSION'),
    #         'PRIMARY_DOMAIN_NAME': os.getenv('PRIMARY_DOMAIN_NAME'),
    #     },
    #     cache_from='registry.gitlab.com/timestep-ai/timestep/frontend:latest',
    #     context='src/timestep/services/frontend',
    #     dockerfile='src/timestep/services/frontend/Dockerfile',
    #     # entrypoint='quasar dev -m spa -p 9000',
    #     # entrypoint=["quasar", "dev", "-m", "spa", "-p", "9000"],
    #     # entrypoint=["/home/ubuntu/docker-entrypoint.sh", "quasar", "dev", "-m", "spa", "-p", "9000"],
    #     entrypoint=["/home/ubuntu/docker-entrypoint.sh", "quasar", "dev", "-m", "spa"],
    #     # only=['.'],
    #     # ignore=['./dist/', 'node_modules', './src-capacitor/', './src-electron/'],
    #     # live_update=[
    #     #     fall_back_on('./src/timestep/services/frontend/quasar.config.js'),
    #     #     # sync('./src/timestep/services/frontend/', '/home/ubuntu'),
    #     #     sync('./src/timestep/services/frontend/src/', '/home/ubuntu/src/'),
    #     #     run(
    #     #         'npm install',
    #     #         trigger=['./src/timestep/services/frontend/package.json', './src/timestep/services/frontend/package-lock.json']
    #     #     )
    #     # ],
    #     pull=True,
    # )

    # custom_build(
    #     'registry.gitlab.com/timestep-ai/timestep/frontend',
    #     # command='docker build -t $EXPECTED_REF src/timestep/services/frontend',
    #     command='docker buildx build --build-arg PRIMARY_DOMAIN_NAME=$PRIMARY_DOMAIN_NAME --cache-from registry.gitlab.com/timestep-ai/timestep/frontend:latest --push --tag $EXPECTED_REF src/timestep/services/frontend',
    #     deps=['src/timestep/services/frontend'],
    #     # disable_push=True,
    #     # live_update=[
    #     #     sync('./src/timestep/services/caddy/', '/etc/caddy/'),
    #     #     run(
    #     #         'caddy reload --config /etc/caddy/Caddyfile --adapter caddyfile',
    #     #         trigger=['./src/timestep/services/caddy/Caddyfile']
    #     #     )
    #     # ],
    #     # skips_local_docker=True,
    #     # tag=str(local(command='echo $VERSION')).strip(),
    # )

    # docker_build(
    #     'registry.gitlab.com/timestep-ai/timestep/api',
    #     context='./src/timestep/services/api',
    #     dockerfile='./src/timestep/services/api/Dockerfile',
    #     extra_tag=['dev'],
    #     pull=True,
    # )

    # custom_build(
    #     'registry.gitlab.com/timestep-ai/timestep/api',
    #     # command='docker build --build-arg DOCKER_IMAGE_REF=$EXPECTED_REF -t $EXPECTED_REF src/timestep/services/api && tilt dump image-deploy-ref $EXPECTED_REF',
    #     command='docker build -t $EXPECTED_REF src/timestep/services/api',
    #     deps=['src/timestep/services/api'],
    #     # entrypoint=["poetry", "run", "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000", "--reload"],
    #     entrypoint="poetry run uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 5000 --reload",
    #     # env={
    #     #     # 'CI_TAG': '1.2.0',
    #     #     'CI_TAG': '$EXPECTED_REF',
    #     # },
    #     # disable_push=True,
    #     live_update=[
    #         sync('./src/timestep/services/api/app/', '/home/ubuntu/src/timestep/services/api/app/'),
    #         # run(
    #         #     'caddy reload --config /etc/caddy/Caddyfile --adapter caddyfile',
    #         #     trigger=['./src/timestep/services/caddy/Caddyfile']
    #         # )
    #     ],
    #     # match_in_env_vars=True,
    #     # skips_local_docker=True,
    #     # tag=str(local(command='echo $VERSION')).strip(),
    # )

    # k8s_kind(
    #     'WorkflowTemplate',
    #     api_version='argoproj.io/v1alpha1',
    #     image_json_path=[
    #         '{.spec.templates[?(@.container.image)].container.image}', 
    #         '{.spec.templates[?(@.script.image)].script.image}'
    #     ],
    #     pod_readiness='ignore',
    # )

    k8s_yaml(
        local(
            'helm template --values src/timestep/infra/stacks/platform/values.' + os.getenv('PRIMARY_DOMAIN_NAME') + '.yaml src/timestep/infra/stacks/platform'
        )
    )
