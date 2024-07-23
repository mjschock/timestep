from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model


class ThreadObjectToolResourcesFileSearch(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, vector_store_ids=None):  # noqa: E501
        """ThreadObjectToolResourcesFileSearch - a model defined in OpenAPI

        :param vector_store_ids: The vector_store_ids of this ThreadObjectToolResourcesFileSearch.  # noqa: E501
        :type vector_store_ids: List[str]
        """
        self.openapi_types = {
            'vector_store_ids': List[str]
        }

        self.attribute_map = {
            'vector_store_ids': 'vector_store_ids'
        }

        self._vector_store_ids = vector_store_ids

    @classmethod
    def from_dict(cls, dikt) -> 'ThreadObjectToolResourcesFileSearch':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ThreadObject_tool_resources_file_search of this ThreadObjectToolResourcesFileSearch.  # noqa: E501
        :rtype: ThreadObjectToolResourcesFileSearch
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vector_store_ids(self) -> List[str]:
        """Gets the vector_store_ids of this ThreadObjectToolResourcesFileSearch.

        The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.   # noqa: E501

        :return: The vector_store_ids of this ThreadObjectToolResourcesFileSearch.
        :rtype: List[str]
        """
        return self._vector_store_ids

    @vector_store_ids.setter
    def vector_store_ids(self, vector_store_ids: List[str]):
        """Sets the vector_store_ids of this ThreadObjectToolResourcesFileSearch.

        The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.   # noqa: E501

        :param vector_store_ids: The vector_store_ids of this ThreadObjectToolResourcesFileSearch.
        :type vector_store_ids: List[str]
        """
        if vector_store_ids is not None and len(vector_store_ids) > 1:
            raise ValueError("Invalid value for `vector_store_ids`, number of items must be less than or equal to `1`")  # noqa: E501

        self._vector_store_ids = vector_store_ids
