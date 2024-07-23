import unittest

from flask import json

from timestep.api.openai.v1.models.create_speech_request import \
    CreateSpeechRequest  # noqa: E501
from timestep.api.openai.v1.models.create_transcription200_response import \
    CreateTranscription200Response  # noqa: E501
from timestep.api.openai.v1.models.create_transcription_request_model import \
    CreateTranscriptionRequestModel  # noqa: E501
from timestep.api.openai.v1.models.create_translation200_response import \
    CreateTranslation200Response  # noqa: E501
from timestep.api.openai.v1.test import BaseTestCase


class TestAudioController(BaseTestCase):
    """AudioController integration test stubs"""

    def test_create_speech(self):
        """Test case for create_speech

        Generates audio from the input text.
        """
        create_speech_request = {"voice":"alloy","input":"input","response_format":"mp3","model":"CreateSpeechRequest_model","speed":0.5503105714228793}
        headers = { 
            'Accept': 'application/octet-stream',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/audio/speech',
            method='POST',
            headers=headers,
            data=json.dumps(create_speech_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_create_transcription(self):
        """Test case for create_transcription

        Transcribes audio into the input language.
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(file='/path/to/file',
                    model=timestep.api.openai.v1.CreateTranscriptionRequestModel(),
                    language='language_example',
                    prompt='prompt_example',
                    response_format=json,
                    temperature=0,
                    timestamp_granularities=['timestamp_granularities_example'])
        response = self.client.open(
            '/v1/audio/transcriptions',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_create_translation(self):
        """Test case for create_translation

        Translates audio into English.
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(file='/path/to/file',
                    model=timestep.api.openai.v1.CreateTranscriptionRequestModel(),
                    prompt='prompt_example',
                    response_format='json',
                    temperature=0)
        response = self.client.open(
            '/v1/audio/translations',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
