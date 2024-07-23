from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.assistant_tools_code import \
    AssistantToolsCode  # noqa: E501
from timestep.api.openai.v1.models.assistant_tools_file_search_type_only import \
    AssistantToolsFileSearchTypeOnly  # noqa: E501
from timestep.api.openai.v1.models.base_model import Model


class MessageObjectAttachmentsInnerToolsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None):  # noqa: E501
        """MessageObjectAttachmentsInnerToolsInner - a model defined in OpenAPI

        :param type: The type of this MessageObjectAttachmentsInnerToolsInner.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'type': str
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'MessageObjectAttachmentsInnerToolsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MessageObject_attachments_inner_tools_inner of this MessageObjectAttachmentsInnerToolsInner.  # noqa: E501
        :rtype: MessageObjectAttachmentsInnerToolsInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this MessageObjectAttachmentsInnerToolsInner.

        The type of tool being defined: `code_interpreter`  # noqa: E501

        :return: The type of this MessageObjectAttachmentsInnerToolsInner.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this MessageObjectAttachmentsInnerToolsInner.

        The type of tool being defined: `code_interpreter`  # noqa: E501

        :param type: The type of this MessageObjectAttachmentsInnerToolsInner.
        :type type: str
        """
        allowed_values = ["code_interpreter", "file_search"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
