load('ext://dotenv', 'dotenv')
dotenv()

local_resource('install-arkade',
    cmd='which ark > /dev/null || echo "Install arkade"',
    labels=['requirements'],
    links=['https://github.com/alexellis/arkade#getting-arkade'],
)

local_resource('install-cdktf',
    cmd='which cdktf > /dev/null || echo "Install CDKTF"',
    labels=['requirements'],
    links=['https://developer.hashicorp.com/terraform/tutorials/cdktf/cdktf-install#install-cdktf'],
)

local_resource('install-hostctl',
    cmd='ark get hostctl',
    labels=['requirements'],
    links=[
        'https://github.com/guumaster/hostctl',
        'https://guumaster.github.io/hostctl',
    ],
    resource_deps=['install-arkade'],
)

local_resource('install-k3sup',
    cmd='which k3sup > /dev/null || echo "Install k3sup"', # arkade get k3sup
    labels=['requirements'],
    links=['https://github.com/alexellis/k3sup#download-k3sup-tldr'],
    resource_deps=['install-arkade'],
)

local_resource('install-multipass',
    cmd='which multipasses > /dev/null || echo "Install Multipass"',
    labels=['requirements'],
    links=['https://multipass.run/install'],
)

local_resource('install-terraform',
    cmd='which terraform > /dev/null || echo "Install Terraform"', # arkade get terraform
    labels=['requirements'],
    links=['https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform'],
    resource_deps=['install-arkade'],
)

local_resource('cdktf-deploy',
    auto_init=False,
    cmd='cdktf deploy --auto-approve --outputs-file dist/deploy/infra/outputs.json',
    labels=['cdktf'],
    resource_deps=['install-cdktf', 'install-multipass', 'install-terraform'],
    trigger_mode=TRIGGER_MODE_MANUAL,
)

local_resource('k3sup-install',
    auto_init=False,
    cmd='PRIVATE_SSH_KEY_PATH=./.ssh/id_rsa ./src/lib/tools/k3sup-install.sh',
    deps=['dist/deploy/infra/outputs.json', 'src/lib/tools/k3sup-install.sh'],
    labels=['k3sup'],
    resource_deps=['cdktf-deploy', 'install-k3sup'],
    trigger_mode=TRIGGER_MODE_AUTO,
)

local_resource('kompose-convert',
    auto_init=True,
    cmd='docker run --rm --name kompose -v $PWD:/src femtopixel/kompose convert --chart --out /src/dist/deploy/k8s/charts/timestep --secrets-as-files --verbose --file docker-compose.yaml',
    deps=['docker-compose.yaml'],
    labels=['kompose'],
    trigger_mode=TRIGGER_MODE_AUTO,
)

allow_k8s_contexts('timestep-k3s-cluster')
local('kubectl config use-context timestep-k3s-cluster')

# load('ext://helm_resource', 'helm_resource', 'helm_repo')
# helm_repo('caddy-ingress-controller', 'https://caddyserver.github.io/ingress/')
# helm_resource(
#     name='mycaddy',
#     chart='caddy-ingress-controller',
#     namespace='caddy-system',
# )

k8s_yaml(helm('src/docs/reference/caddyserver/ingress/charts/caddy-ingress-controller', name='caddy-ingress-controller', values='values-dev.yaml'))
k8s_yaml(listdir('src/docs/reference/caddyserver/ingress/kubernetes/sample'))

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
load('ext://git_resource', 'git_checkout')


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
