from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.fine_tuning_job import \
    FineTuningJob  # noqa: E501


class ListPaginatedFineTuningJobsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None, has_more=None, object=None):  # noqa: E501
        """ListPaginatedFineTuningJobsResponse - a model defined in OpenAPI

        :param data: The data of this ListPaginatedFineTuningJobsResponse.  # noqa: E501
        :type data: List[FineTuningJob]
        :param has_more: The has_more of this ListPaginatedFineTuningJobsResponse.  # noqa: E501
        :type has_more: bool
        :param object: The object of this ListPaginatedFineTuningJobsResponse.  # noqa: E501
        :type object: str
        """
        self.openapi_types = {
            'data': List[FineTuningJob],
            'has_more': bool,
            'object': str
        }

        self.attribute_map = {
            'data': 'data',
            'has_more': 'has_more',
            'object': 'object'
        }

        self._data = data
        self._has_more = has_more
        self._object = object

    @classmethod
    def from_dict(cls, dikt) -> 'ListPaginatedFineTuningJobsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListPaginatedFineTuningJobsResponse of this ListPaginatedFineTuningJobsResponse.  # noqa: E501
        :rtype: ListPaginatedFineTuningJobsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[FineTuningJob]:
        """Gets the data of this ListPaginatedFineTuningJobsResponse.


        :return: The data of this ListPaginatedFineTuningJobsResponse.
        :rtype: List[FineTuningJob]
        """
        return self._data

    @data.setter
    def data(self, data: List[FineTuningJob]):
        """Sets the data of this ListPaginatedFineTuningJobsResponse.


        :param data: The data of this ListPaginatedFineTuningJobsResponse.
        :type data: List[FineTuningJob]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def has_more(self) -> bool:
        """Gets the has_more of this ListPaginatedFineTuningJobsResponse.


        :return: The has_more of this ListPaginatedFineTuningJobsResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more: bool):
        """Sets the has_more of this ListPaginatedFineTuningJobsResponse.


        :param has_more: The has_more of this ListPaginatedFineTuningJobsResponse.
        :type has_more: bool
        """
        if has_more is None:
            raise ValueError("Invalid value for `has_more`, must not be `None`")  # noqa: E501

        self._has_more = has_more

    @property
    def object(self) -> str:
        """Gets the object of this ListPaginatedFineTuningJobsResponse.


        :return: The object of this ListPaginatedFineTuningJobsResponse.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object: str):
        """Sets the object of this ListPaginatedFineTuningJobsResponse.


        :param object: The object of this ListPaginatedFineTuningJobsResponse.
        :type object: str
        """
        allowed_values = ["list"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object
