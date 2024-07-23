from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.run_object import RunObject  # noqa: E501


class RunStreamEventOneOf5(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, event=None, data=None):  # noqa: E501
        """RunStreamEventOneOf5 - a model defined in OpenAPI

        :param event: The event of this RunStreamEventOneOf5.  # noqa: E501
        :type event: str
        :param data: The data of this RunStreamEventOneOf5.  # noqa: E501
        :type data: RunObject
        """
        self.openapi_types = {
            'event': str,
            'data': RunObject
        }

        self.attribute_map = {
            'event': 'event',
            'data': 'data'
        }

        self._event = event
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'RunStreamEventOneOf5':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RunStreamEvent_oneOf_5 of this RunStreamEventOneOf5.  # noqa: E501
        :rtype: RunStreamEventOneOf5
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event(self) -> str:
        """Gets the event of this RunStreamEventOneOf5.


        :return: The event of this RunStreamEventOneOf5.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event: str):
        """Sets the event of this RunStreamEventOneOf5.


        :param event: The event of this RunStreamEventOneOf5.
        :type event: str
        """
        allowed_values = ["thread.run.incomplete"]  # noqa: E501
        if event not in allowed_values:
            raise ValueError(
                "Invalid value for `event` ({0}), must be one of {1}"
                .format(event, allowed_values)
            )

        self._event = event

    @property
    def data(self) -> RunObject:
        """Gets the data of this RunStreamEventOneOf5.


        :return: The data of this RunStreamEventOneOf5.
        :rtype: RunObject
        """
        return self._data

    @data.setter
    def data(self, data: RunObject):
        """Sets the data of this RunStreamEventOneOf5.


        :param data: The data of this RunStreamEventOneOf5.
        :type data: RunObject
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data
