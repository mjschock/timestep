import pathlib
from enum import StrEnum, auto
from typing import Optional

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings

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
    cdktf_cli_version: str = Field()
    cdktf_lib_version: str = Field()
    cdktf_log_level: str = Field()
    cdktf_output: str = Field()
    ci_registry_image: str = Field()
    cloud_instance_name: str = Field()
    cloud_instance_provider: CloudInstanceProvider = Field()
    cloud_instance_user: str = Field()
    dist_path: str = Field(default=DIST_PATH)
    do_droplet_image: str = Field()
    do_droplet_region: str = Field()
    do_droplet_size: str = Field(default=DO_DROPLET_SIZE)
    do_token: Optional[SecretStr] = Field(default=None)
    docker_registry_email: str = Field()
    docker_registry_password: SecretStr = Field()
    docker_registry_server: str = Field()
    docker_registry_username: str = Field()
    domain_name_registrar_provider: DomainNameRegistrarProvider = Field(
        default=DomainNameRegistrarProvider.NONE,
    )
    goenv_version: str = Field()
    hf_token: Optional[SecretStr] = Field(default=None)
    ingress_controller_acme_ca: str = Field()
    ingress_controller_debug: str = Field()
    ingress_controller_email: str = Field()
    kubeconfig: SecretStr = Field(default=None)
    kubecontext: str = Field()
    langchain_api_key: Optional[SecretStr] = Field(default=None)
    litellm_proxy_is_enabled: bool = Field(default=True)
    litellm_master_key: SecretStr = Field()
    local_tls_cert_is_enabled: bool = Field()
    local_tls_crt: Optional[SecretStr] = Field(default=None)
    local_tls_key: Optional[SecretStr] = Field(default=None)
    # marvin_azure_openai_api_key: Optional[SecretStr] = Field(default=None)
    # marvin_azure_openai_endpoint: Optional[str] = Field(default=None)
    # marvin_azure_openai_api_version: Optional[str] = Field(default=None)
    # marvin_chat_completions_model: Optional[str] = Field(default=None)
    # marvin_provider: str = Field()
    multipass_instance_cpus: int = Field(default=MULTIPASS_INSTANCE_CPUS)
    multipass_instance_disk: str = Field(default=MULTIPASS_INSTANCE_DISK)
    multipass_instance_image: str = Field(default=MULTIPASS_INSTANCE_IMAGE)
    multipass_instance_memory: str = Field(default=MULTIPASS_INSTANCE_MEMORY)
    namecheap_api_key: Optional[SecretStr] = Field(default=None)
    namecheap_api_user: Optional[str] = Field(default=None)
    namecheap_user_name: Optional[str] = Field(default=None)
    nodenv_version: str = Field()
    ollama_in_cluster_is_enabled: bool = Field(default=True)
    openai_api_key: SecretStr = Field(default=None)
    open_gpts_assistant_id: str = Field()
    open_gpts_in_cluster_is_enabled: bool = Field(default=True)
    open_gpts_user_id: str = Field()
    open_gpts_thread_id: str = Field()
    paperspace_api_key: Optional[SecretStr] = Field(default=None)
    poetry_virtualenvs_create: bool = Field()
    poetry_virtualenvs_in_project: bool = Field()
    postgres_database: str = Field(default="postgres")
    postgres_hostname: str = Field()
    postgres_password: SecretStr = Field(default="postgres")
    postgres_username: str = Field(default="postgres")
    postgres_port: str = Field(default="5432")
    prefect_api_key: Optional[SecretStr] = Field(default=None)
    prefect_api_url: str = Field(
        default="http://prefect-server.default.svc.cluster.local:4200/api"
    )
    prefect_in_cluster_is_enabled: bool = Field(default=False)
    prefect_server_version: str = Field()
    primary_domain_name: str = Field()
    pyenv_version: str = Field()
    python_target_version: str = Field()
    ray_version: str = Field()
    slack_bot_token: Optional[SecretStr] = Field(default=None)
    slack_signing_secret: Optional[SecretStr] = Field(default=None)
    smtp_password: SecretStr = Field()
    smtp_sender: str = Field()
    smtp_user: str = Field()
    ssh_private_key: SecretStr = Field()
    ssh_public_key: SecretStr = Field()
    tavily_api_key: Optional[SecretStr] = Field(default=None)
    tf_api_token: SecretStr = Field()
    tf_http_address: str = Field()
    tf_username: str = Field()
    timestep_ai_is_enabled: bool = Field(default=True)
    ubuntu_version: str = Field()
    version: str = Field()

    class Config:
        env_file = (".dot.env", ".env")
        env_file_encoding = "utf-8"
        secrets_dir = "./secrets"
