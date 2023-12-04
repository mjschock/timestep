import pathlib
from enum import StrEnum, auto

from pydantic import BaseSettings, Field, SecretStr

BASE_PATH = pathlib.Path.cwd()
CPUS: int = 2
DISK_SIZE_GB: int = 80
DIST_PATH: str = f"{BASE_PATH}/cdktf.out"
MEMORY_SIZE_GB: int = 4
DO_DROPLET_IMAGE: str = "ubuntu-22-04-x64"
DO_DROPLET_REGION: str = "sfo3"
DO_DROPLET_SIZE: str = f"s-{CPUS}vcpu-{MEMORY_SIZE_GB}gb"
MULTIPASS_INSTANCE_CPUS: int = CPUS
MULTIPASS_INSTANCE_DISK: str = f"{DISK_SIZE_GB}G"
MULTIPASS_INSTANCE_IMAGE: str = "22.04"
MULTIPASS_INSTANCE_MEMORY: str = f"{MEMORY_SIZE_GB}G"


class CloudInstanceProvider(StrEnum):
    DIGITALOCEAN: str = auto()
    MULTIPASS: str = auto()


class DomainNameRegistrarProvider(StrEnum):
    NAMECHEAP: str = auto()
    NONE: str = auto()


class Settings(BaseSettings):
    base_path: pathlib.Path = Field(default=BASE_PATH, env="BASE_PATH")
    cdktf_outdir: str = Field(env="CDKTF_OUTDIR")
    cloud_instance_name: str = Field(env="CLOUD_INSTANCE_NAME")
    cloud_instance_provider: str = Field(
        default=CloudInstanceProvider.MULTIPASS, env="CLOUD_INSTANCE_PROVIDER"
    )
    cloud_instance_user: str = Field(env="CLOUD_INSTANCE_USER")
    dist_path: str = Field(default=DIST_PATH, env="DIST_PATH")
    do_droplet_image: str = Field(default=DO_DROPLET_IMAGE, env="DO_DROPLET_IMAGE")
    do_droplet_region: str = Field(default=DO_DROPLET_REGION, env="DO_DROPLET_REGION")
    do_droplet_size: str = Field(default=DO_DROPLET_SIZE, env="DO_DROPLET_SIZE")
    do_token: SecretStr = Field(env="DO_TOKEN")
    docker_registry_email: str = Field(env="DOCKER_REGISTRY_EMAIL")
    docker_registry_password: SecretStr = Field(env="DOCKER_REGISTRY_PASSWORD")
    docker_registry_server: str = Field(env="DOCKER_REGISTRY_SERVER")
    docker_registry_username: str = Field(env="DOCKER_REGISTRY_USERNAME")
    domain_name_registrar_provider: str = Field(
        default=DomainNameRegistrarProvider.NONE, env="DOMAIN_NAME_REGISTRAR_PROVIDER"
    )
    github_api_token: SecretStr = Field(
        default=f"{BASE_PATH}/secrets/github_api_token", env="GITHUB_API_TOKEN"
    )
    hasura_graphql_admin_secret: SecretStr = Field(
        default=f"{BASE_PATH}/secrets/hasura_graphql_admin_secret",
        env="HASURA_GRAPHQL_ADMIN_SECRET",
    )
    hasura_graphql_jwt_secret_key: SecretStr = Field(
        default=f"{BASE_PATH}/secrets/hasura_graphql_jwt_secret_key",
        env="HASURA_GRAPHQL_JWT_SECRET_KEY",
    )
    htpasswd: SecretStr = Field(env="HTPASSWD")
    ingress_controller_acme_ca: str = Field(
        default="https://acme-staging-v02.api.letsencrypt.org/directory",
        # default="https://acme-v02.api.letsencrypt.org/directory",
        env="INGRESS_CONTROLLER_ACME_CA",
    )
    ingress_controller_debug: str = Field(
        default="true",
        env="INGRESS_CONTROLLER_DEBUG",
    )
    ingress_controller_email: str = Field(env="INGRESS_CONTROLLER_EMAIL")
    kubeapps_is_enabled: bool = Field(default=False, env="KUBEAPPS_IS_ENABLED")
    kubecontext: str = Field(env="KUBECONTEXT")
    local_tls_cert_is_enabled: bool = Field(
        default=False, env="LOCAL_TLS_CERT_IS_ENABLED"
    )
    local_tls_crt: SecretStr = Field(
        default=f"{BASE_PATH}/secrets/local_tls_crt",
        env="LOCAL_TLS_CRT",
    )
    local_tls_key: SecretStr = Field(
        default=f"{BASE_PATH}/secrets/local_tls_key",
        env="LOCAL_TLS_KEY",
    )
    minio_root_user: str = Field(env="MINIO_ROOT_USER")
    minio_root_password: SecretStr = Field(
        default=f"{BASE_PATH}/secrets/minio_root_password", env="MINIO_ROOT_PASSWORD"
    )
    multipass_instance_cpus: int = Field(
        default=MULTIPASS_INSTANCE_CPUS, env="MULTIPASS_INSTANCE_CPUS"
    )
    multipass_instance_disk: str = Field(
        default=MULTIPASS_INSTANCE_DISK, env="MULTIPASS_INSTANCE_DISK"
    )
    multipass_instance_image: str = Field(
        default=MULTIPASS_INSTANCE_IMAGE, env="MULTIPASS_INSTANCE_IMAGE"
    )
    multipass_instance_memory: str = Field(
        default=MULTIPASS_INSTANCE_MEMORY, env="MULTIPASS_INSTANCE_MEMORY"
    )
    namecheap_api_key: SecretStr = Field(default=None, env="NAMECHEAP_API_KEY")
    namecheap_api_user: str = Field(default=None, env="NAMECHEAP_API_USER")
    namecheap_user_name: str = Field(default=None, env="NAMECHEAP_USER_NAME")
    pgpool_admin_password: SecretStr = Field(
        default=f"{BASE_PATH}/secrets/pgpool_admin_password",
        env="PGPOOL_ADMIN_PASSWORD",
    )
    postgresql_password: SecretStr = Field(
        default=f"{BASE_PATH}/secrets/postgresql_password", env="POSTGRESQL_PASSWORD"
    )
    postgresql_repmgr_password: SecretStr = Field(
        default=f"{BASE_PATH}/secrets/postgresql_repmgr_password",
        env="POSTGRESQL_REPMGR_PASSWORD",
    )
    prefect_server_version: str = Field(env="PREFECT_SERVER_VERSION")
    primary_domain_name: str = Field(env="PRIMARY_DOMAIN_NAME")
    sealed_secrets_is_enabled: bool = Field(
        default=False, env="SEALED_SECRETS_IS_ENABLED"
    )
    smtp_password: SecretStr = Field(
        default=f"{BASE_PATH}/secrets/smtp_password",
        env="SMTP_PASSWORD",
    )
    smtp_sender: str = Field(env="SMTP_SENDER")
    ssh_private_key: SecretStr = Field(env="SSH_PRIVATE_KEY")
    ssh_private_key_path: str = Field(
        default=f"{BASE_PATH}/secrets/ssh_private_key", env="SSH_PRIVATE_KEY_PATH"
    )
    ssh_public_key: str = Field(env="SSH_PUBLIC_KEY")
    tf_api_token: SecretStr = Field(default=None, env="TF_API_TOKEN")
    tf_http_address: str = Field(default=None, env="TF_HTTP_ADDRESS")
    tf_username: str = Field(default=None, env="TF_USERNAME")
    version: str = Field(env="VERSION")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        secrets_dir = "./secrets"
