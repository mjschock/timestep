from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.ap.v1 import util
from timestep.api.ap.v1.models.base_model import Model
from timestep.api.ap.v1.models.pagination import Pagination  # noqa: E501
from timestep.api.ap.v1.models.step import Step  # noqa: E501


class TaskStepsListResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, steps=None, pagination=None):  # noqa: E501
        """TaskStepsListResponse - a model defined in OpenAPI

        :param steps: The steps of this TaskStepsListResponse.  # noqa: E501
        :type steps: List[Step]
        :param pagination: The pagination of this TaskStepsListResponse.  # noqa: E501
        :type pagination: Pagination
        """
        self.openapi_types = {
            'steps': List[Step],
            'pagination': Pagination
        }

        self.attribute_map = {
            'steps': 'steps',
            'pagination': 'pagination'
        }

        self._steps = steps
        self._pagination = pagination

    @classmethod
    def from_dict(cls, dikt) -> 'TaskStepsListResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TaskStepsListResponse of this TaskStepsListResponse.  # noqa: E501
        :rtype: TaskStepsListResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def steps(self) -> List[Step]:
        """Gets the steps of this TaskStepsListResponse.


        :return: The steps of this TaskStepsListResponse.
        :rtype: List[Step]
        """
        return self._steps

    @steps.setter
    def steps(self, steps: List[Step]):
        """Sets the steps of this TaskStepsListResponse.


        :param steps: The steps of this TaskStepsListResponse.
        :type steps: List[Step]
        """
        if steps is None:
            raise ValueError("Invalid value for `steps`, must not be `None`")  # noqa: E501

        self._steps = steps

    @property
    def pagination(self) -> Pagination:
        """Gets the pagination of this TaskStepsListResponse.


        :return: The pagination of this TaskStepsListResponse.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination: Pagination):
        """Sets the pagination of this TaskStepsListResponse.


        :param pagination: The pagination of this TaskStepsListResponse.
        :type pagination: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")  # noqa: E501

        self._pagination = pagination
