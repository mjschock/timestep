import os
import time
import uuid

import typer
from openai.types.file_object import FileObject
from prefect import flow, task
from prefect.artifacts import create_link_artifact
from starlette.datastructures import UploadFile

app_dir = typer.get_app_dir("timestep")


# async def create_file(file, purpose):  # noqa: E501
async def create_file(body, file: UploadFile):
    """Upload a file that can be used across various endpoints. Individual files can be up to 512 MB, and the size of all files uploaded by one organization can be up to 100 GB.  The Assistants API supports files up to 2 million tokens and of specific file types. See the [Assistants Tools guide](/docs/assistants/tools) for details.  The Fine-tuning API only supports &#x60;.jsonl&#x60; files. The input also has certain required formats for fine-tuning [chat](/docs/api-reference/fine-tuning/chat-input) or [completions](/docs/api-reference/fine-tuning/completions-input) models.  The Batch API only supports &#x60;.jsonl&#x60; files up to 100 MB in size. The input also has a specific required [format](/docs/api-reference/batch/request-input).  Please [contact us](https://help.openai.com/) if you need to increase these storage limits.

     # noqa: E501

    :param file: The File object (not file name) to be uploaded.
    :type file: str
    :param purpose: The intended purpose of the uploaded file.  Use \\\&quot;assistants\\\&quot; for [Assistants](/docs/api-reference/assistants) and [Message](/docs/api-reference/messages) files, \\\&quot;vision\\\&quot; for Assistants image file inputs, \\\&quot;batch\\\&quot; for [Batch API](/docs/guides/batch), and \\\&quot;fine-tune\\\&quot; for [Fine-tuning](/docs/api-reference/fine-tuning).
    :type purpose: str

    :rtype: Union[OpenAIFile, Tuple[OpenAIFile, int], Tuple[OpenAIFile, int, Dict[str, str]]
    """

    purpose = body.get("purpose")

    if purpose == "fine-tune":
        # file_object = FileObject(
        #     id=str(uuid.uuid4()),
        #     bytes=file.size,
        #     created_at=int(time.time()),
        #     filename=file.filename,
        #     object="file",
        #     purpose="fine-tune",
        #     status="uploaded",
        # )

        # os.makedirs(f"{app_dir}/data/{file_object.id}", exist_ok=True)

        # contents = file.file.read() # TODO: stream directly to file instead of loading fully in memory first

        # with open(f"{app_dir}/data/{file_object.id}/{file_object.filename}", "w") as f:
        #     f.write(contents.decode("utf-8"))

        # instance_store._shared_instance_state["file_objects"][file_object.id] = file_object

        artifact_id: uuid.UUID = create_link_artifact(
            description=f"## Fine-tuning file upload of {file.filename}",
            # key="irregular-data",
            key=file.filename,
            # link="https://nyc3.digitaloceanspaces.com/my-bucket-name/highly_variable_data.csv",
            link=f"file://{app_dir}/data/{file.filename}",
            # link_text
            # description="## Highly variable data",
        )

        # os.makedirs(f"{app_dir}/data/{file.filename}", exist_ok=True)

        contents = (
            file.file.read()
        )  # TODO: stream directly to file instead of loading fully in memory first

        with open(f"{app_dir}/data/{file.filename}", "w") as f:
            f.write(contents.decode("utf-8"))

        file_object = FileObject(
            # id=str(uuid.uuid4()),
            id=str(artifact_id),
            bytes=file.size,
            created_at=int(time.time()),
            filename=file.filename,
            object="file",
            purpose="fine-tune",
            status="uploaded",
        )

        return file_object.model_dump(mode="json")

    else:
        raise NotImplementedError


async def delete_file(file_id):  # noqa: E501
    """Delete a file.

     # noqa: E501

    :param file_id: The ID of the file to use for this request.
    :type file_id: str

    :rtype: Union[DeleteFileResponse, Tuple[DeleteFileResponse, int], Tuple[DeleteFileResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


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
