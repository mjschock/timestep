version_settings(constraint='>=0.22.2')

local_resource(
    'pulumi',
    cmd='pulumi stack select local && pulumi up --yes',
    deps=['__main__.py'],
)

docker_build(
    'mschock/reflex-app',
    build_args={
        "API_URL": "https://timestep.local",
        "DEPLOY_URL": "http://0.0.0.0:3000",
    },
    container_args=[
        "/home/ubuntu/app/docker-entrypoint.sh",
        "reflex",
        "run",
        "--loglevel",
        "debug",
    ],
    context='.',
    dockerfile='Dockerfile',
    live_update=[
        sync('./Caddyfile', '/home/ubuntu/app/Caddyfile'),
        sync('./timestep/', '/home/ubuntu/app/timestep/'),
        # run(
        #     'pip install -r /app/requirements.txt',
        #     trigger=['./api/requirements.txt']
        # )
    ]
)

docker_build(
    'mschock/webserver',
    build_args={
        "API_URL": "https://timestep.local",
        "DEPLOY_URL": "http://0.0.0.0:3000",
    },
    context='.',
    dockerfile='Dockerfile',
    live_update=[
        sync('./Caddyfile', '/home/ubuntu/app/Caddyfile'),
        sync('./timestep/', '/home/ubuntu/app/timestep/'),
        run(
        #     'pip install -r /app/requirements.txt',
        #     trigger=['./api/requirements.txt']
            'caddy reload --config Caddyfile --adapter caddyfile',
            trigger=['./Caddyfile'],
        )
    ]
)

allow_k8s_contexts('timestep.local')

k8s_yaml(
    local(
        'kubectl --kubeconfig kubeconfig get deployment/app -o yaml'
    )
)

k8s_yaml(
    local(
        'kubectl --kubeconfig kubeconfig get deployment/webserver -o yaml'
    )
)

# k8s_custom_deploy(
#   "app",
#   apply_cmd="""
#     kubectl --kubeconfig kubeconfig -v=0 set image deployment/app *=$TILT_IMAGE_0 > /dev/null && \
#       kubectl --kubeconfig kubeconfig get deployment/app -o yaml
#   """,
#   delete_cmd="echo App managed outside of Tilt",
# #   delete_cmd="""
# #     kubectl --kubeconfig kubeconfig -v=0 set image deployment/app *=mschock/reflex-app > /dev/null && \
# #       kubectl --kubeconfig kubeconfig get deployment/app -o yaml
# #   """,
#   deps=[
#     "Dockerfile"
#   ],
#   image_deps=["mschock/reflex-app"]
# )

# k8s_custom_deploy(
#   "webserver",
#   apply_cmd="""
#     kubectl --kubeconfig kubeconfig -v=0 set image deployment/webserver *=$TILT_IMAGE_0 > /dev/null && \
#       kubectl --kubeconfig kubeconfig get deployment/webserver -o yaml
#   """,
#   delete_cmd="echo Webserver managed outside of Tilt",
#   deps=[
#     "Dockerfile"
#   ],
#   image_deps=["mschock/webserver"]
# )
