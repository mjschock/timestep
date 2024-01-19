import base64
import os
from typing import Any, Dict

import kedro
import kubernetes
import sky
import yaml
from minio import Minio
from prefect import deploy, flow, task
from prefect.blocks.system import Secret
from prefect.deployments.deployments import run_deployment
from prefect.deployments.runner import DeploymentImage
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

# @task
async def load_cloud_credentials(memo: Dict[str, Any]):
    # logger = get_run_logger()

    try:
        kubernetes.config.load_incluster_config()
        memo = load_kubeconfig(memo)

    except kubernetes.config.config_exception.ConfigException as e:
        # logger.info(e)
        print(e)

    return memo

# @task
async def sky_check_task(memo: dict[str, Any]):
    # logger = get_run_logger()

    sky.check.check()

    enabled_clouds: list[sky.clouds.Cloud] = sky.global_user_state.get_enabled_clouds()
    enabled_storage_clouds: list[
        str
    ] = sky.global_user_state.get_enabled_storage_clouds()

    # logger.info("enabled_clouds: %s", enabled_clouds)
    # logger.info("enabled_storage_clouds: %s", enabled_storage_clouds)

    memo["enabled_clouds"] = enabled_clouds
    memo["enabled_storage_clouds"] = enabled_storage_clouds

    return memo

# @task
async def sky_status_task(memo: dict[str, Any]):
    # logger: logging.Logger = get_run_logger()

    # async with ShellOperation(
    #     commands=[
    #         f"sky status",
    #     ],
    #     # working_dir="workflows",
    #     # working_dir=f"{cwd}/app/api/routers/workflows",
    # ) as sky_op:
    #     sky_op_process = await sky_op.trigger()
    #     await sky_op_process.wait_for_completion()

    memo["cluster_statuses"]: list[dict[str, Any]] = sky.core.status(refresh=True)

    return memo

async def sky_queue_task(name: str, memo: dict[str, Any]):
    memo["cluster_queue"]: list[dict] = sky.core.queue(cluster_name=name)  # noqa: E501

    return memo

# @task
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

# @task
async def create_minio_storage_block(
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

    await minio_storage_block.save("minio-storage", overwrite=True)

    return await S3Bucket.load("minio-storage")

# @task
async def upload_directory_to_minio(
    minio_storage_block: S3Bucket,
    local_path: str,
    to_path: str,
) -> int:
    return await minio_storage_block.put_directory(
        local_path=local_path,
        to_path=to_path,
    )

# @task(
#     timeout_seconds=10,
# )
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
        # flow_name="agent-flow",
        flow_name="serve-agent-flow",
        # flow_name=f"{name}-agent-flow",
        # entrypoint="workflows/agents.py:deploy_agent_flow",
        # entrypoint="serve.py:serve_agent",
        entrypoint="flow.py:serve_agent_flow",
        # entrypoint="register_prefect_flow.py:prefect_deploy",
        # entrypoint="register_prefect_flow.py:my_flow",
        job_variables={
            "env": {
                # "EXTRA_PIP_PACKAGES": f"""
                #     fastapi=={fastapi.__version__}
                #     prefect-aws=={prefect_aws.__version__}
                #     prefect-shell=={prefect_shell.__version__}
                #     s3fs=={s3fs.__version__}
                #     skypilot-nightly[kubernetes]=={sky.__version__}
                # """,
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
        # name="agent-flow-deployment",
        # name=f"{name}-agent-deployment",
        # name=f"{name}-agent-flow-deployment",
        name="serve-agent-flow-deployment",
        parameters={
            "account_id": account_id,
            # "model_ids": ["phi:latest"]
            "name": agent_name,
            # "work_pool_name": "default-worker-pool",
            # "work_queue_name": "default",
            # "pipeline_name": "__default__",
            # "env": "base",
        },
        storage=storage,
        work_pool_name="default-worker-pool",
        work_queue_name="default",
    )

    deployment_ids: list = await deploy(
        deployment,
        build=False,
        # image=DeploymentImage(
        #     name="registry.gitlab.com/timestep-ai/timestep/backend",
        #     # tag="latest",
        #     tag="tilt-10e7c7af83cae422", # TODO: Use Tilt to get appropriate tag
        # ),
        image="registry.gitlab.com/timestep-ai/timestep/backend:latest",
        push=False,
        work_pool_name="default-worker-pool",
    )

    return deployment_ids
