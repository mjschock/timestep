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

# docker_build(
#     'www',
#     context='.',
#     dockerfile='Dockerfile',
#     # env={
#     #     'PROJECT_NAME': 'rps',
#     # },
#     only=[
#         './www/',
#         'pyproject.toml',
#         'poetry.lock',
#         'Caddyfile',
#     ],
#     ignore=['./www/dist/'],
# )

# k8s_yaml('deploy/www.yaml')

# k8s_resource(
#     'www',
#     # port_forwards='9999:11345',
#     # port_forwards='9999:80',
#     # labels=['world']
# )

local_resource(
    'kompose convert',
    # cmd='kompose convert --build local --build-command "docker build -t registry.gitlab.com/timestep-ai/timestep/www ." --file docker-compose.yml --push-image --push-command "docker push registry.gitlab.com/timestep-ai/timestep/www" --push-image-registry registry.gitlab.com --out deploy/www.yaml --secrets-as-files --verbose',
    # cmd='rm -rf timestep-ai && kompose convert --build local --build-command "docker compose pull && docker compose build && helm package timestep-ai" --chart --file docker-compose.yml --push-image --push-command "docker compose push && helm push timestep-ai-0.0.1.tgz oci://registry.gitlab.com/timestep-ai/timestep" --push-image-registry registry.gitlab.com --out timestep-ai --secrets-as-files --verbose',
    # cmd='kompose convert --chart --file docker-compose.yml --out timestep-ai --secrets-as-files --verbose',
    # cmd='rm -rf timestep-ai && kompose convert --build local --build-command "docker compose pull && docker compose build && helm package timestep-ai" --chart --file docker-compose.yml --push-image --push-command "helm push timestep-ai-0.0.1.tgz oci://registry.gitlab.com/timestep-ai/timestep" --push-image-registry registry.gitlab.com --out timestep-ai --secrets-as-files --verbose',
    # cmd='kompose convert --build local --build-command "helm package timestep-ai" --chart --file docker-compose.yml --push-image --push-command "helm push timestep-ai-0.0.1.tgz oci://registry.gitlab.com/timestep-ai/timestep" --push-image-registry registry.gitlab.com --out timestep-ai --secrets-as-files --verbose',
    # cmd='rm -rf timestep-ai && kompose convert --chart --file docker-compose.yml --generate-network-policies --out timestep-ai --secrets-as-files --verbose',
    cmd='rm -rf timestep-ai && kompose convert --chart --file docker-compose.yml --out timestep-ai --secrets-as-files --verbose',
    # cmd="./scripts/kompose-convert.sh",
    deps=[
        '.env',
        # 'Caddyfile',
        'docker-compose.yml',
        # 'www',
    ],
    labels=['build'],
    # resource_deps=[
    #     'regctl image import www',
    # ]
)

watch_file('timestep-ai')

if os.path.exists('timestep-ai'):
    local_resource(
        'helm package',
        cmd='helm package timestep-ai --version $VERSION',
        deps=['timestep-ai'],
        labels=['build'],
        resource_deps=[
            'kompose convert',
        ]
    )

    # docker_build(
    #     'registry.gitlab.com/timestep-ai/timestep/caddy',
    #     context='./src/timestep/services/caddy',
    #     dockerfile='./src/timestep/services/caddy/Dockerfile',
    #     only=['.'],
    #     # live_update=[
    #     #     sync('./src/timestep/services/caddy/', '/etc/caddy/'),
    #     #     run(
    #     #         'caddy reload',
    #     #         trigger=['./src/timestep/services/caddy/Caddyfile']
    #     #     )
    #     # ]
    # )

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
        # tag='latest',
        tag=str(local(command='echo $VERSION')).strip(),
    )

    # docker_build(
    #     'registry.gitlab.com/timestep-ai/timestep/api',
    #     context='./src/timestep/services/api',
    #     dockerfile='./src/timestep/services/api/Dockerfile',
    #     only=['.'],
    #     live_update=[
    #         sync('./src/timestep/services/api/', '/app/api/'),
    #         run(
    #             'pip install -r /app/requirements.txt',
    #             trigger=['./src/timestep/services/api/requirements.txt']
    #         )
    #     ]
    # )

    # docker_build(
    #     'registry.gitlab.com/timestep-ai/timestep/web',
    #     context='src/timestep/services/web',
    #     dockerfile='src/timestep/services/web/Dockerfile',
    #     only=['.'],
    #     ignore=['./dist/'],
    #     live_update=[
    #         fall_back_on('./src/timestep/services/web/vite.config.js'),
    #         sync('./src/timestep/services/web/', '/app/'),
    #         run(
    #             'yarn install',
    #             trigger=['./src/timestep/services/web/package.json', './src/timestep/services/web/yarn.lock']
    #         )
    #     ]
    # )

    docker_build(
        'registry.gitlab.com/timestep-ai/timestep/www',
        build_args={
         'NODENV_VERSION': os.getenv('NODENV_VERSION'),
        },
        context='src/timestep/services/www',
        dockerfile='src/timestep/services/www/Dockerfile',
        entrypoint='quasar dev -m spa -p 9000',
        # entrypoint='quasar dev --hostname 127.0.0.1 -m spa -p 9000',
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
        # skips_local_docker=True,
    )

    # custom_build(
    #     'registry.gitlab.com/timestep-ai/timestep/www',
    #     command='docker build -t $EXPECTED_REF src/timestep/services/www',
    #     deps=['src/timestep/services/www'],
    #     disable_push=True,
    #     # entrypoint=['npm', 'run', 'dev'],
    #     # entrypoint=['npm', 'run', 'serve'],
    #     # entrypoint=['tail', '-f', '/dev/null'],
    #     ignore=['dist', 'src-capacitor', 'src-electron'],
    #     skips_local_docker=True,
    #     # tag='latest',
    #     tag=str(local(command='echo $VERSION')).strip(),
    # )

    k8s_yaml(local('helm template timestep-ai'))

# watch_file('timestep-ai')

    # k8s_resource(
    #     'caddy',
    #     # labels=['release'],
    #     links=['https://' + str(local(command='echo $PRIMARY_DOMAIN_NAME')).strip()],
    # )

    # k8s_resource(
    #     'api',
    #     port_forwards='5734:5000',
    #     # labels=['backend'],
    # )

    # k8s_resource(
    #     'dashboard',
    #     port_forwards='3030:3030',
    #     labels=['backend', 'frontend'],
    # )

    # k8s_resource(
    #     'prefect-server',
    #     port_forwards='4200:4200',
    #     # labels=['backend', 'frontend'],
    # )

    # k8s_resource(
    #     'web',
    #     port_forwards='5735:5173', # 5173 is the port Vite listens on in the container
    #     labels=['frontend'],
    # )

    # k8s_resource(
    #     'www',
    #     # port_forwards='5735:5173', # 5173 is the port Vite listens on in the container
    #     port_forwards='9200:9000',
    #     # labels=['frontend'],
    # )

# local_resource(
#     'docker build',
#     # cmd='docker build --tag registry.gitlab.com/timestep-ai/timestep/www .',
#     cmd='docker build --tag $EXPECTED_REF .',
#     deps=[
#         'Caddyfile',
#         'docker-compose.yml',
#         'www',
#     ],
#     labels=['build'],
# )

# custom_build(
#     # 'docker build',
#     'registry.gitlab.com/timestep-ai/timestep/www',
#     # cmd='docker build --tag registry.gitlab.com/timestep-ai/timestep/www .',
#     'docker build --tag $EXPECTED_REF .',
#     deps=[
#         'Caddyfile',
#         'Dockerfile',
#         'docker-compose.yml',
#         'www',
#     ],
#     # labels=['build'],
#     live_update=[
#         fall_back_on('./www/quasar.config.js'),
#         sync('./www/', '/home/base/www/'),
#         run(
#             cmd='cd /home/base/www/ && npm install && npm run build',
#             # trigger=['./www/package.json', './www/package-lock.json']
#         )
#     ]
# )

# local_resource(
#     'docker push',
#     cmd='docker push registry.gitlab.com/timestep-ai/timestep/www',
#     deps=[
#         'Caddyfile',
#         'docker-compose.yml',
#         'www',
#     ],
#     labels=['build'],
#     resource_deps=[
#         'docker build',
#     ]
# )

# local_resource(
#     'docker save www',
#     cmd='docker save registry.gitlab.com/timestep-ai/timestep/www > www.tar',
# )

# local_resource(
#     'regctl image import www',
#     cmd='./bin/regctl image import registry.gitlab.com/timestep-ai/timestep/www www.tar -v debug',
#     resource_deps=[
#         'docker save www',
#     ],
# )
