from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.message_content_image_file_object import \
    MessageContentImageFileObject  # noqa: E501
from timestep.api.openai.v1.models.message_content_image_file_object_image_file import \
    MessageContentImageFileObjectImageFile  # noqa: E501
from timestep.api.openai.v1.models.message_content_image_url_object import \
    MessageContentImageUrlObject  # noqa: E501
from timestep.api.openai.v1.models.message_content_image_url_object_image_url import \
    MessageContentImageUrlObjectImageUrl  # noqa: E501
from timestep.api.openai.v1.models.message_request_content_text_object import \
    MessageRequestContentTextObject  # noqa: E501


class ArrayOfContentPartsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, image_file=None, image_url=None, text=None):  # noqa: E501
        """ArrayOfContentPartsInner - a model defined in OpenAPI

        :param type: The type of this ArrayOfContentPartsInner.  # noqa: E501
        :type type: str
        :param image_file: The image_file of this ArrayOfContentPartsInner.  # noqa: E501
        :type image_file: MessageContentImageFileObjectImageFile
        :param image_url: The image_url of this ArrayOfContentPartsInner.  # noqa: E501
        :type image_url: MessageContentImageUrlObjectImageUrl
        :param text: The text of this ArrayOfContentPartsInner.  # noqa: E501
        :type text: str
        """
        self.openapi_types = {
            'type': str,
            'image_file': MessageContentImageFileObjectImageFile,
            'image_url': MessageContentImageUrlObjectImageUrl,
            'text': str
        }

        self.attribute_map = {
            'type': 'type',
            'image_file': 'image_file',
            'image_url': 'image_url',
            'text': 'text'
        }

        self._type = type
        self._image_file = image_file
        self._image_url = image_url
        self._text = text

    @classmethod
    def from_dict(cls, dikt) -> 'ArrayOfContentPartsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Array_of_content_parts_inner of this ArrayOfContentPartsInner.  # noqa: E501
        :rtype: ArrayOfContentPartsInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this ArrayOfContentPartsInner.

        Always `image_file`.  # noqa: E501

        :return: The type of this ArrayOfContentPartsInner.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ArrayOfContentPartsInner.

        Always `image_file`.  # noqa: E501

        :param type: The type of this ArrayOfContentPartsInner.
        :type type: str
        """
        allowed_values = ["image_file", "image_url", "text"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def image_file(self) -> MessageContentImageFileObjectImageFile:
        """Gets the image_file of this ArrayOfContentPartsInner.


        :return: The image_file of this ArrayOfContentPartsInner.
        :rtype: MessageContentImageFileObjectImageFile
        """
        return self._image_file

    @image_file.setter
    def image_file(self, image_file: MessageContentImageFileObjectImageFile):
        """Sets the image_file of this ArrayOfContentPartsInner.


        :param image_file: The image_file of this ArrayOfContentPartsInner.
        :type image_file: MessageContentImageFileObjectImageFile
        """
        if image_file is None:
            raise ValueError("Invalid value for `image_file`, must not be `None`")  # noqa: E501

        self._image_file = image_file

    @property
    def image_url(self) -> MessageContentImageUrlObjectImageUrl:
        """Gets the image_url of this ArrayOfContentPartsInner.


        :return: The image_url of this ArrayOfContentPartsInner.
        :rtype: MessageContentImageUrlObjectImageUrl
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url: MessageContentImageUrlObjectImageUrl):
        """Sets the image_url of this ArrayOfContentPartsInner.


        :param image_url: The image_url of this ArrayOfContentPartsInner.
        :type image_url: MessageContentImageUrlObjectImageUrl
        """
        if image_url is None:
            raise ValueError("Invalid value for `image_url`, must not be `None`")  # noqa: E501

        self._image_url = image_url

    @property
    def text(self) -> str:
        """Gets the text of this ArrayOfContentPartsInner.

        Text content to be sent to the model  # noqa: E501

        :return: The text of this ArrayOfContentPartsInner.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this ArrayOfContentPartsInner.

        Text content to be sent to the model  # noqa: E501

        :param text: The text of this ArrayOfContentPartsInner.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text