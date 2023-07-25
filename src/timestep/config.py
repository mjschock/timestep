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

from pydantic import BaseModel, Field, SecretStr

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
MULTIPASS_INSTANCE_MEMORY: int = f"{MEMORY_SIZE_GB}G"


class CloudInstanceProvider(StrEnum):
    DIGITALOCEAN: str = auto()
    MULTIPASS: str = auto()


class MainConfig(BaseModel):
    base_path: str = BASE_PATH
    cdktf_outdir: str = Field(alias="CDKTF_OUTDIR")
    cloud_instance_cloud_init_config_username: str = Field(
        alias="CLOUD_INSTANCE_CLOUD_INIT_CONFIG_USERNAME", default="ubuntu"
    )  # noqa: E501
    cloud_instance_provider: str = Field(
        alias="CLOUD_INSTANCE_PROVIDER", default=CloudInstanceProvider.MULTIPASS
    )  # noqa: E501
    cpus: int = CPUS
    disk_size_gb: int = DISK_SIZE_GB
    dist_path: str = DIST_PATH
    do_droplet_image: str = DO_DROPLET_IMAGE
    do_droplet_region: str = DO_DROPLET_REGION
    do_droplet_size: str = DO_DROPLET_SIZE
    kubecontext: str = Field(alias="KUBECONTEXT")
    memory_size_gb: int = MEMORY_SIZE_GB
    multipass_instance_cpus: int = MULTIPASS_INSTANCE_CPUS
    multipass_instance_disk: str = MULTIPASS_INSTANCE_DISK
    multipass_instance_image: str = MULTIPASS_INSTANCE_IMAGE
    multipass_instance_memory: int = MULTIPASS_INSTANCE_MEMORY
    primary_domain_name: str = Field(alias="PRIMARY_DOMAIN_NAME")
    ssh_public_key: str = Field(alias="SSH_PUBLIC_KEY")
    ssh_private_key: SecretStr = Field(alias="SSH_PRIVATE_KEY")
