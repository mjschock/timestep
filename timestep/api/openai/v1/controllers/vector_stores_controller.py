from typing import Dict, Tuple, Union

import connexion

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.create_vector_store_file_batch_request import (  # noqa: E501
    CreateVectorStoreFileBatchRequest,
)
from timestep.api.openai.v1.models.create_vector_store_file_request import (  # noqa: E501
    CreateVectorStoreFileRequest,
)
from timestep.api.openai.v1.models.create_vector_store_request import (  # noqa: E501
    CreateVectorStoreRequest,
)
from timestep.api.openai.v1.models.delete_vector_store_file_response import (  # noqa: E501
    DeleteVectorStoreFileResponse,
)
from timestep.api.openai.v1.models.delete_vector_store_response import (  # noqa: E501
    DeleteVectorStoreResponse,
)
from timestep.api.openai.v1.models.list_vector_store_files_response import (  # noqa: E501
    ListVectorStoreFilesResponse,
)
from timestep.api.openai.v1.models.list_vector_stores_response import (  # noqa: E501
    ListVectorStoresResponse,
)
from timestep.api.openai.v1.models.update_vector_store_request import (  # noqa: E501
    UpdateVectorStoreRequest,
)
from timestep.api.openai.v1.models.vector_store_file_batch_object import (  # noqa: E501
    VectorStoreFileBatchObject,
)
from timestep.api.openai.v1.models.vector_store_file_object import (  # noqa: E501
    VectorStoreFileObject,
)
from timestep.api.openai.v1.models.vector_store_object import (  # noqa: E501
    VectorStoreObject,
)


def cancel_vector_store_file_batch(vector_store_id, batch_id):  # noqa: E501
    """Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

     # noqa: E501

    :param vector_store_id: The ID of the vector store that the file batch belongs to.
    :type vector_store_id: str
    :param batch_id: The ID of the file batch to cancel.
    :type batch_id: str

    :rtype: Union[VectorStoreFileBatchObject, Tuple[VectorStoreFileBatchObject, int], Tuple[VectorStoreFileBatchObject, int, Dict[str, str]]
    """
    raise NotImplementedError


def create_vector_store(create_vector_store_request):  # noqa: E501
    """Create a vector store.

     # noqa: E501

    :param create_vector_store_request:
    :type create_vector_store_request: dict | bytes

    :rtype: Union[VectorStoreObject, Tuple[VectorStoreObject, int], Tuple[VectorStoreObject, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_vector_store_request = CreateVectorStoreRequest.from_dict(
            connexion.request.get_json()
        )  # noqa: E501
    raise NotImplementedError


def create_vector_store_file(
    vector_store_id, create_vector_store_file_request
):  # noqa: E501
    """Create a vector store file by attaching a [File](/docs/api-reference/files) to a [vector store](/docs/api-reference/vector-stores/object).

     # noqa: E501

    :param vector_store_id: The ID of the vector store for which to create a File.
    :type vector_store_id: str
    :param create_vector_store_file_request:
    :type create_vector_store_file_request: dict | bytes

    :rtype: Union[VectorStoreFileObject, Tuple[VectorStoreFileObject, int], Tuple[VectorStoreFileObject, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_vector_store_file_request = CreateVectorStoreFileRequest.from_dict(
            connexion.request.get_json()
        )  # noqa: E501
    raise NotImplementedError


def create_vector_store_file_batch(
    vector_store_id, create_vector_store_file_batch_request
):  # noqa: E501
    """Create a vector store file batch.

     # noqa: E501

    :param vector_store_id: The ID of the vector store for which to create a File Batch.
    :type vector_store_id: str
    :param create_vector_store_file_batch_request:
    :type create_vector_store_file_batch_request: dict | bytes

    :rtype: Union[VectorStoreFileBatchObject, Tuple[VectorStoreFileBatchObject, int], Tuple[VectorStoreFileBatchObject, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_vector_store_file_batch_request = (
            CreateVectorStoreFileBatchRequest.from_dict(connexion.request.get_json())
        )  # noqa: E501
    raise NotImplementedError


def delete_vector_store(vector_store_id):  # noqa: E501
    """Delete a vector store.

     # noqa: E501

    :param vector_store_id: The ID of the vector store to delete.
    :type vector_store_id: str

    :rtype: Union[DeleteVectorStoreResponse, Tuple[DeleteVectorStoreResponse, int], Tuple[DeleteVectorStoreResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


def delete_vector_store_file(vector_store_id, file_id):  # noqa: E501
    """Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](/docs/api-reference/files/delete) endpoint.

     # noqa: E501

    :param vector_store_id: The ID of the vector store that the file belongs to.
    :type vector_store_id: str
    :param file_id: The ID of the file to delete.
    :type file_id: str

    :rtype: Union[DeleteVectorStoreFileResponse, Tuple[DeleteVectorStoreFileResponse, int], Tuple[DeleteVectorStoreFileResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


def get_vector_store(vector_store_id):  # noqa: E501
    """Retrieves a vector store.

     # noqa: E501

    :param vector_store_id: The ID of the vector store to retrieve.
    :type vector_store_id: str

    :rtype: Union[VectorStoreObject, Tuple[VectorStoreObject, int], Tuple[VectorStoreObject, int, Dict[str, str]]
    """
    raise NotImplementedError


def get_vector_store_file(vector_store_id, file_id):  # noqa: E501
    """Retrieves a vector store file.

     # noqa: E501

    :param vector_store_id: The ID of the vector store that the file belongs to.
    :type vector_store_id: str
    :param file_id: The ID of the file being retrieved.
    :type file_id: str

    :rtype: Union[VectorStoreFileObject, Tuple[VectorStoreFileObject, int], Tuple[VectorStoreFileObject, int, Dict[str, str]]
    """
    raise NotImplementedError


def get_vector_store_file_batch(vector_store_id, batch_id):  # noqa: E501
    """Retrieves a vector store file batch.

     # noqa: E501

    :param vector_store_id: The ID of the vector store that the file batch belongs to.
    :type vector_store_id: str
    :param batch_id: The ID of the file batch being retrieved.
    :type batch_id: str

    :rtype: Union[VectorStoreFileBatchObject, Tuple[VectorStoreFileBatchObject, int], Tuple[VectorStoreFileBatchObject, int, Dict[str, str]]
    """
    raise NotImplementedError


def list_files_in_vector_store_batch(
    vector_store_id,
    batch_id,
    limit=None,
    order=None,
    after=None,
    before=None,
    filter=None,
):  # noqa: E501
    """Returns a list of vector store files in a batch.

     # noqa: E501

    :param vector_store_id: The ID of the vector store that the files belong to.
    :type vector_store_id: str
    :param batch_id: The ID of the file batch that the files belong to.
    :type batch_id: str
    :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.
    :type limit: int
    :param order: Sort order by the &#x60;created_at&#x60; timestamp of the objects. &#x60;asc&#x60; for ascending order and &#x60;desc&#x60; for descending order.
    :type order: str
    :param after: A cursor for use in pagination. &#x60;after&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after&#x3D;obj_foo in order to fetch the next page of the list.
    :type after: str
    :param before: A cursor for use in pagination. &#x60;before&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before&#x3D;obj_foo in order to fetch the previous page of the list.
    :type before: str
    :param filter: Filter by file status. One of &#x60;in_progress&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, &#x60;cancelled&#x60;.
    :type filter: str

    :rtype: Union[ListVectorStoreFilesResponse, Tuple[ListVectorStoreFilesResponse, int], Tuple[ListVectorStoreFilesResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


def list_vector_store_files(
    vector_store_id, limit=None, order=None, after=None, before=None, filter=None
):  # noqa: E501
    """Returns a list of vector store files.

     # noqa: E501

    :param vector_store_id: The ID of the vector store that the files belong to.
    :type vector_store_id: str
    :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.
    :type limit: int
    :param order: Sort order by the &#x60;created_at&#x60; timestamp of the objects. &#x60;asc&#x60; for ascending order and &#x60;desc&#x60; for descending order.
    :type order: str
    :param after: A cursor for use in pagination. &#x60;after&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after&#x3D;obj_foo in order to fetch the next page of the list.
    :type after: str
    :param before: A cursor for use in pagination. &#x60;before&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before&#x3D;obj_foo in order to fetch the previous page of the list.
    :type before: str
    :param filter: Filter by file status. One of &#x60;in_progress&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, &#x60;cancelled&#x60;.
    :type filter: str

    :rtype: Union[ListVectorStoreFilesResponse, Tuple[ListVectorStoreFilesResponse, int], Tuple[ListVectorStoreFilesResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


def list_vector_stores(limit=None, order=None, after=None, before=None):  # noqa: E501
    """Returns a list of vector stores.

     # noqa: E501

    :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.
    :type limit: int
    :param order: Sort order by the &#x60;created_at&#x60; timestamp of the objects. &#x60;asc&#x60; for ascending order and &#x60;desc&#x60; for descending order.
    :type order: str
    :param after: A cursor for use in pagination. &#x60;after&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after&#x3D;obj_foo in order to fetch the next page of the list.
    :type after: str
    :param before: A cursor for use in pagination. &#x60;before&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before&#x3D;obj_foo in order to fetch the previous page of the list.
    :type before: str

    :rtype: Union[ListVectorStoresResponse, Tuple[ListVectorStoresResponse, int], Tuple[ListVectorStoresResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


def modify_vector_store(vector_store_id, update_vector_store_request):  # noqa: E501
    """Modifies a vector store.

     # noqa: E501

    :param vector_store_id: The ID of the vector store to modify.
    :type vector_store_id: str
    :param update_vector_store_request:
    :type update_vector_store_request: dict | bytes

    :rtype: Union[VectorStoreObject, Tuple[VectorStoreObject, int], Tuple[VectorStoreObject, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_vector_store_request = UpdateVectorStoreRequest.from_dict(
            connexion.request.get_json()
        )  # noqa: E501
    raise NotImplementedError
