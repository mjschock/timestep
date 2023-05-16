load('ext://dotenv', 'dotenv')
load('ext://git_resource', 'git_checkout')

dotenv()


# Organize logic into functions
#   Tiltfiles are written in Starlark, a Python-inspired language, so
#   you can use functions, conditionals, loops, and more.
#
#   More info: https://docs.tilt.dev/tiltfile_concepts.html
#
def src_lib():
    # Tilt provides many useful portable built-ins
    # https://docs.tilt.dev/api.html#modules.os.path.exists
    if os.path.exists('src/lib/Tiltfile'):
        # It's possible to load other Tiltfiles to further organize
        # your logic in large projects
        # https://docs.tilt.dev/multiple_repos.html
        load_dynamic('src/lib/Tiltfile')

    watch_file('src/lib/Tiltfile')
    # git_checkout('https://github.com/tilt-dev/tilt-avatars.git',
    #              checkout_dir='src/docs/reference/tilt-dev/tilt-avatars')


# Edit your Tiltfile without restarting Tilt
#   While running `tilt up`, Tilt watches the Tiltfile on disk and
#   automatically re-evaluates it on change.
#
#   To see it in action, try uncommenting the following line with
#   Tilt running.
src_lib()

local_resource('cdktf-deploy',
    auto_init=True,
    cmd='cdktf deploy --auto-approve --outputs-file dist/deploy/infra/outputs.json',
    labels=['deploy'],
    resource_deps=['cdktf', 'multipass', 'terraform'],
    trigger_mode=TRIGGER_MODE_MANUAL,
)

local_resource('k3sup-install',
    auto_init=False,
    cmd='PRIVATE_SSH_KEY_PATH=./.ssh/id_rsa ./src/lib/tools/k3sup-install.sh',
    deps=['dist/deploy/infra/outputs.json', 'src/lib/tools/k3sup-install.sh'],
    labels=['deploy'],
    resource_deps=['cdktf-deploy', 'k3sup'],
    trigger_mode=TRIGGER_MODE_AUTO,
)

local_resource('clean',
    auto_init=False,
    cmd='rm -rf dist/deploy/k8s/charts/timestep',
    deps=['docker-compose.yaml'],
    labels=['clean'],
    trigger_mode=TRIGGER_MODE_MANUAL,
)

local_resource('kompose-convert',
    auto_init=True,
    cmd='docker run --rm --name kompose -v $PWD:/src femtopixel/kompose convert --chart --out /src/dist/deploy/k8s/charts/timestep --secrets-as-files --verbose --file docker-compose.yaml',
    deps=['docker-compose.yaml'],
    labels=['build'],
    trigger_mode=TRIGGER_MODE_AUTO,
)

allow_k8s_contexts('timestep-k3s-cluster')
# local('kubectl config use-context timestep-k3s-cluster')

if k8s_context() == 'timestep-k3s-cluster':
    # local_resource('k3s-deploy',
    #     auto_init=True,
    #     cmd='k3s kubectl apply -f dist/deploy/k8s/manifests',
    #     deps=['dist/deploy/k8s/manifests'],
    #     labels=['deploy'],
    #     resource_deps=['k3sup-install'],
    #     trigger_mode=TRIGGER_MODE_AUTO,
    # )

    k8s_yaml(listdir('dist/deploy/k8s/manifests'))
    k8s_yaml(helm('src/docs/reference/caddyserver/ingress/charts/caddy-ingress-controller', name='caddy-ingress-controller', namespace='caddy-system', values='values-dev.yaml'))
    # k8s_yaml(listdir('src/docs/reference/caddyserver/ingress/kubernetes/sample'))
    k8s_yaml(helm('dist/deploy/k8s/charts/timestep', name='timestep', namespace='default'))

    local('src/lib/tools/hostsctl-add.sh') # TODO: pass in the IP address

# k8s_resource("caddy-ingress-controller",
#     # port_forwards=['timestep.local:80:80', 'timestep.local:443:443'],
#     port_forwards=['0.0.0.0:80:80', '0.0.0.0:443:443'],
#     trigger_mode=TRIGGER_MODE_AUTO,
# )

# Welcome to Tilt!
#   To get you started as quickly as possible, we have created a
#   starter Tiltfile for you.
#
#   Uncomment, modify, and delete any commands as needed for your
#   project's configuration.


# Output diagnostic messages
#   You can print log messages, warnings, and fatal errors, which will
#   appear in the (Tiltfile) resource in the web UI. Tiltfiles support
#   multiline strings and common string operations such as formatting.
#
#   More info: https://docs.tilt.dev/api.html#api.warn
# print("""
# -----------------------------------------------------------------
# ✨ Hello Tilt! This appears in the (Tiltfile) pane whenever Tilt
#    evaluates this file.
# -----------------------------------------------------------------
# """.strip())
# warn('ℹ️ Open {tiltfile_path} in your favorite editor to get started.'.format(
#     tiltfile_path=config.main_path))


# Build Docker image
#   Tilt will automatically associate image builds with the resource(s)
#   that reference them (e.g. via Kubernetes or Docker Compose YAML).
#
#   More info: https://docs.tilt.dev/api.html#api.docker_build
#
# docker_build('registry.example.com/my-image',
#              context='.',
#              # (Optional) Use a custom Dockerfile path
#              dockerfile='./deploy/app.dockerfile',
#              # (Optional) Filter the paths used in the build
#              only=['./app'],
#              # (Recommended) Updating a running container in-place
#              # https://docs.tilt.dev/live_update_reference.html
#              live_update=[
#                 # Sync files from host to container
#                 sync('./app', '/src/'),
#                 # Execute commands inside the container when certain
#                 # paths change
#                 run('/src/codegen.sh', trigger=['./app/api'])
#              ]
# )


# Apply Kubernetes manifests
#   Tilt will build & push any necessary images, re-deploying your
#   resources as they change.
#
#   More info: https://docs.tilt.dev/api.html#api.k8s_yaml
#
# k8s_yaml(['k8s/deployment.yaml', 'k8s/service.yaml'])


# Customize a Kubernetes resource
#   By default, Kubernetes resource names are automatically assigned
#   based on objects in the YAML manifests, e.g. Deployment name.
#
#   Tilt strives for sane defaults, so calling k8s_resource is
#   optional, and you only need to pass the arguments you want to
#   override.
#
#   More info: https://docs.tilt.dev/api.html#api.k8s_resource
#
# k8s_resource('my-deployment',
#              # map one or more local ports to ports on your Pod
#              port_forwards=['5000:8080'],
#              # change whether the resource is started by default
#              auto_init=False,
#              # control whether the resource automatically updates
#              trigger_mode=TRIGGER_MODE_MANUAL
# )


# Run local commands
#   Local commands can be helpful for one-time tasks like installing
#   project prerequisites. They can also manage long-lived processes
#   for non-containerized services or dependencies.
#
#   More info: https://docs.tilt.dev/local_resource.html
#
# local_resource('install-helm',
#                cmd='which helm > /dev/null || brew install helm',
#                # `cmd_bat`, when present, is used instead of `cmd` on Windows.
#                cmd_bat=[
#                    'powershell.exe',
#                    '-Noninteractive',
#                    '-Command',
#                    '& {if (!(Get-Command helm -ErrorAction SilentlyContinue)) {scoop install helm}}'
#                ]
# )


# Extensions are open-source, pre-packaged functions that extend Tilt
#
#   More info: https://github.com/tilt-dev/tilt-extensions
#
# load('ext://git_resource', 'git_checkout')


# Organize logic into functions
#   Tiltfiles are written in Starlark, a Python-inspired language, so
#   you can use functions, conditionals, loops, and more.
#
#   More info: https://docs.tilt.dev/tiltfile_concepts.html
#
def tilt_demo():
    # Tilt provides many useful portable built-ins
    # https://docs.tilt.dev/api.html#modules.os.path.exists
    if os.path.exists('src/docs/reference/tilt-dev/tilt-avatars/Tiltfile'):
        # It's possible to load other Tiltfiles to further organize
        # your logic in large projects
        # https://docs.tilt.dev/multiple_repos.html
        load_dynamic('src/docs/reference/tilt-dev/tilt-avatars/Tiltfile')

    watch_file('src/docs/reference/tilt-dev/tilt-avatars/Tiltfile')
    git_checkout('https://github.com/tilt-dev/tilt-avatars.git',
                 checkout_dir='src/docs/reference/tilt-dev/tilt-avatars')


# Edit your Tiltfile without restarting Tilt
#   While running `tilt up`, Tilt watches the Tiltfile on disk and
#   automatically re-evaluates it on change.
#
#   To see it in action, try uncommenting the following line with
#   Tilt running.
# tilt_demo()
