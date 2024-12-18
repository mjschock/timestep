import os
import time

import paramiko


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

            _, stdout, stderr = client.exec_command(script)

            print("stdout:")
            print(stdout.read().decode())

            print("stderr:")
            print(stderr.read().decode())

            return client

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(10)

    raise Exception("Failed to connect after multiple attempts")
