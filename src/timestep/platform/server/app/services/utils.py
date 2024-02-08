import base64
import hashlib
import os
from typing import Any, Dict, List

import kedro
import kubernetes
import sky
import yaml
from minio import Minio
from prefect import deploy
from prefect.blocks.system import Secret
from prefect.runner.runner import RunnerDeployment
from prefect.runner.storage import RemoteStorage
from prefect_aws import AwsClientParameters, MinIOCredentials, S3Bucket
from pydantic import SecretStr


def load_kubeconfig(overwrite=True, memo: Dict[str, Any] = {}):
    kubeconfig_path = os.path.expanduser(sky.clouds.kubernetes.CREDENTIAL_PATH)

    if overwrite or not os.path.exists(kubeconfig_path):
        cluster_name = os.getenv("PRIMARY_DOMAIN_NAME")
        kubecontext = os.getenv("KUBECONTEXT")
        kubernetes_service_host = os.getenv("KUBERNETES_SERVICE_HOST")
        kubernetes_service_port = os.getenv("KUBERNETES_SERVICE_PORT")
        user_name = os.getenv("PRIMARY_DOMAIN_NAME")

        ca_certificate_path = "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        # namespace_path = "/var/run/secrets/kubernetes.io/serviceaccount/namespace"
        service_account_token_path = (
            "/var/run/secrets/kubernetes.io/serviceaccount/token"
        )

        kubernetes.config.load_incluster_config()
        config = kubernetes.client.Configuration.get_default_copy()

        server = config.host

        assert (
            server == f"https://{kubernetes_service_host}:{kubernetes_service_port}"
        ), f"{server} != https://{kubernetes_service_host}:{kubernetes_service_port}"

        ssl_ca_cert = config.ssl_ca_cert

        assert (
            ssl_ca_cert == ca_certificate_path
        ), f"{ssl_ca_cert} != {ca_certificate_path}"

        # Load CA certificate and encode it in base64
        with open(ssl_ca_cert, "rb") as ssl_ca_cert_file:
            certificate_authority_data = base64.b64encode(
                ssl_ca_cert_file.read()
            ).decode("utf-8")

        # Load service account token
        with open(service_account_token_path, "rb") as token_file:
            service_account_token = token_file.read()

        # Create kubeconfig dictionary
        kubeconfig = {
            "apiVersion": "v1",
            "kind": "Config",
            "clusters": [
                {
                    "cluster": {
                        "certificate-authority-data": certificate_authority_data,
                        "server": server,
                    },
                    "name": cluster_name,
                }
            ],
            "contexts": [
                {
                    "context": {
                        "cluster": cluster_name,
                        # "namespace": namespace,
                        "user": user_name,
                    },
                    "name": kubecontext,
                }
            ],
            "current-context": kubecontext,
            "preferences": {},
            "users": [
                {
                    "name": user_name,
                    "user": {"token": service_account_token},
                }
            ],
        }

        # Create ~/.kube directory if it doesn't exist
        kube_dir = os.path.dirname(kubeconfig_path)
        os.makedirs(kube_dir, exist_ok=True)

        # Save the kubeconfig dictionary to ~/.kube/config
        with open(kubeconfig_path, "w") as outfile:
            yaml.dump(kubeconfig, outfile, default_flow_style=False)

        if not os.path.exists(kubeconfig_path):
            raise RuntimeError(f"{kubeconfig_path} file has not been generated.")

    # memo["kubeconfig_path"] = kubeconfig_path

    return memo

async def load_cloud_credentials(memo: Dict[str, Any]):
    try:
        kubernetes.config.load_incluster_config()
        memo = load_kubeconfig(memo)

    except kubernetes.config.config_exception.ConfigException as e:
        print(e)

    return memo

async def sky_check_task(memo: dict[str, Any]):
    sky.check.check()

    enabled_clouds: list[sky.clouds.Cloud] = sky.global_user_state.get_enabled_clouds()
    enabled_storage_clouds: list[
        str
    ] = sky.global_user_state.get_enabled_storage_clouds()

    memo["enabled_clouds"] = enabled_clouds
    memo["enabled_storage_clouds"] = enabled_storage_clouds

    return memo

async def sky_status_task(memo: dict[str, Any], refresh: bool = True):
    memo["cluster_statuses"]: list[dict[str, Any]] = sky.core.status(refresh=refresh)

    return memo

async def sky_queue_task(name: str, memo: dict[str, Any]):
    memo["cluster_queue"]: List[dict] = sky.core.queue(cluster_name=name)

    return memo

async def create_minio_bucket(bucket_name: str, ignore_exists: bool = False) -> str:
    minio_endpoint = os.getenv("MINIO_ENDPOINT")
    minio_client = Minio(
        minio_endpoint,
        access_key=os.getenv("MINIO_ROOT_USER"),
        secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
        secure=False,
    )

    if minio_client.bucket_exists(bucket_name):
        if ignore_exists:
            return bucket_name

        else:
            raise Exception(f"Bucket {bucket_name} already exists")

    minio_client.make_bucket(bucket_name)

    return bucket_name

async def create_minio_storage_block(
    account_id: str,
    agent_name: str,
    bucket_folder: str,
    bucket_name: str,
):
    minio_endpoint_url = f'http://{os.getenv("MINIO_ENDPOINT")}'
    minio_storage_block = S3Bucket(
        bucket_folder=bucket_folder,
        bucket_name=bucket_name,
        credentials=MinIOCredentials(
            aws_client_parameters=AwsClientParameters(
                endpoint_url=minio_endpoint_url,
                verify=False,
                use_ssl=False,
            ),
            minio_root_user=os.getenv("MINIO_ROOT_USER"),
            minio_root_password=SecretStr(os.getenv("MINIO_ROOT_PASSWORD")),
        ),
    )
    storage_block_name = f"{bucket_name}-{bucket_folder}"

    await minio_storage_block.save(storage_block_name, overwrite=True)

    return await S3Bucket.load(storage_block_name)

async def upload_directory_to_minio(
    minio_storage_block: S3Bucket,
    local_path: str,
    to_path: str,
) -> int:
    return await minio_storage_block.put_directory(
        local_path=local_path,
        to_path=to_path,
    )

async def deploy_agent(
    uploaded_file_count: int,
    account_id: str,
    agent_name: str,
    bucket_name: str,
):
    minio_endpoint = os.getenv("MINIO_ENDPOINT")
    minio_endpoint_url = f"http://{minio_endpoint}"
    minio_root_user_secret_block = Secret(value=SecretStr(os.getenv("MINIO_ROOT_USER")))
    minio_root_password_secret_block = Secret(
        value=SecretStr(os.getenv("MINIO_ROOT_PASSWORD"))
    )

    await minio_root_user_secret_block.save("minio-root-user", overwrite=True)
    await minio_root_password_secret_block.save("minio-root-password", overwrite=True)

    storage = RemoteStorage(
        url=f"s3://{bucket_name}/{account_id}/agents/{agent_name}",
        key=minio_root_user_secret_block,
        secret=minio_root_password_secret_block,
        client_kwargs={
            "endpoint_url": minio_endpoint_url,
            "verify": False,
            "use_ssl": False,
        },
    )

    deployment: RunnerDeployment = RunnerDeployment(
        flow_name="serve-agent-flow",
        entrypoint="flow.py:serve_agent_flow",
        job_variables={
            "env": {
                "EXTRA_PIP_PACKAGES": f"""
                    kedro=={kedro.__version__}
                """,
                "KUBECONTEXT": os.getenv("KUBECONTEXT"),
                "MINIO_ENDPOINT": os.getenv("MINIO_ENDPOINT"),
                "MINIO_ROOT_USER": os.getenv("MINIO_ROOT_USER"),
                "MINIO_ROOT_PASSWORD": os.getenv("MINIO_ROOT_PASSWORD"), # TODO: Use Secrets
                "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
                "PRIMARY_DOMAIN_NAME": os.getenv("PRIMARY_DOMAIN_NAME"),
            },
            "service_account_name": "prefect-worker-job-service-account",
        },
        name="serve-agent-flow-deployment",
        parameters={
            "account_id": account_id,
            "agent_name": agent_name,
        },
        storage=storage,
        work_pool_name="default-worker-pool",
        work_queue_name="default",
    )

    deployment_ids: list = await deploy(
        deployment,
        build=False,
        image="registry.gitlab.com/timestep-ai/timestep/server:latest",
        push=False,
        work_pool_name="default-worker-pool",
    )

    return deployment_ids

def generate_folder_hash(folder_path, hash_algorithm='sha256'):
    # Choose the hash algorithm (e.g., 'sha256', 'md5', etc.)
    hasher = hashlib.new(hash_algorithm)

    # Walk through all files and subdirectories in the folder
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Calculate hash for each file
            with open(file_path, 'rb') as f:
                # Read the file in chunks to handle large files
                for chunk in iter(lambda: f.read(4096), b''):
                    hasher.update(chunk)

    # Return the hexadecimal digest of the hash
    return hasher.hexdigest()

def get_agent_deployment_idempotency_key(
    local_path: str,
):
    return generate_folder_hash(local_path)
