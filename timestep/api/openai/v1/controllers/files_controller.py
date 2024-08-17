import os
import time
import uuid
from datetime import datetime

import libcloud
import typer

# from libcloud.compute.types import Provider
from libcloud.storage.providers import get_driver

# from libcloud.compute.providers import get_driver
from libcloud.storage.types import Provider
from openai.types.file_deleted import FileDeleted
from openai.types.file_object import FileObject
from prefect import flow, get_client, task
from prefect.artifacts import create_link_artifact
from starlette.datastructures import UploadFile

from timestep.config import settings

app_dir = typer.get_app_dir("timestep")


async def create_file(body, file: UploadFile, token_info: dict, user: str):
    """Upload a file that can be used across various endpoints. Individual files can be up to 512 MB, and the size of all files uploaded by one organization can be up to 100 GB.  The Assistants API supports files up to 2 million tokens and of specific file types. See the [Assistants Tools guide](/docs/assistants/tools) for details.  The Fine-tuning API only supports &#x60;.jsonl&#x60; files. The input also has certain required formats for fine-tuning [chat](/docs/api-reference/fine-tuning/chat-input) or [completions](/docs/api-reference/fine-tuning/completions-input) models.  The Batch API only supports &#x60;.jsonl&#x60; files up to 100 MB in size. The input also has a specific required [format](/docs/api-reference/batch/request-input).  Please [contact us](https://help.openai.com/) if you need to increase these storage limits.

     # noqa: E501

    :param file: The File object (not file name) to be uploaded.
    :type file: str
    :param purpose: The intended purpose of the uploaded file.  Use \\\&quot;assistants\\\&quot; for [Assistants](/docs/api-reference/assistants) and [Message](/docs/api-reference/messages) files, \\\&quot;vision\\\&quot; for Assistants image file inputs, \\\&quot;batch\\\&quot; for [Batch API](/docs/guides/batch), and \\\&quot;fine-tune\\\&quot; for [Fine-tuning](/docs/api-reference/fine-tuning).
    :type purpose: str

    :rtype: Union[OpenAIFile, Tuple[OpenAIFile, int], Tuple[OpenAIFile, int, Dict[str, str]]
    """
    purpose = body.get("purpose")

    file_name = file.filename
    file_uuid = uuid.uuid4()

    cls = get_driver(Provider.LOCAL)
    # driver = cls("api key", "api secret key")
    # driver = cls(key=f"{app_dir}/data")
    driver = cls(key=f"{app_dir}")

    # container = driver.get_container(container_name=settings.openai_org_id)
    container = driver.get_container(container_name="data")
    # extra = {"meta_data": {"owner": user, "created": "2014-02-2"}}
    extra = {
        "meta_data": {
            # "artifact_id": artifact_id,
            # "file_object": file_object.model_dump_json(),
            # "created_at": file_object.created_at,
            # "filename": file_object.filename,
            # "purpose": file_object.purpose,
            # "owner": user,
            # "owner": settings.openai_org_id,
            # "created": datetime.today().strftime("%Y-%m-%d"),
            "created_at": int(time.time()),
            "user": user,
            # "organization_id": settings.openai_org_id,
        }
    }

    with file.file as iterator:
        obj: libcloud.storage.base.Object = driver.upload_object_via_stream(
            iterator=iterator,
            container=container,
            object_name=file_name,
            # object_name=str(file_uuid),
            # object_name=str(artifact_id),
            extra=extra,
        )

    async with get_client() as client:
        artifact_id: uuid.UUID = await create_link_artifact(
            client=client,
            description=f"""
            ## File upload of {file_name}.
            
            Organization: {settings.openai_org_id}
            Purpose: {purpose}
            """,
            # key="irregular-data",
            # key=file_name,
            key=str(file_uuid),
            # link="https://nyc3.digitaloceanspaces.com/my-bucket-name/highly_variable_data.csv",
            # link=f"file://{app_dir}/data/{settings.openai_org_id}/{file_name}",
            link=f"file://{app_dir}/data/{file_name}",
            # link_text
            # description="## Highly variable data",
        )

    file_object = FileObject(
        id=str(artifact_id),
        bytes=file.size,
        # created_at=int(time.time()),
        created_at=extra["meta_data"]["created_at"],
        filename=file_name,
        object="file",
        purpose=purpose,
        status="uploaded",
    )

    return file_object.model_dump(mode="json")


async def delete_file(file_id):  # noqa: E501
    """Delete a file.

     # noqa: E501

    :param file_id: The ID of the file to use for this request.
    :type file_id: str

    :rtype: Union[DeleteFileResponse, Tuple[DeleteFileResponse, int], Tuple[DeleteFileResponse, int, Dict[str, str]]
    """
    cls = get_driver(Provider.LOCAL)
    # driver = cls("api key", "api secret key")
    driver = cls(key=f"{app_dir}")
    container = driver.get_container(container_name="data")

    artifact_id = uuid.UUID(file_id)

    raise NotImplementedError

    # artifact = # TODO: Get the artifact from Prefect

    artifact_link = artifact.link
    file_name = Path.from_uri(artifact_link).name

    obj: libcloud.storage.base.Object = driver.delete_object(
        # obj=container.get_object(str(artifact_id))
        obj=container.get_object(file_name)
    )

    # TODO: Delete the Prefect artifact as well

    file_deleted = FileDeleted(id=file_id, deleted=True, object="file")

    return file_deleted.model_dump(mode="json")


async def download_file(file_id):  # noqa: E501
    """Returns the contents of the specified file.

     # noqa: E501

    :param file_id: The ID of the file to use for this request.
    :type file_id: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    raise NotImplementedError


async def list_files(purpose=None):  # noqa: E501
    """Returns a list of files that belong to the user&#39;s organization.

     # noqa: E501

    :param purpose: Only return files with the given purpose.
    :type purpose: str

    :rtype: Union[ListFilesResponse, Tuple[ListFilesResponse, int], Tuple[ListFilesResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


# async def retrieve_file(file_id):  # noqa: E501
# async def retrieve_file(*args, **kwargs):
async def retrieve_file(file_id: str, token_info: dict, user: str):
    """Returns information about a specific file.

     # noqa: E501

    :param file_id: The ID of the file to use for this request.
    :type file_id: str

    :rtype: Union[OpenAIFile, Tuple[OpenAIFile, int], Tuple[OpenAIFile, int, Dict[str, str]]
    """
    file_object: FileObject = instance_store._shared_instance_state["file_objects"][
        file_id
    ]

    return file_object.model_dump(mode="json")
