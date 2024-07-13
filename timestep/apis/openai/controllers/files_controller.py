import time
import connexion
from typing import Dict, Literal
from typing import Tuple
from typing import Union

from openai.types.file_object import FileObject
from starlette.datastructures import UploadFile

from timestep.apis.openai.models.delete_file_response import DeleteFileResponse  # noqa: E501
from timestep.apis.openai.models.list_files_response import ListFilesResponse  # noqa: E501
from timestep.apis.openai.models.open_ai_file import OpenAIFile  # noqa: E501
from timestep.apis.openai import util

# def create_file(file, purpose):  # noqa: E501
# def create_file(file):
def create_file(body, file: UploadFile):
    """Upload a file that can be used across various endpoints. Individual files can be up to 512 MB, and the size of all files uploaded by one organization can be up to 100 GB.  The Assistants API supports files up to 2 million tokens and of specific file types. See the [Assistants Tools guide](/docs/assistants/tools) for details.  The Fine-tuning API only supports &#x60;.jsonl&#x60; files. The input also has certain required formats for fine-tuning [chat](/docs/api-reference/fine-tuning/chat-input) or [completions](/docs/api-reference/fine-tuning/completions-input) models.  The Batch API only supports &#x60;.jsonl&#x60; files up to 100 MB in size. The input also has a specific required [format](/docs/api-reference/batch/request-input).  Please [contact us](https://help.openai.com/) if you need to increase these storage limits. 

     # noqa: E501

    :param file: The File object (not file name) to be uploaded. 
    :type file: str
    :param purpose: The intended purpose of the uploaded file.  Use \\\&quot;assistants\\\&quot; for [Assistants](/docs/api-reference/assistants) and [Message](/docs/api-reference/messages) files, \\\&quot;vision\\\&quot; for Assistants image file inputs, \\\&quot;batch\\\&quot; for [Batch API](/docs/guides/batch), and \\\&quot;fine-tune\\\&quot; for [Fine-tuning](/docs/api-reference/fine-tuning). 
    :type purpose: str

    :rtype: Union[OpenAIFile, Tuple[OpenAIFile, int], Tuple[OpenAIFile, int, Dict[str, str]]
    """

    print('file: ', file)
    # file:  UploadFile(
    # filename='tmp_recipe_finetune_training.jsonl', 
    # size=58688,
    # headers=Headers({'content-disposition': 'form-data; name="file"; filename="tmp_recipe_finetune_training.jsonl"', 'content-type': 'application/octet-stream'}))
    print('type(file): ', type(file))
    print('body: ', body)

    purpose = body.get('purpose')
    print('purpose: ', purpose)

    if purpose == "fine-tune":
        print('TODO: create file for fine-tuning')

        return FileObject(
            id=file.filename,
            bytes=file.size,
            created_at=int(time.time()),
            filename=file.filename,
            object="file",
            purpose="fine-tune",
            status="uploaded",
        ).model_dump(mode="json")

    else:
        raise NotImplementedError

    # return 'do some magic!'


def delete_file(file_id):  # noqa: E501
    """Delete a file.

     # noqa: E501

    :param file_id: The ID of the file to use for this request.
    :type file_id: str

    :rtype: Union[DeleteFileResponse, Tuple[DeleteFileResponse, int], Tuple[DeleteFileResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def download_file(file_id):  # noqa: E501
    """Returns the contents of the specified file.

     # noqa: E501

    :param file_id: The ID of the file to use for this request.
    :type file_id: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_files(purpose=None):  # noqa: E501
    """Returns a list of files that belong to the user&#39;s organization.

     # noqa: E501

    :param purpose: Only return files with the given purpose.
    :type purpose: str

    :rtype: Union[ListFilesResponse, Tuple[ListFilesResponse, int], Tuple[ListFilesResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def retrieve_file(file_id):  # noqa: E501
    """Returns information about a specific file.

     # noqa: E501

    :param file_id: The ID of the file to use for this request.
    :type file_id: str

    :rtype: Union[OpenAIFile, Tuple[OpenAIFile, int], Tuple[OpenAIFile, int, Dict[str, str]]
    """
    return 'do some magic!'
