from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.message_delta_content_text_object_text_annotations_inner import \
    MessageDeltaContentTextObjectTextAnnotationsInner  # noqa: E501


class MessageDeltaContentTextObjectText(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, annotations=None):  # noqa: E501
        """MessageDeltaContentTextObjectText - a model defined in OpenAPI

        :param value: The value of this MessageDeltaContentTextObjectText.  # noqa: E501
        :type value: str
        :param annotations: The annotations of this MessageDeltaContentTextObjectText.  # noqa: E501
        :type annotations: List[MessageDeltaContentTextObjectTextAnnotationsInner]
        """
        self.openapi_types = {
            'value': str,
            'annotations': List[MessageDeltaContentTextObjectTextAnnotationsInner]
        }

        self.attribute_map = {
            'value': 'value',
            'annotations': 'annotations'
        }

        self._value = value
        self._annotations = annotations

    @classmethod
    def from_dict(cls, dikt) -> 'MessageDeltaContentTextObjectText':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MessageDeltaContentTextObject_text of this MessageDeltaContentTextObjectText.  # noqa: E501
        :rtype: MessageDeltaContentTextObjectText
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this MessageDeltaContentTextObjectText.

        The data that makes up the text.  # noqa: E501

        :return: The value of this MessageDeltaContentTextObjectText.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this MessageDeltaContentTextObjectText.

        The data that makes up the text.  # noqa: E501

        :param value: The value of this MessageDeltaContentTextObjectText.
        :type value: str
        """

        self._value = value

    @property
    def annotations(self) -> List[MessageDeltaContentTextObjectTextAnnotationsInner]:
        """Gets the annotations of this MessageDeltaContentTextObjectText.


        :return: The annotations of this MessageDeltaContentTextObjectText.
        :rtype: List[MessageDeltaContentTextObjectTextAnnotationsInner]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations: List[MessageDeltaContentTextObjectTextAnnotationsInner]):
        """Sets the annotations of this MessageDeltaContentTextObjectText.


        :param annotations: The annotations of this MessageDeltaContentTextObjectText.
        :type annotations: List[MessageDeltaContentTextObjectTextAnnotationsInner]
        """

        self._annotations = annotations
