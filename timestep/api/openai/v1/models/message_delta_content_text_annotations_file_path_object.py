from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.message_delta_content_text_annotations_file_path_object_file_path import \
    MessageDeltaContentTextAnnotationsFilePathObjectFilePath  # noqa: E501


class MessageDeltaContentTextAnnotationsFilePathObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, index=None, type=None, text=None, file_path=None, start_index=None, end_index=None):  # noqa: E501
        """MessageDeltaContentTextAnnotationsFilePathObject - a model defined in OpenAPI

        :param index: The index of this MessageDeltaContentTextAnnotationsFilePathObject.  # noqa: E501
        :type index: int
        :param type: The type of this MessageDeltaContentTextAnnotationsFilePathObject.  # noqa: E501
        :type type: str
        :param text: The text of this MessageDeltaContentTextAnnotationsFilePathObject.  # noqa: E501
        :type text: str
        :param file_path: The file_path of this MessageDeltaContentTextAnnotationsFilePathObject.  # noqa: E501
        :type file_path: MessageDeltaContentTextAnnotationsFilePathObjectFilePath
        :param start_index: The start_index of this MessageDeltaContentTextAnnotationsFilePathObject.  # noqa: E501
        :type start_index: int
        :param end_index: The end_index of this MessageDeltaContentTextAnnotationsFilePathObject.  # noqa: E501
        :type end_index: int
        """
        self.openapi_types = {
            'index': int,
            'type': str,
            'text': str,
            'file_path': MessageDeltaContentTextAnnotationsFilePathObjectFilePath,
            'start_index': int,
            'end_index': int
        }

        self.attribute_map = {
            'index': 'index',
            'type': 'type',
            'text': 'text',
            'file_path': 'file_path',
            'start_index': 'start_index',
            'end_index': 'end_index'
        }

        self._index = index
        self._type = type
        self._text = text
        self._file_path = file_path
        self._start_index = start_index
        self._end_index = end_index

    @classmethod
    def from_dict(cls, dikt) -> 'MessageDeltaContentTextAnnotationsFilePathObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MessageDeltaContentTextAnnotationsFilePathObject of this MessageDeltaContentTextAnnotationsFilePathObject.  # noqa: E501
        :rtype: MessageDeltaContentTextAnnotationsFilePathObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def index(self) -> int:
        """Gets the index of this MessageDeltaContentTextAnnotationsFilePathObject.

        The index of the annotation in the text content part.  # noqa: E501

        :return: The index of this MessageDeltaContentTextAnnotationsFilePathObject.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index: int):
        """Sets the index of this MessageDeltaContentTextAnnotationsFilePathObject.

        The index of the annotation in the text content part.  # noqa: E501

        :param index: The index of this MessageDeltaContentTextAnnotationsFilePathObject.
        :type index: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def type(self) -> str:
        """Gets the type of this MessageDeltaContentTextAnnotationsFilePathObject.

        Always `file_path`.  # noqa: E501

        :return: The type of this MessageDeltaContentTextAnnotationsFilePathObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this MessageDeltaContentTextAnnotationsFilePathObject.

        Always `file_path`.  # noqa: E501

        :param type: The type of this MessageDeltaContentTextAnnotationsFilePathObject.
        :type type: str
        """
        allowed_values = ["file_path"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def text(self) -> str:
        """Gets the text of this MessageDeltaContentTextAnnotationsFilePathObject.

        The text in the message content that needs to be replaced.  # noqa: E501

        :return: The text of this MessageDeltaContentTextAnnotationsFilePathObject.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this MessageDeltaContentTextAnnotationsFilePathObject.

        The text in the message content that needs to be replaced.  # noqa: E501

        :param text: The text of this MessageDeltaContentTextAnnotationsFilePathObject.
        :type text: str
        """

        self._text = text

    @property
    def file_path(self) -> MessageDeltaContentTextAnnotationsFilePathObjectFilePath:
        """Gets the file_path of this MessageDeltaContentTextAnnotationsFilePathObject.


        :return: The file_path of this MessageDeltaContentTextAnnotationsFilePathObject.
        :rtype: MessageDeltaContentTextAnnotationsFilePathObjectFilePath
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: MessageDeltaContentTextAnnotationsFilePathObjectFilePath):
        """Sets the file_path of this MessageDeltaContentTextAnnotationsFilePathObject.


        :param file_path: The file_path of this MessageDeltaContentTextAnnotationsFilePathObject.
        :type file_path: MessageDeltaContentTextAnnotationsFilePathObjectFilePath
        """

        self._file_path = file_path

    @property
    def start_index(self) -> int:
        """Gets the start_index of this MessageDeltaContentTextAnnotationsFilePathObject.


        :return: The start_index of this MessageDeltaContentTextAnnotationsFilePathObject.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index: int):
        """Sets the start_index of this MessageDeltaContentTextAnnotationsFilePathObject.


        :param start_index: The start_index of this MessageDeltaContentTextAnnotationsFilePathObject.
        :type start_index: int
        """
        if start_index is not None and start_index < 0:  # noqa: E501
            raise ValueError("Invalid value for `start_index`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start_index = start_index

    @property
    def end_index(self) -> int:
        """Gets the end_index of this MessageDeltaContentTextAnnotationsFilePathObject.


        :return: The end_index of this MessageDeltaContentTextAnnotationsFilePathObject.
        :rtype: int
        """
        return self._end_index

    @end_index.setter
    def end_index(self, end_index: int):
        """Sets the end_index of this MessageDeltaContentTextAnnotationsFilePathObject.


        :param end_index: The end_index of this MessageDeltaContentTextAnnotationsFilePathObject.
        :type end_index: int
        """
        if end_index is not None and end_index < 0:  # noqa: E501
            raise ValueError("Invalid value for `end_index`, must be a value greater than or equal to `0`")  # noqa: E501

        self._end_index = end_index
