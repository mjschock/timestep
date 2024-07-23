from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model


class BatchRequestCounts(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, total=None, completed=None, failed=None):  # noqa: E501
        """BatchRequestCounts - a model defined in OpenAPI

        :param total: The total of this BatchRequestCounts.  # noqa: E501
        :type total: int
        :param completed: The completed of this BatchRequestCounts.  # noqa: E501
        :type completed: int
        :param failed: The failed of this BatchRequestCounts.  # noqa: E501
        :type failed: int
        """
        self.openapi_types = {
            'total': int,
            'completed': int,
            'failed': int
        }

        self.attribute_map = {
            'total': 'total',
            'completed': 'completed',
            'failed': 'failed'
        }

        self._total = total
        self._completed = completed
        self._failed = failed

    @classmethod
    def from_dict(cls, dikt) -> 'BatchRequestCounts':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Batch_request_counts of this BatchRequestCounts.  # noqa: E501
        :rtype: BatchRequestCounts
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total(self) -> int:
        """Gets the total of this BatchRequestCounts.

        Total number of requests in the batch.  # noqa: E501

        :return: The total of this BatchRequestCounts.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int):
        """Sets the total of this BatchRequestCounts.

        Total number of requests in the batch.  # noqa: E501

        :param total: The total of this BatchRequestCounts.
        :type total: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def completed(self) -> int:
        """Gets the completed of this BatchRequestCounts.

        Number of requests that have been completed successfully.  # noqa: E501

        :return: The completed of this BatchRequestCounts.
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed: int):
        """Sets the completed of this BatchRequestCounts.

        Number of requests that have been completed successfully.  # noqa: E501

        :param completed: The completed of this BatchRequestCounts.
        :type completed: int
        """
        if completed is None:
            raise ValueError("Invalid value for `completed`, must not be `None`")  # noqa: E501

        self._completed = completed

    @property
    def failed(self) -> int:
        """Gets the failed of this BatchRequestCounts.

        Number of requests that have failed.  # noqa: E501

        :return: The failed of this BatchRequestCounts.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed: int):
        """Sets the failed of this BatchRequestCounts.

        Number of requests that have failed.  # noqa: E501

        :param failed: The failed of this BatchRequestCounts.
        :type failed: int
        """
        if failed is None:
            raise ValueError("Invalid value for `failed`, must not be `None`")  # noqa: E501

        self._failed = failed
