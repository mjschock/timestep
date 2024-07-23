from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.create_translation_response_json import \
    CreateTranslationResponseJson  # noqa: E501
from timestep.api.openai.v1.models.create_translation_response_verbose_json import \
    CreateTranslationResponseVerboseJson  # noqa: E501
from timestep.api.openai.v1.models.transcription_segment import \
    TranscriptionSegment  # noqa: E501


class CreateTranslation200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, text=None, language=None, duration=None, segments=None):  # noqa: E501
        """CreateTranslation200Response - a model defined in OpenAPI

        :param text: The text of this CreateTranslation200Response.  # noqa: E501
        :type text: str
        :param language: The language of this CreateTranslation200Response.  # noqa: E501
        :type language: str
        :param duration: The duration of this CreateTranslation200Response.  # noqa: E501
        :type duration: str
        :param segments: The segments of this CreateTranslation200Response.  # noqa: E501
        :type segments: List[TranscriptionSegment]
        """
        self.openapi_types = {
            'text': str,
            'language': str,
            'duration': str,
            'segments': List[TranscriptionSegment]
        }

        self.attribute_map = {
            'text': 'text',
            'language': 'language',
            'duration': 'duration',
            'segments': 'segments'
        }

        self._text = text
        self._language = language
        self._duration = duration
        self._segments = segments

    @classmethod
    def from_dict(cls, dikt) -> 'CreateTranslation200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The createTranslation_200_response of this CreateTranslation200Response.  # noqa: E501
        :rtype: CreateTranslation200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self) -> str:
        """Gets the text of this CreateTranslation200Response.

        The translated text.  # noqa: E501

        :return: The text of this CreateTranslation200Response.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this CreateTranslation200Response.

        The translated text.  # noqa: E501

        :param text: The text of this CreateTranslation200Response.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def language(self) -> str:
        """Gets the language of this CreateTranslation200Response.

        The language of the output translation (always `english`).  # noqa: E501

        :return: The language of this CreateTranslation200Response.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str):
        """Sets the language of this CreateTranslation200Response.

        The language of the output translation (always `english`).  # noqa: E501

        :param language: The language of this CreateTranslation200Response.
        :type language: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def duration(self) -> str:
        """Gets the duration of this CreateTranslation200Response.

        The duration of the input audio.  # noqa: E501

        :return: The duration of this CreateTranslation200Response.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration: str):
        """Sets the duration of this CreateTranslation200Response.

        The duration of the input audio.  # noqa: E501

        :param duration: The duration of this CreateTranslation200Response.
        :type duration: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def segments(self) -> List[TranscriptionSegment]:
        """Gets the segments of this CreateTranslation200Response.

        Segments of the translated text and their corresponding details.  # noqa: E501

        :return: The segments of this CreateTranslation200Response.
        :rtype: List[TranscriptionSegment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments: List[TranscriptionSegment]):
        """Sets the segments of this CreateTranslation200Response.

        Segments of the translated text and their corresponding details.  # noqa: E501

        :param segments: The segments of this CreateTranslation200Response.
        :type segments: List[TranscriptionSegment]
        """

        self._segments = segments
