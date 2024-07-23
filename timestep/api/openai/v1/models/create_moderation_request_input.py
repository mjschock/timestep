from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model


class CreateModerationRequestInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """CreateModerationRequestInput - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'CreateModerationRequestInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateModerationRequest_input of this CreateModerationRequestInput.  # noqa: E501
        :rtype: CreateModerationRequestInput
        """
        return util.deserialize_model(dikt, cls)
