from pydantic import BaseModel
import pathlib

BASE_PATH = pathlib.Path.cwd()

class AppConfig(BaseModel):
    CLOUD_INSTANCE_PROVIDER: str = "multipass"
    CLOUD_INSTANCE_NAME: str = "timestep-ai"
    CPUS: int = 1
    DISK_SIZE_GB: int = 10
    DO_DROPLET_IMAGE: str = "ubuntu-22-04-x64"
    DO_DROPLET_REGION: str = "sfo3"
    DO_DROPLET_SIZE: str = f"s-{CPUS}vcpu-512mb-{DISK_SIZE_GB}gb"
    DO_TOKEN: str = "dop_v1_733fa9e49f5996b01a20a1b2142696e0a43ca027edae0a4b699ec45a16dacd65"
    DIST_PATH: str = f"{BASE_PATH}/dist"
    DOMAIN: str = "timestep.local"
    MULTIPASS_INSTANCE_CPUS: int = CPUS
    MULTIPASS_INSTANCE_DISK: str = f"{DISK_SIZE_GB}G"
    MULTIPASS_INSTANCE_IMAGE: str = "22.04"
    SSH_AUTHORIZED_KEYS_PATH: str = f"{DIST_PATH}/.ssh/authorized_keys"
