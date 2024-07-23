import unittest

from flask import json

from timestep.api.openai.v1.models.delete_model_response import \
    DeleteModelResponse  # noqa: E501
from timestep.api.openai.v1.models.list_models_response import \
    ListModelsResponse  # noqa: E501
from timestep.api.openai.v1.models.model import Model  # noqa: E501
from timestep.api.openai.v1.test import BaseTestCase


class TestModelsController(BaseTestCase):
    """ModelsController integration test stubs"""

    def test_delete_model(self):
        """Test case for delete_model

        Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/models/{model}'.format(model='ft:gpt-3.5-turbo:acemeco:suffix:abc123'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_models(self):
        """Test case for list_models

        Lists the currently available models, and provides basic information about each one such as the owner and availability.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/models',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_model(self):
        """Test case for retrieve_model

        Retrieves a model instance, providing basic information about the model such as the owner and permissioning.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/models/{model}'.format(model='gpt-3.5-turbo'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
