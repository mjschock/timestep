# Timestep AI

[![Agent protocol](https://github.com/mjschock/timestep/actions/workflows/deploy.yml/badge.svg)](https://agentprotocol.ai/compliance)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg)](https://www.digitalocean.com/?refcode=2184d1107783&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

## Requirements

- [arkade](https://github.com/alexellis/arkade#getting-arkade)
- [direnv](https://direnv.net/)
- [Multipass](https://multipass.run/install)

## Setup

### Local Secrets (GitHub Actions Secrets)

```bash
secrets/argo_cd_private_repo_access_token (ARGO_CD_PRIVATE_REPO_ACCESS_TOKEN)
secrets/do_token (DO_TOKEN)
secrets/docker_registry_password (DOCKER_REGISTRY_PASSWORD)
secrets/hasura_graphql_admin_secret (HASURA_GRAPHQL_ADMIN_SECRET)
secrets/hasura_graphql_jwt_secret_key (HASURA_GRAPHQL_JWT_SECRET_KEY)
secrets/minio_root_password (MINIO_ROOT_PASSWORD)
secrets/pgpool_admin_password (PGPOOL_ADMIN_PASSWORD)
secrets/postgresql_password (POSTGRESQL_PASSWORD)
secrets/postgresql_repmgr_password (POSTGRESQL_REPMGR_PASSWORD)
secrets/smtp_password (SMTP_PASSWORD)
secrets/ssh_private_key (SSH_PRIVATE_KEY)
secrets/ssh_public_key (SSH_PUBLIC_KEY)
secrets/tf_api_token (TF_API_TOKEN)
```

### Local / GitHub Actions Variables

Copy `.env.example` to `.env` and ajust the values as needed. The following variables are also required:

```bash
ARGO_CD_PRIVATE_REPO_USERNAME
CI_REGISTRY_IMAGE
CLOUD_INSTANCE_NAME
DOCKER_REGISTRY_EMAIL
DOCKER_REGISTRY_SERVER
DOCKER_REGISTRY_USERNAME
INGRESS_CONTROLLER_EMAIL
SMTP_SENDER
SMTP_USER
TF_HTTP_ADDRESS
TF_USERNAME
```

## Setup

```bash
ark get hostctl mkcert tilt
direnv allow
tilt up
```

```bash
make hosts # In a separate terminal
```

## Usage

```bash
open https://${PRIMARY_DOMAIN_NAME}
```
