import unittest

from flask import json

from timestep.api.openai.v1.models.create_embedding_request import \
    CreateEmbeddingRequest  # noqa: E501
from timestep.api.openai.v1.models.create_embedding_response import \
    CreateEmbeddingResponse  # noqa: E501
from timestep.api.openai.v1.test import BaseTestCase


class TestEmbeddingsController(BaseTestCase):
    """EmbeddingsController integration test stubs"""

    def test_create_embedding(self):
        """Test case for create_embedding

        Creates an embedding vector representing the input text.
        """
        create_embedding_request = {"input":"The quick brown fox jumped over the lazy dog","encoding_format":"float","model":"text-embedding-3-small","user":"user-1234","dimensions":1}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/embeddings',
            method='POST',
            headers=headers,
            data=json.dumps(create_embedding_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
