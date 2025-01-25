import os
import time
from pathlib import Path

import docker
import paramiko


def run_kompose_convert(cwd: Path, env: dict, out: str):
    client = docker.from_env()

    # Configure the volume mapping
    volumes = {str(cwd): {"bind": "/opt", "mode": "rw"}}

    try:
        client.images.get("kompose")

    except docker.errors.ImageNotFound:
        print("Image 'kompose' not found. Building it now...")
        client.images.build(
            path="https://github.com/kubernetes/kompose.git#main",
            pull=True,
            tag="kompose",
        )

    try:
        command = f"cd /opt && kompose convert --chart --file docker-compose.yaml --out {out} --with-kompose-annotation=false"

        container = client.containers.run(
            command=["sh", "-c", command],
            detach=True,  # Run in background
            environment=env,
            image="kompose",
            remove=True,  # equivalent to --rm
            stdin_open=True,  # equivalent to -i
            tty=True,  # equivalent to -t
            user=f"{os.getuid()}:{os.getgid()}",
            volumes=volumes,
        )

        # Stream the logs
        for log in container.logs(stream=True, follow=True):
            print(log.decode().strip(), end="")

        print("")

        # Wait for container to finish
        result = container.wait()
        if result["StatusCode"] != 0:
            raise Exception(f"Container exited with status code {result['StatusCode']}")

    except docker.errors.ContainerError as e:
        print(f"Container error: {e}")
    except docker.errors.ImageNotFound:
        print("Image 'kompose' not found")
    except docker.errors.APIError as e:
        print(f"Docker API error: {e}")
    finally:
        # Ensure the container is removed even if an error occurred
        try:
            container.remove(force=True)
        except:
            pass


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
