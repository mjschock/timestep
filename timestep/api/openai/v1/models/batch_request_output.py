from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.batch_request_output_error import \
    BatchRequestOutputError  # noqa: E501
from timestep.api.openai.v1.models.batch_request_output_response import \
    BatchRequestOutputResponse  # noqa: E501


class BatchRequestOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, custom_id=None, response=None, error=None):  # noqa: E501
        """BatchRequestOutput - a model defined in OpenAPI

        :param id: The id of this BatchRequestOutput.  # noqa: E501
        :type id: str
        :param custom_id: The custom_id of this BatchRequestOutput.  # noqa: E501
        :type custom_id: str
        :param response: The response of this BatchRequestOutput.  # noqa: E501
        :type response: BatchRequestOutputResponse
        :param error: The error of this BatchRequestOutput.  # noqa: E501
        :type error: BatchRequestOutputError
        """
        self.openapi_types = {
            'id': str,
            'custom_id': str,
            'response': BatchRequestOutputResponse,
            'error': BatchRequestOutputError
        }

        self.attribute_map = {
            'id': 'id',
            'custom_id': 'custom_id',
            'response': 'response',
            'error': 'error'
        }

        self._id = id
        self._custom_id = custom_id
        self._response = response
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'BatchRequestOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BatchRequestOutput of this BatchRequestOutput.  # noqa: E501
        :rtype: BatchRequestOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this BatchRequestOutput.


        :return: The id of this BatchRequestOutput.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this BatchRequestOutput.


        :param id: The id of this BatchRequestOutput.
        :type id: str
        """

        self._id = id

    @property
    def custom_id(self) -> str:
        """Gets the custom_id of this BatchRequestOutput.

        A developer-provided per-request id that will be used to match outputs to inputs.  # noqa: E501

        :return: The custom_id of this BatchRequestOutput.
        :rtype: str
        """
        return self._custom_id

    @custom_id.setter
    def custom_id(self, custom_id: str):
        """Sets the custom_id of this BatchRequestOutput.

        A developer-provided per-request id that will be used to match outputs to inputs.  # noqa: E501

        :param custom_id: The custom_id of this BatchRequestOutput.
        :type custom_id: str
        """

        self._custom_id = custom_id

    @property
    def response(self) -> BatchRequestOutputResponse:
        """Gets the response of this BatchRequestOutput.


        :return: The response of this BatchRequestOutput.
        :rtype: BatchRequestOutputResponse
        """
        return self._response

    @response.setter
    def response(self, response: BatchRequestOutputResponse):
        """Sets the response of this BatchRequestOutput.


        :param response: The response of this BatchRequestOutput.
        :type response: BatchRequestOutputResponse
        """

        self._response = response

    @property
    def error(self) -> BatchRequestOutputError:
        """Gets the error of this BatchRequestOutput.


        :return: The error of this BatchRequestOutput.
        :rtype: BatchRequestOutputError
        """
        return self._error

    @error.setter
    def error(self, error: BatchRequestOutputError):
        """Sets the error of this BatchRequestOutput.


        :param error: The error of this BatchRequestOutput.
        :type error: BatchRequestOutputError
        """

        self._error = error