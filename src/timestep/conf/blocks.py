import os
import pathlib
import socket
import tempfile
from enum import StrEnum, auto
from typing import Dict, Optional

from prefect.blocks.core import Block
from prefect.blocks.fields import SecretDict
from prefect_shell import ShellOperation
from pydantic import SecretStr

BASE_PATH = pathlib.Path.cwd()
DIST_PATH: str = f"{BASE_PATH}/dist"

use_tmpdirname = False


class SecureShellCredentials(Block):
    _block_type_slug: str = "ssh-credentials"

    public_key: Optional[str] = None
    private_key: Optional[SecretStr] = None

    def block_initialization(self):
        if self.public_key is None or self.private_key is None:
            with tempfile.TemporaryDirectory() as tmpdirname:
                comment = f"{os.environ.get('USER')}@{socket.gethostname()}"
                key_type = "ed25519"

                if use_tmpdirname:
                    output_keyfile = f"{tmpdirname}/.ssh/id_{key_type}"
                else:
                    output_keyfile = f"{BASE_PATH}/.ssh/id_{key_type}"

                if not os.path.exists(output_keyfile):
                    os.makedirs(os.path.dirname(output_keyfile), exist_ok=True)

                    command = f"""ssh-keygen \
-t {key_type} \
-C {comment} \
-f {output_keyfile} \
-N ''"""
                    with ShellOperation(
                        commands=[command],
                    ) as shell_operation:
                        shell_process = shell_operation.trigger()
                        shell_process.wait_for_completion()

                self.public_key = pathlib.Path(f"{output_keyfile}.pub").read_text()
                self.private_key = SecretStr(pathlib.Path(output_keyfile).read_text())


class CloudInstanceProvider(StrEnum):
    DIGITALOCEAN: str = auto()
    MULTIPASS: str = auto()


class DomainNameRegistrarProvider(StrEnum):
    NAMECHEAP: str = auto()


class AppConfig(Block):
    _block_type_slug: str = "app-config"
    secrets: SecretDict
    variables: Dict
