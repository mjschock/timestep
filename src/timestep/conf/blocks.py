import os
import pathlib
import socket
import tempfile
from enum import StrEnum, auto
from typing import Dict, Optional

from prefect import flow
from prefect.blocks.core import Block
from prefect.blocks.fields import SecretDict
from prefect.blocks.kubernetes import KubernetesClusterConfig
from prefect.blocks.system import Secret
from prefect.exceptions import ObjectNotFound
from prefect_shell import ShellOperation
from pydantic import BaseModel, SecretStr, validator

BASE_PATH = pathlib.Path.cwd()
DIST_PATH: str = f"{BASE_PATH}/dist"


class SecureShellCredentials(Block):
    _block_type_slug: str = "ssh-credentials"

    # comment: Optional[str] = f"{os.environ.get('USER')}@{socket.gethostname()}"
    # key_type: Optional[str] = "ed25519"
    # new_passphrase: Optional[SecretStr] = "''"
    # output_keyfile: Optional[str] = f"{DIST_PATH}/.ssh/id_{key_type}"
    public_key: Optional[str] = None
    private_key: Optional[SecretStr] = None

    def block_initialization(self):
        if self.public_key is None or self.private_key is None:
            with tempfile.TemporaryDirectory() as tmpdirname:
                comment = f"{os.environ.get('USER')}@{socket.gethostname()}"
                key_type = "ed25519"
                output_keyfile = f"{tmpdirname}/.ssh/id_{key_type}"

                if not os.path.exists(output_keyfile):
                    os.makedirs(os.path.dirname(output_keyfile), exist_ok=True)

                    with ShellOperation(
                        commands=[
                            f"ssh-keygen -t {key_type} -C {comment} -f {output_keyfile} -N ''",
                        ],
                    ) as shell_operation:
                        shell_process = shell_operation.trigger()
                        shell_process.wait_for_completion()

                self.public_key = pathlib.Path(f"{output_keyfile}.pub").read_text()
                self.private_key = SecretStr(pathlib.Path(output_keyfile).read_text())

            # Delete the key files after they are loaded into memory
            # os.remove(f"{output_keyfile}.pub")
            # os.remove(output_keyfile)

        # with tempfile.TemporaryDirectory() as tmpdirname:
        #     fp.write(ssh_private_key.get_secret_value().encode())
        #     fp.flush()

        #     local_exec_provisioner = LocalExecProvisioner( # TODO: use --print-config
        #         command=f"k3sup install --context {kubecontext} --ip {ip} --local-path {local_path} --skip-install --ssh-key {fp.name} --user ubuntu",
        #         type="local-exec",
        #     )

    # def save_private_key_to_tempfile(self):
    # with tempfile.NamedTemporaryFile(
    #     delete=False,
    #     dir=DIST_PATH,
    # ) as fp:
    #     fp.write(self.private_key.get_secret_value().encode())
    #     fp.flush()

    #     return fp.name

    # if not os.path.exists(f"{DIST_PATH}/.ssh"):
    #     os.makedirs(f"{DIST_PATH}/.ssh")
    # if not os.path.exists(self.output_keyfile):

    # shell_output = ShellOperation(
    #     commands=[
    #         f"ssh-keygen -t ed25519 -f {DIST_PATH}/.ssh/id_ed25519 -N ''",
    #     ],
    #     shell="bash",
    # ).run()

    # self.public_key = pathlib.Path(f"{DIST_PATH}/.ssh/id_ed25519.pub").read_text()
    # self.private_key = SecretStr(pathlib.Path(f"{DIST_PATH}/.ssh/id_ed25519").read_text())

    #     comment = f"{os.environ.get('USER')}@{socket.gethostname()}"
    #     key_type = "ed25519"
    #     new_passphrase = "''"
    #     output_keyfile = f"{DIST_PATH}/.ssh/id_{key_type}"

    #     with ShellOperation(
    #         commands=[
    #             f"ssh-keygen -t {key_type} -C {comment} -f {output_keyfile} -N {new_passphrase}",
    #         ],
    #     ) as shell_operation:
    #         shell_process = shell_operation.trigger()
    #         shell_process.wait_for_completion()

    #     self.ssh_public_key = pathlib.Path(f"{output_keyfile}.pub").read_text()
    #     self.ssh_private_key = SecretStr(pathlib.Path(output_keyfile).read_text())


# class KubeConfig(Block):
#     _block_type_slug: str = "kube-config"

#     private_key: SecretStr = None
#     ip: str = None

#     def block_initialization(self):
#         context = "default"
#         local_path = f"{DIST_PATH}/kube-config.yml"
#         # ssh_key = f"{DIST_PATH}/.ssh/id_ed25519"

#         with tempfile.NamedTemporaryFile() as fp:
#             fp.write(self.private_key.get_secret_value().encode())
#             fp.flush()

#             with ShellOperation(
#                 commands=[
#                     f"k3sup install --context {context} --ip {self.ip} --local-path {local_path} --skip-install --ssh-key {fp.name} --user ubuntu"
#                 ],
#             ) as shell_operation:
#                 shell_process = shell_operation.trigger()
#                 shell_process.wait_for_completion()

# self.public_key = pathlib.Path(f"{output_keyfile}.pub").read_text()
# self.private_key = SecretStr(pathlib.Path(output_keyfile).read_text())


# ssh_credentials_block = SecureShellCredentials(
#     public_key="AKIAJKLJKLJKLJKLJKLJK",
#     private_key="secret_access_key"
# )

# ssh_credentials_block.save(
#     name="ssh-credentials",
#     overwrite=True,
# )


class CloudInitConfig(Block):
    _block_type_slug: str = "cloud-init-config"

    ssh_credentials: SecureShellCredentials

    def block_initialization(self):
        pass


class CloudInstanceProvider(StrEnum):
    DIGITALOCEAN: str = auto()
    MULTIPASS: str = auto()


class DomainNameRegistrarProvider(StrEnum):
    NAMECHEAP: str = auto()


class CloudInstanceConfig(Block):
    _block_type_slug: str = "cloud-instance-config"

    cloud_init_config: CloudInitConfig
    cloud_instance_provider: CloudInstanceProvider


class MultipassCloudInstanceConfig(CloudInstanceConfig):
    cloud_instance_provider: CloudInstanceProvider = CloudInstanceProvider.MULTIPASS


class MainConfig(Block):
    _block_type_slug: str = "main-config"

    cloud_instance_config: CloudInstanceConfig
    DOMAIN: str = None
    KUBECONTEXT: str = "default"

    def block_initialization(self):
        pass
        # try:
        #     self.cloud_instance_config = CloudInstanceConfig.load(
        #         name=self.cloud_instance_config_block_name
        #     )

        # except ObjectNotFound:
        #     self.cloud_instance_config = CloudInstanceConfig(

        #     )

        #     self.cloud_instance_config.save(
        #         name=self.cloud_instance_config_block_name,
        #         overwrite=False,
        #     )

    # domain_name_registrar_config: DomainNameRegistrarConfig
    # kube_config: KubernetesClusterConfig

    # class CLOUD_INSTANCE_PROVIDERS:
    #     MULTIPASS: str = "multipass"
    #     DIGITALOCEAN: str = "digitalocean"

    # BASE_PATH: str = f"{BASE_PATH}"
    # CLOUD_CONFIG_PATH: str = "dist/cloud-config.yaml"
    # CLOUD_INSTANCE_PROVIDER: str = CLOUD_INSTANCE_PROVIDERS.MULTIPASS
    # CLOUD_INSTANCE_NAME: str = "timestep-ai"
    # DO_DROPLET_IMAGE: str = "ubuntu-22-04-x64"
    # DO_DROPLET_REGION: str = "sfo3"
    # DO_DROPLET_SIZE: str = f"s-{CPUS}vcpu-512mb-{DISK_SIZE_GB}gb"
    # DO_TOKEN: str = None
    # DOMAIN: str = None
    # HOSTS_FILE_PATH: str = None
    # KUBECONFIG: str = "dist/kube-config.yml"
    # KUBECONTEXT: str = "default"
    # MULTIPASS_INSTANCE_CPUS: int = CPUS
    # MULTIPASS_INSTANCE_DISK: str = f"{DISK_SIZE_GB}G"
    # MULTIPASS_INSTANCE_IMAGE: str = "22.04"
    # NAMECHEAP_API_KEY: str = None
    # NAMECHEAP_API_USER: str = None
    # NAMECHEAP_USER_NAME: str = None
    # SSH_PUBLIC_KEY: str = None
    # SSH_PRIVATE_KEY: str = None
    # SSH_PUBLIC_KEY_PATH: str = "dist/.ssh/id_rsa.pub"
    # SSH_PRIVATE_KEY_PATH: str = "dist/.ssh/id_rsa"
    # TF_API_TOKEN: str = None
    # TERRAFORM_HOSTNAME: str = "app.terraform.io"
    # TERRAFORM_ORGANIZATION: str = "timestep-ai"
    # TERRAFORM_WORKSPACE: str = "timestep-ai"


class AppConfig(Block):
    _block_type_slug: str = "app-config"
    secrets: SecretDict
    variables: Dict

    # comment: Optional[str] = f"{os.environ.get('USER')}@{socket.gethostname()}"
    # key_type: Optional[str] = "ed25519"
    # new_passphrase: Optional[SecretStr] = "''"
    # output_keyfile: Optional[str] = f"{DIST_PATH}/.ssh/id_{key_type}"
    # public_key: Optional[str] = None
    # private_key: Optional[SecretStr] = None

    # def block_initialization(self):
    #     # if self.public_key is None or self.private_key is None:
    #     if not self.variables.get("ssh_public_key", None) or not self.secrets.get("ssh_private_key", None):
    #         comment = f"{os.environ.get('USER')}@{socket.gethostname()}"
    #         key_type = "ed25519"
    #         output_keyfile = f"{DIST_PATH}/.ssh/id_{key_type}"

    #         if not os.path.exists(output_keyfile):
    #             os.makedirs(os.path.dirname(output_keyfile), exist_ok=True)

    #             with ShellOperation(
    #                 commands=[
    #                     f"ssh-keygen -t {key_type} -C {comment} -f {output_keyfile} -N ''",
    #                 ],
    #             ) as shell_operation:
    #                 shell_process = shell_operation.trigger()
    #                 shell_process.wait_for_completion()

    #         self.variables["ssh_public_key"] = pathlib.Path(f"{output_keyfile}.pub").read_text()
    #         self.secrets["ssh_private_key"] = SecretStr(pathlib.Path(output_keyfile).read_text())
