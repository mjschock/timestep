from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.create_moderation_request_input import \
    CreateModerationRequestInput  # noqa: E501
from timestep.api.openai.v1.models.create_moderation_request_model import \
    CreateModerationRequestModel  # noqa: E501


class CreateModerationRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input=None, model=None):  # noqa: E501
        """CreateModerationRequest - a model defined in OpenAPI

        :param input: The input of this CreateModerationRequest.  # noqa: E501
        :type input: CreateModerationRequestInput
        :param model: The model of this CreateModerationRequest.  # noqa: E501
        :type model: CreateModerationRequestModel
        """
        self.openapi_types = {
            'input': CreateModerationRequestInput,
            'model': CreateModerationRequestModel
        }

        self.attribute_map = {
            'input': 'input',
            'model': 'model'
        }

        self._input = input
        self._model = model

    @classmethod
    def from_dict(cls, dikt) -> 'CreateModerationRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateModerationRequest of this CreateModerationRequest.  # noqa: E501
        :rtype: CreateModerationRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self) -> CreateModerationRequestInput:
        """Gets the input of this CreateModerationRequest.


        :return: The input of this CreateModerationRequest.
        :rtype: CreateModerationRequestInput
        """
        return self._input

    @input.setter
    def input(self, input: CreateModerationRequestInput):
        """Sets the input of this CreateModerationRequest.


        :param input: The input of this CreateModerationRequest.
        :type input: CreateModerationRequestInput
        """
        if input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input

    @property
    def model(self) -> CreateModerationRequestModel:
        """Gets the model of this CreateModerationRequest.


        :return: The model of this CreateModerationRequest.
        :rtype: CreateModerationRequestModel
        """
        return self._model

    @model.setter
    def model(self, model: CreateModerationRequestModel):
        """Sets the model of this CreateModerationRequest.


        :param model: The model of this CreateModerationRequest.
        :type model: CreateModerationRequestModel
        """

        self._model = model
