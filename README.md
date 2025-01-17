# Timestep

Timestep CLI - free, local-first, open-source AI

## Project Structure

```
src/timestep/
│
├── infra/                  # Infrastructure management
│   ├── cloud/              # Cloud instance management
│   │   └── cloud_instance_controller.py
│   │       - Manages cloud instances using Apache Libcloud
│   │
│   ├── k3s/                # K3s Kubernetes cluster management
│   │   └── k3s_cluster_controller.py
│   │       - Manages K3s Kubernetes clusters
│   │
│   └── sky/                # SkyPilot workload management
│       └── sky_workload_controller.py
│           - Manages computational workloads using SkyPilot
│
|── pipelines/             # Pipelines
|   ├── data_engineering/  # Data engineering pipeline
|   │   └── task.yaml
|   │       - SkyPilot task specification
|   ├── machine_learning/   # Machine learning pipeline
|   │   └── task.yaml
|   │       - SkyPilot task specification
|   ├── model_deployment/   # Model deployment pipeline
|   │   └── task.yaml
|   │       - SkyPilot task specification
|   └── model_monitoring/   # Model monitoring pipeline
|       └── task.yaml
|           - SkyPilot task specification
|
└── services/              # Services
    ├── backend/           # Backend service
    │   └── main.py
    │       - FastAPI backend service
    │
    └── frontend/          # Frontend service
        └── main.py
            - Flet frontend service
```

**Development Setup**:

```console
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
$ pipx install poetry==1.8.3
$ cp .env.example .env
$ direnv allow # See https://direnv.net/#getting-started
$ make
$ timestep up --dev
```

**Library Setup**:

```console
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
$ pipx install timestep
$ timestep up
```

**Usage**:

```console
$ timestep [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `up`: Start up the Timestep platform.

## `timestep up`

Start up the Timestep platform.

**Usage**:

```console
$ timestep up [OPTIONS]
```

**Options**:

* `--accept-defaults / --no-accept-defaults`: Accept defaults and skip prompts  [default: no-accept-defaults]
* `--allowed-image-ids TEXT`: Allowed image IDs to filter by  [default: ami-0e7c4f6b17a66658a]
* `--allowed-image-names TEXT`: Allowed image names to filter by  [default: 24.04 LTS, 24.04 (LTS) x64, Ubuntu 24.04 LTS]
* `--allowed-location-countries TEXT`: Allowed location countries to filter by
* `--allowed-location-ids TEXT`: Allowed location IDs to filter by
* `--allowed-location-names TEXT`: Allowed location names to filter by
* `--down / --no-down`: Down  [default: no-down]
* `--min-bandwidth INTEGER`: Minimum bandwidth in GB
* `--min-cpu INTEGER`: Minimum CPU count  [default: 2]
* `--min-disk INTEGER`: Minimum disk size in GB  [default: 10]
* `--min-ram INTEGER`: Minimum RAM in MB  [default: 4000]
* `--name TEXT`: Name  [default: timestep]
* `--providers TEXT`: Providers to filter by
* `--ssh-key TEXT`: Path to the SSH key  [default: ~/.ssh/id_ed25519]
* `--help`: Show this message and exit.
