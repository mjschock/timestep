from pydantic import BaseModel, validator
import pathlib
import os

BASE_PATH = pathlib.Path.cwd()
DIST_PATH: str = f"{BASE_PATH}/dist"

CPUS: int = 1
DISK_SIZE_GB: int = 10

class MainConfig(BaseModel): # TODO: Make this a Prefect Block with secrets
    class CLOUD_INSTANCE_PROVIDERS:
        MULTIPASS: str = "multipass"
        DIGITALOCEAN: str = "digitalocean"

    # CADDY_INGRESS_CONTROLLER_EMAIL: str = "m@mjschock.com"
    # CADDY_INGRESS_CONTROLLER_CHART_PATH: str = f"{BASE_PATH}/src/timestep/infra/ingress/charts/caddy-ingress-controller"
    # DOCKER_REGISTRY_HTPASSWD: str = "admin:$2a$10$70qctd/h6OkNr4ugiFoPWuBLowf5TqRr/Y3R.6LGPCqelHG5JRa7e" # admin:BVNt6uwp95H6o4e59022
    # CDKTF_OUTDIR: str = os.environ.get("CDKTF_OUTDIR", f"{DIST_PATH}/cdktf.out")
    # CDKTF_OUTDIR: str = None
    # CLOUD_CONFIG_PATH: str = f"{DIST_PATH}/cloud-config.yml"
    # CLOUD_CONFIG_PATH: str = f"{DIST_PATH}/cloud-config.yaml"
    CLOUD_CONFIG_PATH: str = "cloud-config.yaml"
    CLOUD_INSTANCE_PROVIDER: str = CLOUD_INSTANCE_PROVIDERS.MULTIPASS
    # CLOUD_INSTANCE_PROVIDER: str = "multipass"
    CLOUD_INSTANCE_NAME: str = "timestep-ai"
    DO_DROPLET_IMAGE: str = "ubuntu-22-04-x64"
    DO_DROPLET_REGION: str = "sfo3"
    DO_DROPLET_SIZE: str = f"s-{CPUS}vcpu-512mb-{DISK_SIZE_GB}gb"
    DO_TOKEN: str = None
    # DOMAIN: str = "timestep.local"
    # HOSTS_FILE_PATH: str = f"{DIST_PATH}/.etchosts"
    # KUBE_CONFIG_PATH: str = f"{DIST_PATH}/kube-config.yml"
    # KUBE_CONTEXT: str = "timestep-ai"
    KUBECONTEXT: str = "default"
    MULTIPASS_INSTANCE_CPUS: int = CPUS
    MULTIPASS_INSTANCE_DISK: str = f"{DISK_SIZE_GB}G"
    MULTIPASS_INSTANCE_IMAGE: str = "22.04"
    # NAMECHEAP_API_KEY: str = os.environ.get("NAMECHEAP_API_KEY")
    # NAMECHEAP_API_USER: str = os.environ.get("NAMECHEAP_API_USER")
    # NAMECHEAP_USER_NAME: str = os.environ.get("NAMECHEAP_USER_NAME")
    # PLATFORM_CHART_PATH: str = f"{DIST_PATH}/charts/platform"
    # REGISTRY_URL=f"registry.{DOMAIN}"
    # SSH_AUTHORIZED_KEYS_PATH: str = f"{DIST_PATH}/.ssh/authorized_keys"
    SSH_PUBLIC_KEY: str = None
    # SSH_PUBLIC_KEY_PATH: str = f"{DIST_PATH}/.ssh/id_rsa.pub"
    # SSH_PRIVATE_KEY_PATH: str = f"{DIST_PATH}/.ssh/id_rsa"
    SSH_PUBLIC_KEY_PATH: str = ".ssh/id_rsa.pub"
    SSH_PRIVATE_KEY_PATH: str = ".ssh/id_rsa"
    STACK_ID: str = None

    # @validator('SSH_PUBLIC_KEY_PATH')
    # def ssh_public_key_path_must_end_in_pub(cls, v):
    #     if v is not None and not v.endswith('.pub'):
    #         raise ValueError('SSH_PUBLIC_KEY_PATH must end in .pub')

    #     return v
