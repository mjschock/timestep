from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.chat_completion_request_message_content_part import \
    ChatCompletionRequestMessageContentPart  # noqa: E501


class ChatCompletionRequestUserMessageContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """ChatCompletionRequestUserMessageContent - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ChatCompletionRequestUserMessageContent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChatCompletionRequestUserMessage_content of this ChatCompletionRequestUserMessageContent.  # noqa: E501
        :rtype: ChatCompletionRequestUserMessageContent
        """
        return util.deserialize_model(dikt, cls)
