# import os
# import pathlib
# import socket
# import tempfile
# from typing import Dict, Optional

# from prefect.blocks.core import Block
# from prefect.blocks.fields import SecretDict
# from prefect_shell import ShellOperation
# from pydantic import SecretStr

# BASE_PATH = pathlib.Path.cwd()
# DIST_PATH: str = f"{BASE_PATH}/dist"

# use_tmpdirname = False


# class SecureShellCredentials(Block):
#     _block_type_slug: str = "ssh-credentials"

#     public_key: Optional[str] = None
#     private_key: Optional[SecretStr] = None

#     def block_initialization(self):
#         if self.public_key is None or self.private_key is None:
#             with tempfile.TemporaryDirectory() as tmpdirname:
#                 comment = f"{os.environ.get('USER')}@{socket.gethostname()}"
#                 key_type = "ed25519"

#                 if use_tmpdirname:
#                     output_keyfile = f"{tmpdirname}/.ssh/id_{key_type}"
#                 else:
#                     output_keyfile = f"{BASE_PATH}/.ssh/id_{key_type}"

#                 if not os.path.exists(output_keyfile):
#                     os.makedirs(os.path.dirname(output_keyfile), exist_ok=True)

#                     command = f"""ssh-keygen \
# -t {key_type} \
# -C {comment} \
# -f {output_keyfile} \
# -N ''"""
#                     with ShellOperation(
#                         commands=[command],
#                     ) as shell_operation:
#                         shell_process = shell_operation.trigger()
#                         shell_process.wait_for_completion()

#                 self.public_key = pathlib.Path(f"{output_keyfile}.pub").read_text()
#                 self.private_key = SecretStr(pathlib.Path(output_keyfile).read_text())


# class AppConfig(Block):
#     _block_type_slug: str = "app-config"
#     secrets: SecretDict
#     variables: Dict

import pathlib
from enum import StrEnum, auto

from pydantic import BaseSettings, Field, SecretStr

BASE_PATH = pathlib.Path.cwd()
CPUS: int = 2
DISK_SIZE_GB: int = 60
DIST_PATH: str = f"{BASE_PATH}/cdktf.out"
MEMORY_SIZE_GB: int = 2
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
    cdktf_outdir: str = Field(env="CDKTF_OUTDIR")
    cloud_instance_name: str = Field(env="CLOUD_INSTANCE_NAME")
    cloud_instance_provider: str = Field(
        default=CloudInstanceProvider.MULTIPASS, env="CLOUD_INSTANCE_PROVIDER"
    )
    cloud_instance_user: str = Field(env="CLOUD_INSTANCE_USER")
    domain_name_registrar_provider: str = Field(
        default=DomainNameRegistrarProvider.NONE, env="DOMAIN_NAME_REGISTRAR_PROVIDER"
    )
    kubecontext: str = Field(env="KUBECONTEXT")
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
    primary_domain_name: str = Field(env="PRIMARY_DOMAIN_NAME")
    ssh_private_key: SecretStr = Field(env="SSH_PRIVATE_KEY")
    ssh_public_key: str = Field(env="SSH_PUBLIC_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        secrets_dir = "./secrets"
