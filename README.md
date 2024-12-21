# Timestep AI

Timestep AI CLI - free, local-first, open-source AI

## Project Structure

```
src/timestep/
│
├── infra/                  # Infrastructure management
│   ├── cloud_management/   # Cloud instance operations
│   │   └── cloud_instance_controller.py
│   │       - Manages cloud instances using Apache Libcloud
│   │
│   ├── cluster_management/ # Kubernetes cluster management
│   │   └── k3s_cluster_controller.py
│   │       - Manages K3s Kubernetes clusters
│   │
│   └── workload_management/ # Workload orchestration
│       └── sky_workload_controller.py
│           - Manages computational workloads using SkyPilot
│
└── pipelines/              # Data and ML pipeline components
    ├── data_engineering/   # Data preparation stage
    │   └── task.yaml
    │
    ├── machine_learning/   # Model development stage
    │   └── task.yaml
    │
    └── model_deployment/   # Model deployment and monitoring
        └── task.yaml
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

* `up`: Start up the Timestep AI platform.

## `timestep up`

Start up the Timestep AI platform.

**Usage**:

```console
$ timestep up [OPTIONS]
```

**Options**:

* `--allowed-image-ids TEXT`: Allowed image IDs to filter by  [default: ami-0e7c4f6b17a66658a]
* `--allowed-image-names TEXT`: Allowed image names to filter by  [default: 24.04 (LTS) x64, Ubuntu 24.04 LTS]
* `--allowed-location-countries TEXT`: Allowed location countries to filter by
* `--allowed-location-ids TEXT`: Allowed location IDs to filter by
* `--allowed-location-names TEXT`: Allowed location names to filter by
* `--clean / --no-clean`: Clean up  [default: no-clean]
* `--dev / --no-dev`: Development mode  [default: no-dev]
* `--host TEXT`: Host  [default: 0.0.0.0]
* `--min-bandwidth INTEGER`: Minimum bandwidth in GB
* `--min-disk INTEGER`: Minimum disk size in GB  [default: 10]
* `--min-ram INTEGER`: Minimum RAM in MB  [default: 2000]
* `--name TEXT`: Name  [default: timestep]
* `--port INTEGER`: Port  [default: 8000]
* `--ssh-key TEXT`: Path to the SSH key  [default: ~/.ssh/id_ed25519]
* `--help`: Show this message and exit.
