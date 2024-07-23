from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.create_assistant_request_tool_resources_file_search_vector_stores_inner_chunking_strategy import \
    CreateAssistantRequestToolResourcesFileSearchVectorStoresInnerChunkingStrategy  # noqa: E501


class CreateAssistantRequestToolResourcesFileSearchVectorStoresInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_ids=None, chunking_strategy=None, metadata=None):  # noqa: E501
        """CreateAssistantRequestToolResourcesFileSearchVectorStoresInner - a model defined in OpenAPI

        :param file_ids: The file_ids of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.  # noqa: E501
        :type file_ids: List[str]
        :param chunking_strategy: The chunking_strategy of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.  # noqa: E501
        :type chunking_strategy: CreateAssistantRequestToolResourcesFileSearchVectorStoresInnerChunkingStrategy
        :param metadata: The metadata of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.  # noqa: E501
        :type metadata: object
        """
        self.openapi_types = {
            'file_ids': List[str],
            'chunking_strategy': CreateAssistantRequestToolResourcesFileSearchVectorStoresInnerChunkingStrategy,
            'metadata': object
        }

        self.attribute_map = {
            'file_ids': 'file_ids',
            'chunking_strategy': 'chunking_strategy',
            'metadata': 'metadata'
        }

        self._file_ids = file_ids
        self._chunking_strategy = chunking_strategy
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'CreateAssistantRequestToolResourcesFileSearchVectorStoresInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateAssistantRequest_tool_resources_file_search_vector_stores_inner of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.  # noqa: E501
        :rtype: CreateAssistantRequestToolResourcesFileSearchVectorStoresInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_ids(self) -> List[str]:
        """Gets the file_ids of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.

        A list of [file](/docs/api-reference/files) IDs to add to the vector store. There can be a maximum of 10000 files in a vector store.   # noqa: E501

        :return: The file_ids of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.
        :rtype: List[str]
        """
        return self._file_ids

    @file_ids.setter
    def file_ids(self, file_ids: List[str]):
        """Sets the file_ids of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.

        A list of [file](/docs/api-reference/files) IDs to add to the vector store. There can be a maximum of 10000 files in a vector store.   # noqa: E501

        :param file_ids: The file_ids of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.
        :type file_ids: List[str]
        """
        if file_ids is not None and len(file_ids) > 10000:
            raise ValueError("Invalid value for `file_ids`, number of items must be less than or equal to `10000`")  # noqa: E501

        self._file_ids = file_ids

    @property
    def chunking_strategy(self) -> CreateAssistantRequestToolResourcesFileSearchVectorStoresInnerChunkingStrategy:
        """Gets the chunking_strategy of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.


        :return: The chunking_strategy of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.
        :rtype: CreateAssistantRequestToolResourcesFileSearchVectorStoresInnerChunkingStrategy
        """
        return self._chunking_strategy

    @chunking_strategy.setter
    def chunking_strategy(self, chunking_strategy: CreateAssistantRequestToolResourcesFileSearchVectorStoresInnerChunkingStrategy):
        """Sets the chunking_strategy of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.


        :param chunking_strategy: The chunking_strategy of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.
        :type chunking_strategy: CreateAssistantRequestToolResourcesFileSearchVectorStoresInnerChunkingStrategy
        """

        self._chunking_strategy = chunking_strategy

    @property
    def metadata(self) -> object:
        """Gets the metadata of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.

        Set of 16 key-value pairs that can be attached to a vector store. This can be useful for storing additional information about the vector store in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.   # noqa: E501

        :return: The metadata of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: object):
        """Sets the metadata of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.

        Set of 16 key-value pairs that can be attached to a vector store. This can be useful for storing additional information about the vector store in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.   # noqa: E501

        :param metadata: The metadata of this CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.
        :type metadata: object
        """

        self._metadata = metadata