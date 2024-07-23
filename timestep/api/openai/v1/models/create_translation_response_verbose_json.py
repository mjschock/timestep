from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.transcription_segment import \
    TranscriptionSegment  # noqa: E501


class CreateTranslationResponseVerboseJson(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, language=None, duration=None, text=None, segments=None):  # noqa: E501
        """CreateTranslationResponseVerboseJson - a model defined in OpenAPI

        :param language: The language of this CreateTranslationResponseVerboseJson.  # noqa: E501
        :type language: str
        :param duration: The duration of this CreateTranslationResponseVerboseJson.  # noqa: E501
        :type duration: str
        :param text: The text of this CreateTranslationResponseVerboseJson.  # noqa: E501
        :type text: str
        :param segments: The segments of this CreateTranslationResponseVerboseJson.  # noqa: E501
        :type segments: List[TranscriptionSegment]
        """
        self.openapi_types = {
            'language': str,
            'duration': str,
            'text': str,
            'segments': List[TranscriptionSegment]
        }

        self.attribute_map = {
            'language': 'language',
            'duration': 'duration',
            'text': 'text',
            'segments': 'segments'
        }

        self._language = language
        self._duration = duration
        self._text = text
        self._segments = segments

    @classmethod
    def from_dict(cls, dikt) -> 'CreateTranslationResponseVerboseJson':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateTranslationResponseVerboseJson of this CreateTranslationResponseVerboseJson.  # noqa: E501
        :rtype: CreateTranslationResponseVerboseJson
        """
        return util.deserialize_model(dikt, cls)

    @property
    def language(self) -> str:
        """Gets the language of this CreateTranslationResponseVerboseJson.

        The language of the output translation (always `english`).  # noqa: E501

        :return: The language of this CreateTranslationResponseVerboseJson.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str):
        """Sets the language of this CreateTranslationResponseVerboseJson.

        The language of the output translation (always `english`).  # noqa: E501

        :param language: The language of this CreateTranslationResponseVerboseJson.
        :type language: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def duration(self) -> str:
        """Gets the duration of this CreateTranslationResponseVerboseJson.

        The duration of the input audio.  # noqa: E501

        :return: The duration of this CreateTranslationResponseVerboseJson.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration: str):
        """Sets the duration of this CreateTranslationResponseVerboseJson.

        The duration of the input audio.  # noqa: E501

        :param duration: The duration of this CreateTranslationResponseVerboseJson.
        :type duration: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def text(self) -> str:
        """Gets the text of this CreateTranslationResponseVerboseJson.

        The translated text.  # noqa: E501

        :return: The text of this CreateTranslationResponseVerboseJson.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this CreateTranslationResponseVerboseJson.

        The translated text.  # noqa: E501

        :param text: The text of this CreateTranslationResponseVerboseJson.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def segments(self) -> List[TranscriptionSegment]:
        """Gets the segments of this CreateTranslationResponseVerboseJson.

        Segments of the translated text and their corresponding details.  # noqa: E501

        :return: The segments of this CreateTranslationResponseVerboseJson.
        :rtype: List[TranscriptionSegment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments: List[TranscriptionSegment]):
        """Sets the segments of this CreateTranslationResponseVerboseJson.

        Segments of the translated text and their corresponding details.  # noqa: E501

        :param segments: The segments of this CreateTranslationResponseVerboseJson.
        :type segments: List[TranscriptionSegment]
        """

        self._segments = segments
