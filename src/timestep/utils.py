import os
import time

import paramiko
from libcloud.compute.base import KeyPair, NodeDriver


def get_or_create_key_pair(node_driver: NodeDriver, name: str, content: str) -> KeyPair:
    # TODO: what about we want to delete the key pair? delete_key_pair

    key_pair: KeyPair | None = node_driver.get_key_pair(name=name)

    if not key_pair:
        key_pair: KeyPair = node_driver.create_key_pair(name=name, public_key=content)

    return key_pair


def ssh_connect(
    ip_address: str, script: str, username: str, ssh_key: str
) -> paramiko.SSHClient:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            client.connect(
                hostname=ip_address,
                username=username,
                key_filename=os.path.expanduser(ssh_key),
                timeout=10,
            )

            stdin, stdout, stderr = client.exec_command(script)

            print("stdout:")
            print(stdout.read().decode())

            print("stderr:")
            print(stderr.read().decode())

            return client

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(10)

    raise Exception("Failed to connect after multiple attempts")
