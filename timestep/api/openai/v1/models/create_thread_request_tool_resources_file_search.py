from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.create_thread_request_tool_resources_file_search_vector_stores_inner import \
    CreateThreadRequestToolResourcesFileSearchVectorStoresInner  # noqa: E501


class CreateThreadRequestToolResourcesFileSearch(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, vector_store_ids=None, vector_stores=None):  # noqa: E501
        """CreateThreadRequestToolResourcesFileSearch - a model defined in OpenAPI

        :param vector_store_ids: The vector_store_ids of this CreateThreadRequestToolResourcesFileSearch.  # noqa: E501
        :type vector_store_ids: List[str]
        :param vector_stores: The vector_stores of this CreateThreadRequestToolResourcesFileSearch.  # noqa: E501
        :type vector_stores: List[CreateThreadRequestToolResourcesFileSearchVectorStoresInner]
        """
        self.openapi_types = {
            'vector_store_ids': List[str],
            'vector_stores': List[CreateThreadRequestToolResourcesFileSearchVectorStoresInner]
        }

        self.attribute_map = {
            'vector_store_ids': 'vector_store_ids',
            'vector_stores': 'vector_stores'
        }

        self._vector_store_ids = vector_store_ids
        self._vector_stores = vector_stores

    @classmethod
    def from_dict(cls, dikt) -> 'CreateThreadRequestToolResourcesFileSearch':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateThreadRequest_tool_resources_file_search of this CreateThreadRequestToolResourcesFileSearch.  # noqa: E501
        :rtype: CreateThreadRequestToolResourcesFileSearch
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vector_store_ids(self) -> List[str]:
        """Gets the vector_store_ids of this CreateThreadRequestToolResourcesFileSearch.

        The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.   # noqa: E501

        :return: The vector_store_ids of this CreateThreadRequestToolResourcesFileSearch.
        :rtype: List[str]
        """
        return self._vector_store_ids

    @vector_store_ids.setter
    def vector_store_ids(self, vector_store_ids: List[str]):
        """Sets the vector_store_ids of this CreateThreadRequestToolResourcesFileSearch.

        The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.   # noqa: E501

        :param vector_store_ids: The vector_store_ids of this CreateThreadRequestToolResourcesFileSearch.
        :type vector_store_ids: List[str]
        """
        if vector_store_ids is not None and len(vector_store_ids) > 1:
            raise ValueError("Invalid value for `vector_store_ids`, number of items must be less than or equal to `1`")  # noqa: E501

        self._vector_store_ids = vector_store_ids

    @property
    def vector_stores(self) -> List[CreateThreadRequestToolResourcesFileSearchVectorStoresInner]:
        """Gets the vector_stores of this CreateThreadRequestToolResourcesFileSearch.

        A helper to create a [vector store](/docs/api-reference/vector-stores/object) with file_ids and attach it to this thread. There can be a maximum of 1 vector store attached to the thread.   # noqa: E501

        :return: The vector_stores of this CreateThreadRequestToolResourcesFileSearch.
        :rtype: List[CreateThreadRequestToolResourcesFileSearchVectorStoresInner]
        """
        return self._vector_stores

    @vector_stores.setter
    def vector_stores(self, vector_stores: List[CreateThreadRequestToolResourcesFileSearchVectorStoresInner]):
        """Sets the vector_stores of this CreateThreadRequestToolResourcesFileSearch.

        A helper to create a [vector store](/docs/api-reference/vector-stores/object) with file_ids and attach it to this thread. There can be a maximum of 1 vector store attached to the thread.   # noqa: E501

        :param vector_stores: The vector_stores of this CreateThreadRequestToolResourcesFileSearch.
        :type vector_stores: List[CreateThreadRequestToolResourcesFileSearchVectorStoresInner]
        """
        if vector_stores is not None and len(vector_stores) > 1:
            raise ValueError("Invalid value for `vector_stores`, number of items must be less than or equal to `1`")  # noqa: E501

        self._vector_stores = vector_stores