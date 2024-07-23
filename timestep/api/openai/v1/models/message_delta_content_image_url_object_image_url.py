from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model


class MessageDeltaContentImageUrlObjectImageUrl(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, url=None, detail='auto'):  # noqa: E501
        """MessageDeltaContentImageUrlObjectImageUrl - a model defined in OpenAPI

        :param url: The url of this MessageDeltaContentImageUrlObjectImageUrl.  # noqa: E501
        :type url: str
        :param detail: The detail of this MessageDeltaContentImageUrlObjectImageUrl.  # noqa: E501
        :type detail: str
        """
        self.openapi_types = {
            'url': str,
            'detail': str
        }

        self.attribute_map = {
            'url': 'url',
            'detail': 'detail'
        }

        self._url = url
        self._detail = detail

    @classmethod
    def from_dict(cls, dikt) -> 'MessageDeltaContentImageUrlObjectImageUrl':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MessageDeltaContentImageUrlObject_image_url of this MessageDeltaContentImageUrlObjectImageUrl.  # noqa: E501
        :rtype: MessageDeltaContentImageUrlObjectImageUrl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self) -> str:
        """Gets the url of this MessageDeltaContentImageUrlObjectImageUrl.

        The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.  # noqa: E501

        :return: The url of this MessageDeltaContentImageUrlObjectImageUrl.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this MessageDeltaContentImageUrlObjectImageUrl.

        The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.  # noqa: E501

        :param url: The url of this MessageDeltaContentImageUrlObjectImageUrl.
        :type url: str
        """

        self._url = url

    @property
    def detail(self) -> str:
        """Gets the detail of this MessageDeltaContentImageUrlObjectImageUrl.

        Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.  # noqa: E501

        :return: The detail of this MessageDeltaContentImageUrlObjectImageUrl.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail: str):
        """Sets the detail of this MessageDeltaContentImageUrlObjectImageUrl.

        Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.  # noqa: E501

        :param detail: The detail of this MessageDeltaContentImageUrlObjectImageUrl.
        :type detail: str
        """
        allowed_values = ["auto", "low", "high"]  # noqa: E501
        if detail not in allowed_values:
            raise ValueError(
                "Invalid value for `detail` ({0}), must be one of {1}"
                .format(detail, allowed_values)
            )

        self._detail = detail
