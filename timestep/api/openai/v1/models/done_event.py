from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model


class DoneEvent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, event=None, data=None):  # noqa: E501
        """DoneEvent - a model defined in OpenAPI

        :param event: The event of this DoneEvent.  # noqa: E501
        :type event: str
        :param data: The data of this DoneEvent.  # noqa: E501
        :type data: str
        """
        self.openapi_types = {
            'event': str,
            'data': str
        }

        self.attribute_map = {
            'event': 'event',
            'data': 'data'
        }

        self._event = event
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'DoneEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DoneEvent of this DoneEvent.  # noqa: E501
        :rtype: DoneEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event(self) -> str:
        """Gets the event of this DoneEvent.


        :return: The event of this DoneEvent.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event: str):
        """Sets the event of this DoneEvent.


        :param event: The event of this DoneEvent.
        :type event: str
        """
        allowed_values = ["done"]  # noqa: E501
        if event not in allowed_values:
            raise ValueError(
                "Invalid value for `event` ({0}), must be one of {1}"
                .format(event, allowed_values)
            )

        self._event = event

    @property
    def data(self) -> str:
        """Gets the data of this DoneEvent.


        :return: The data of this DoneEvent.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data: str):
        """Sets the data of this DoneEvent.


        :param data: The data of this DoneEvent.
        :type data: str
        """
        allowed_values = ["[DONE]"]  # noqa: E501
        if data not in allowed_values:
            raise ValueError(
                "Invalid value for `data` ({0}), must be one of {1}"
                .format(data, allowed_values)
            )

        self._data = data