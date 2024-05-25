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

## Configuration

### Variables

For local configuration, copy `.env.sample` to `.env` and adjust the values as needed. For remote configuration, create a GitHub repository variable for each variable in `.env`. For example:

| Variable | Local Value (empty if default) | Remote Value (empty if default) |
| --- | --- | --- |
| ARGO_CD_PRIVATE_REPO_USERNAME | mjschock | mjschock |
| CI_REGISTRY_IMAGE | registry.gitlab.com/timestep-ai/timestep | registry.gitlab.com/timestep-ai/timestep |
| CLOUD_INSTANCE_NAME | timestep-ai | timestep-ai |
| CLOUD_INSTANCE_PROVIDER | multipass | digitalocean |
| DOCKER_REGISTRY_EMAIL | m@mjschock.com | m@mjschock.com |
| DOCKER_REGISTRY_SERVER | registry.gitlab.com | registry.gitlab.com |
| DOCKER_REGISTRY_USERNAME | m.schock | m.schock |
| INGRESS_CONTROLLER_ACME_CA | https://acme-staging-v02.api.letsencrypt.org/directory | |
| INGRESS_CONTROLLER_DEBUG | true | |
| INGRESS_CONTROLLER_EMAIL | agent@timestep.ai | agent@timestep.ai |
| KUBECONTEXT | timestep.local | timestep.ai |
| LOCAL_TLS_CERT_IS_ENABLED | true | |
| NAMECHEAP_API_USER | | mschock |
| NAMECHEAP_USER_NAME | | mschock |
| OPEN_GPTS_IN_CLUSTER_IS_ENABLED | true | |
| POSTGRES_DATABASE | | |
| POSTGRES_HOSTNAME | aws-0-us-west-1.pooler.supabase.com | aws-0-us-west-1.pooler.supabase.com |
| POSTGRES_PORT | | |
| POSTGRES_USERNAME | postgres.iuoxbzzwmbwctbhztahw | postgres.iuoxbzzwmbwctbhztahw |
| PRIMARY_DOMAIN_NAME | timestep.local | timestep.ai |
| SMTP_SENDER | agent@timestep.ai.test-google-a.com | agent@timestep.ai.test-google-a.com |
| SMTP_USER | agent@timestep.ai | agent@timestep.ai |
| TF_HTTP_ADDRESS | https://gitlab.com/api/v4/projects/47704767/terraform/state | https://gitlab.com/api/v4/projects/47704767/terraform/state |
| TF_USERNAME | m.schock | m.schock |

### Secrets

For local configuration, create a file in the `secrets` directory for each secret below, using the lowercased secret name as the filename.
For remote configuration, create a GitHub repository secret for each secret below. For example, if the secret is `OPENAI_API_KEY`, the local secret file would be `secrets/openai_api_key` and the remote repository secret would be `OPENAI_API_KEY`. The mapping is as follows:

| Local File Secret (empty if unset) | Remote Repository Secret |
| --- | --- |
| `secrets/argo_cd_private_repo_access_token` | ARGO_CD_PRIVATE_REPO_ACCESS_TOKEN |
| `secrets/do_token` | DO_TOKEN |
| `secrets/docker_registry_password` | DOCKER_REGISTRY_PASSWORD |
| | NAMECHEAP_API_KEY |
| `secrets/openai_api_key` | OPENAI_API_KEY |
| `secrets/postgres_password` | POSTGRESQL_PASSWORD |
| `secrets/smtp_password` | SMTP_PASSWORD |
| `secrets/ssh_private_key` | SSH_PRIVATE_KEY |
| `secrets/ssh_public_key` | SSH_PUBLIC_KEY |
| `secrets/tf_api_token` | TF_API_TOKEN |

## Setup

```bash
ark get hostctl mkcert tilt
direnv allow
tilt up
```

```bash
make local-tls-cert # If LOCAL_TLS_CERT_IS_ENABLED is true and trigger caddy update
```

```bash
make hosts # In a separate terminal
```

## Usage

```bash
open https://${PRIMARY_DOMAIN_NAME}
```
