import pathlib
from enum import StrEnum, auto

from pydantic import BaseSettings, Field, SecretStr

BASE_PATH = pathlib.Path.cwd()
CPUS: int = 4
DISK_SIZE_GB: int = 160
DIST_PATH: str = f"{BASE_PATH}/cdktf.out"
MEMORY_SIZE_GB: int = 8
DO_DROPLET_SIZE: str = f"s-{CPUS}vcpu-{MEMORY_SIZE_GB}gb"
MULTIPASS_INSTANCE_CPUS: int = CPUS
MULTIPASS_INSTANCE_DISK: str = f"{DISK_SIZE_GB}G"
MULTIPASS_INSTANCE_IMAGE: str = "22.04"
MULTIPASS_INSTANCE_MEMORY: str = f"{MEMORY_SIZE_GB}G"


class CloudInstanceProvider(StrEnum):
    DIGITALOCEAN = auto()
    MULTIPASS = auto()


class DomainNameRegistrarProvider(StrEnum):
    NAMECHEAP = auto()
    NONE = auto()


class Settings(BaseSettings):
    anthropic_api_key: SecretStr = Field(default=None)
    argo_cd_private_repo_access_token: SecretStr = Field()
    argo_cd_private_repo_username: str = Field()
    base_path: pathlib.Path = Field(default=BASE_PATH)
    cdktf_outdir: str = Field()
    ci_registry_image: str = Field()
    cloud_instance_name: str = Field()
    cloud_instance_provider: CloudInstanceProvider = Field()
    cloud_instance_user: str = Field()
    dist_path: str = Field(default=DIST_PATH)
    do_droplet_image: str = Field()
    do_droplet_region: str = Field()
    do_droplet_size: str = Field(default=DO_DROPLET_SIZE)
    do_token: SecretStr = Field()
    docker_registry_email: str = Field()
    docker_registry_password: SecretStr = Field()
    docker_registry_server: str = Field()
    docker_registry_username: str = Field()
    domain_name_registrar_provider: DomainNameRegistrarProvider = Field(
        default=DomainNameRegistrarProvider.NONE,
    )
    # hasura_graphql_admin_secret: SecretStr = Field()
    # hasura_graphql_jwt_secret_key: SecretStr = Field(min_length=32)
    hasura_in_cluster_is_enabled: bool = Field(default=False)
    hf_token: SecretStr = Field(default=None)
    ingress_controller_acme_ca: str = Field()
    ingress_controller_debug: str = Field()
    ingress_controller_email: str = Field()
    kube_prometheus_stack_is_enabled: bool = Field(default=False)
    kubeapps_is_enabled: bool = Field(default=False)
    kubeconfig: SecretStr = Field(default=None)
    kubecontext: str = Field()
    langsmith_api_key: SecretStr = Field(default=None)
    local_tls_cert_is_enabled: bool = Field()
    local_tls_crt: SecretStr = Field(default=None)
    local_tls_key: SecretStr = Field(default=None)
    minio_in_cluster_is_enabled: bool = Field(default=False)
    minio_root_user: str = Field()
    # minio_root_password: SecretStr = Field()
    multipass_instance_cpus: int = Field(default=MULTIPASS_INSTANCE_CPUS)
    multipass_instance_disk: str = Field(default=MULTIPASS_INSTANCE_DISK)
    multipass_instance_image: str = Field(default=MULTIPASS_INSTANCE_IMAGE)
    multipass_instance_memory: str = Field(default=MULTIPASS_INSTANCE_MEMORY)
    namecheap_api_key: SecretStr = Field(default=None)
    namecheap_api_user: str = Field(default=None)
    namecheap_user_name: str = Field(default=None)
    nhost_in_cluster_is_enabled: bool = Field(default=False)
    openai_api_key: SecretStr = Field(default=None)
    open_gpts_in_cluster_is_enabled: bool = Field(default=True)
    # pgpool_admin_password: SecretStr = Field()
    postgresql_in_cluster_is_enabled: bool = Field(default=False)
    # postgresql_password: SecretStr = Field()
    # postgres_database = "postgres"
    postgres_database: str = Field(default="postgres")
    # postgres_hostname = "postgresql-postgresql-ha-pgpool.default.svc.cluster.local"
    postgres_hostname: str = Field(default="postgresql-postgresql-ha-pgpool.default.svc.cluster.local")
    # postgres_password = config.postgresql_password.get_secret_value()
    postgres_password: SecretStr = Field(default="postgres")
    # postgres_username = "postgres"
    postgres_username: str = Field(default="postgres")
    postgres_port: str = Field(default="5432")
    # postgresql_repmgr_password: SecretStr = Field()
    prefect_in_cluster_is_enabled: bool = Field(default=False)
    prefect_server_version: str = Field()
    primary_domain_name: str = Field()
    python_target_version: str = Field()
    ray_version: str = Field()
    sealed_secrets_is_enabled: bool = Field(default=False)
    stalwart_is_enabled: bool = Field(default=False)
    smtp_password: SecretStr = Field()
    smtp_sender: str = Field()
    smtp_user: str = Field()
    ssh_private_key: SecretStr = Field()
    ssh_public_key: SecretStr = Field()
    supabase_access_token: SecretStr = Field()
    tavily_api_key: SecretStr = Field(default=None)
    tf_api_token: SecretStr = Field()
    tf_http_address: str = Field()
    tf_username: str = Field()
    timestep_ai_is_enabled: bool = Field(default=True)
    version: str = Field()

    class Config:
        env_file = (".dot.env", ".env")
        env_file_encoding = "utf-8"
        secrets_dir = "./secrets"
