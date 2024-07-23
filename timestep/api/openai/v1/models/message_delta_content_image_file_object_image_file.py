from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model


class MessageDeltaContentImageFileObjectImageFile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_id=None, detail='auto'):  # noqa: E501
        """MessageDeltaContentImageFileObjectImageFile - a model defined in OpenAPI

        :param file_id: The file_id of this MessageDeltaContentImageFileObjectImageFile.  # noqa: E501
        :type file_id: str
        :param detail: The detail of this MessageDeltaContentImageFileObjectImageFile.  # noqa: E501
        :type detail: str
        """
        self.openapi_types = {
            'file_id': str,
            'detail': str
        }

        self.attribute_map = {
            'file_id': 'file_id',
            'detail': 'detail'
        }

        self._file_id = file_id
        self._detail = detail

    @classmethod
    def from_dict(cls, dikt) -> 'MessageDeltaContentImageFileObjectImageFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MessageDeltaContentImageFileObject_image_file of this MessageDeltaContentImageFileObjectImageFile.  # noqa: E501
        :rtype: MessageDeltaContentImageFileObjectImageFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_id(self) -> str:
        """Gets the file_id of this MessageDeltaContentImageFileObjectImageFile.

        The [File](/docs/api-reference/files) ID of the image in the message content. Set `purpose=\"vision\"` when uploading the File if you need to later display the file content.  # noqa: E501

        :return: The file_id of this MessageDeltaContentImageFileObjectImageFile.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id: str):
        """Sets the file_id of this MessageDeltaContentImageFileObjectImageFile.

        The [File](/docs/api-reference/files) ID of the image in the message content. Set `purpose=\"vision\"` when uploading the File if you need to later display the file content.  # noqa: E501

        :param file_id: The file_id of this MessageDeltaContentImageFileObjectImageFile.
        :type file_id: str
        """

        self._file_id = file_id

    @property
    def detail(self) -> str:
        """Gets the detail of this MessageDeltaContentImageFileObjectImageFile.

        Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.  # noqa: E501

        :return: The detail of this MessageDeltaContentImageFileObjectImageFile.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail: str):
        """Sets the detail of this MessageDeltaContentImageFileObjectImageFile.

        Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.  # noqa: E501

        :param detail: The detail of this MessageDeltaContentImageFileObjectImageFile.
        :type detail: str
        """
        allowed_values = ["auto", "low", "high"]  # noqa: E501
        if detail not in allowed_values:
            raise ValueError(
                "Invalid value for `detail` ({0}), must be one of {1}"
                .format(detail, allowed_values)
            )

        self._detail = detail