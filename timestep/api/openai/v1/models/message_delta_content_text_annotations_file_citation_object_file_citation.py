from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model


class MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_id=None, quote=None):  # noqa: E501
        """MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation - a model defined in OpenAPI

        :param file_id: The file_id of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.  # noqa: E501
        :type file_id: str
        :param quote: The quote of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.  # noqa: E501
        :type quote: str
        """
        self.openapi_types = {
            'file_id': str,
            'quote': str
        }

        self.attribute_map = {
            'file_id': 'file_id',
            'quote': 'quote'
        }

        self._file_id = file_id
        self._quote = quote

    @classmethod
    def from_dict(cls, dikt) -> 'MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MessageDeltaContentTextAnnotationsFileCitationObject_file_citation of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.  # noqa: E501
        :rtype: MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_id(self) -> str:
        """Gets the file_id of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.

        The ID of the specific File the citation is from.  # noqa: E501

        :return: The file_id of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id: str):
        """Sets the file_id of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.

        The ID of the specific File the citation is from.  # noqa: E501

        :param file_id: The file_id of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.
        :type file_id: str
        """

        self._file_id = file_id

    @property
    def quote(self) -> str:
        """Gets the quote of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.

        The specific quote in the file.  # noqa: E501

        :return: The quote of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.
        :rtype: str
        """
        return self._quote

    @quote.setter
    def quote(self, quote: str):
        """Sets the quote of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.

        The specific quote in the file.  # noqa: E501

        :param quote: The quote of this MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation.
        :type quote: str
        """

        self._quote = quote