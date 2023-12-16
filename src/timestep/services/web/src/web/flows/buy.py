import logging
import os

from prefect import flow
from prefect_aws import MinIOCredentials, S3Bucket

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@flow(log_prints=True)
def buy():
    print("Buying securities")


def deploy_flow():
    # return buy.deploy(
    #     name="my-code-baked-into-an-image-deployment",
    #     build=False,
    #     image="prefecthq/prefect:2.14.6-python3.11-kubernetes",
    #     push=False,
    #     work_pool_name="default-worker-pool",
    # )

    logger.info("Deploying flow")

    minio_endpoint_url = f'http://{os.getenv("MINIO_ENDPOINT")}'
    minio_credentials = MinIOCredentials(
        aws_client_parameters={
            "endpoint_url": minio_endpoint_url,
            # "use_ssl": False,
        },
        minio_root_user=os.getenv("MINIO_ROOT_USER"),
        minio_root_password=os.getenv("MINIO_ROOT_PASSWORD"),
    )

    minio_credentials.save("minio-credentials", overwrite=True)

    logger.info("Saved minio credentials")

    # s3_client = minio_credentials.get_boto3_session().client(
    #     service="s3",
    #     endpoint_url=minio_endpoint_url,
    # )

    minio_block = S3Bucket(
        bucket_name="default",
        bucket_folder="test",
        credentials=minio_credentials,
    )

    # minio_block = RemoteFileSystem(
    #     # basepath="s3://default",
    #     # basepath="s3://my-bucket",
    #     basepath="minio://my-bucket",
    #     settings={
    #         "key": os.getenv("MINIO_ROOT_USER"),
    #         "secret": os.getenv("MINIO_ROOT_PASSWORD"),
    #         "client_kwargs": {"endpoint_url": minio_endpoint_url},
    #     },
    # )
    minio_block.save("minio", overwrite=True)

    logger.info("Saved minio block")

    # uploaded_file_count = minio_block.put_directory(
    #     # ignore_file=ignore_file, to_path=self.path
    # )

    # logger.info("Saved minio block")

    # deployment = Deployment.build_from_flow(
    #     flow=buy,
    #     apply=False,
    #     # infrastructure="kubernetes",
    #     name="my-code-baked-into-an-image-deployment",
    #     skip_upload=True,
    #     # storage=minio_block,
    #     work_pool_name="default-worker-pool",
    #     work_queue_name="default",
    # )

    # logger.info("Built deployment")

    # id = deployment.apply(upload=False)

    # logger.info(f"Applied deployment {id}")

    # file_count = deployment.upload_to_storage(storage_block='s3-bucket/minio')

    # logger.info(f"Uploaded {uploaded_file_count} files")

    # return deployment

    # return deploy(
    #     buy.to_deployment(
    #         name="my-code-baked-into-an-image-deployment",
    #     ),
    #     build=False,
    #     image="prefecthq/prefect:2.14.6-python3.11-kubernetes",
    #     push=False,
    #     work_pool_name="default-worker-pool",
    # )


if __name__ == "__main__":
    deploy_flow()
