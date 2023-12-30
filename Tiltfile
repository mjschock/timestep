load('ext://dotenv', 'dotenv')
load('ext://git_resource', 'git_checkout')
load('ext://helm_resource', 'helm_resource', 'helm_repo')
load('ext://kubectl_build', 'kubectl_build')
load('ext://uibutton', 'cmd_button', 'bool_input', 'location', 'text_input')

dotenv('.dot.env')
dotenv('.env')

local_resource(
    'npm install -g cdktf-cli',
    cmd='npm install -g cdktf-cli@$CDKTF_CLI_VERSION',
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
    auto_init=False,
    cmd='poetry add cdktf@$CDKTF_LIB_VERSION',
    labels=['build'],
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
    cmd='poetry run cdktf deploy --auto-approve $PRIMARY_DOMAIN_NAME.k3s_cluster $PRIMARY_DOMAIN_NAME.kubernetes_config $PRIMARY_DOMAIN_NAME.platform',
    deps=[
        '.dot.env',
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

allow_k8s_contexts(
    os.getenv('KUBECONTEXT'), # TODO: hardcode this to timestep.local instead?
)

if k8s_context() != 'timestep.local': # TODO: remove this?
    print('k8s context is not timestep.local, skipping k8s resources')
    exit()

local_resource(
    'port-forward argo-cd-server 8080:80',
    auto_init=False,
    labels=['ops'],
    links=['https://localhost:8080'],
    serve_cmd='src/timestep/infra/stacks/kubernetes_config/argo_cd/port_forward.sh',
)

if os.getenv('KUBE_PROMETHEUS_STACK_IS_ENABLED', False) == 'true':
    local_resource(
        'port-forward kube-prometheus-grafana 3000:80',
        auto_init=False,
        labels=['ops'],
        links=['http://localhost:3000'],
        serve_cmd='kubectl port-forward --namespace kube-prometheus svc/kube-prometheus-grafana 3000:80',
    )

if os.getenv('KUBEAPPS_IS_ENABLED', False) == 'true':
    local_resource(
        'port-forward kubeapps 8484:80',
        labels=['deploy'],
        links=['http://localhost:8484'],
        serve_cmd='make kubeapps-port-forward',
    )

local_resource(
    'port-forward kubernetes-dashboard 8443:8443',
    auto_init=False,
    labels=['ops'],
    links=['https://localhost:8443'],
    serve_cmd='make kubernetes-dashboard-port-forward',
)

local_resource(
    'port-forward hasura-graphql-engine 9000:8080',
    auto_init=False,
    labels=['ops'],
    links=['http://localhost:9000'],
    serve_cmd='kubectl port-forward --namespace default svc/hasura-graphql-engine 9000:8080',
)

local_resource(
    'port-forward minio 9001:9001',
    auto_init=False,
    labels=['ops'],
    links=['http://localhost:9001'],
    serve_cmd='src/timestep/infra/stacks/kubernetes_config/minio/scripts/port_forward.sh',
)

local_resource(
    'port-forward ollama 11434:80',
    auto_init=False,
    labels=['ops'],
    links=['http://localhost:11434', 'http://localhost:11434/api/tags'],
    serve_cmd='kubectl port-forward --namespace default svc/ollama 11434:80',
)

local_resource(
    'port-forward postgresql-postgresql-ha-pgpool 5432:5432',
    auto_init=False,
    labels=['ops'],
    serve_cmd='kubectl port-forward --namespace default svc/postgresql-postgresql-ha-pgpool 5432:5432',
)

local_resource(
    'port-forward prefect-server 4200:4200',
    auto_init=False,
    labels=['ops'],
    links=['http://localhost:4200'],
    serve_cmd='kubectl port-forward --namespace default svc/prefect-server 4200:4200',
)

if os.getenv('KUBE_RAY_IS_ENABLED', False) == 'true':
    local_resource(
        'port-forward ray-cluster-kuberay-head-svc 8265:8265',
        auto_init=False,
        labels=['ops'],
        links=['http://localhost:8265'],
        serve_cmd='kubectl port-forward --address 0.0.0.0 svc/ray-cluster-kuberay-head-svc 8265:8265',
    )

watch_file('src/timestep/infra/stacks/platform/timestep_ai')

if os.path.exists('src/timestep/infra/stacks/platform/timestep_ai'):
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
            "python",
            "-Xfrozen_modules=off",
            "-m",
            "debugpy",
            "--listen",
            "0.0.0.0:5678",
            "src/web/server.py",
            "--reload"
        ],
        live_update=[
            sync('src/timestep/services/web/src', '/home/ubuntu/app/src'),
        ],
        match_in_env_vars=True # https://docs.tilt.dev/custom_resource#env-variable-injection
    )

    if os.getenv('LOCAL_TLS_CERT_IS_ENABLED', False) == 'true':
        print('local tls cert is enabled')

        k8s_yaml(
            local(
                'helm template --values src/timestep/infra/stacks/platform/timestep_ai/values.' + os.getenv('PRIMARY_DOMAIN_NAME') + '.tls.yaml src/timestep/infra/stacks/platform/timestep_ai'
            )
        )

    else:
        print('local tls cert is disabled')

        k8s_yaml(
            local(
                'helm template --values src/timestep/infra/stacks/platform/timestep_ai/values.' + os.getenv('PRIMARY_DOMAIN_NAME') + '.yaml src/timestep/infra/stacks/platform/timestep_ai'
            )
        )

    k8s_resource(
        'caddy',
        objects=[
            'caddy:ingress',
            'caddy-certs'
        ]
    )

    k8s_resource(
        'frontend',
        links=['https://' + os.getenv('PRIMARY_DOMAIN_NAME')],
    )

    k8s_resource(
        'web',
        links=['https://' + os.getenv('PRIMARY_DOMAIN_NAME') + '/docs', 'https://' + os.getenv('PRIMARY_DOMAIN_NAME') + '/redoc'],
        port_forwards=[
            '5678:5678'
        ],
    )
