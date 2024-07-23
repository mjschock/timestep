import unittest

from flask import json

from timestep.api.openai.v1.models.create_image_edit_request_model import \
    CreateImageEditRequestModel  # noqa: E501
from timestep.api.openai.v1.models.create_image_request import \
    CreateImageRequest  # noqa: E501
from timestep.api.openai.v1.models.images_response import \
    ImagesResponse  # noqa: E501
from timestep.api.openai.v1.test import BaseTestCase


class TestImagesController(BaseTestCase):
    """ImagesController integration test stubs"""

    def test_create_image(self):
        """Test case for create_image

        Creates an image given a prompt.
        """
        create_image_request = {"response_format":"url","size":"1024x1024","model":"dall-e-3","style":"vivid","prompt":"A cute baby sea otter","user":"user-1234","n":1,"quality":"standard"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/images/generations',
            method='POST',
            headers=headers,
            data=json.dumps(create_image_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_create_image_edit(self):
        """Test case for create_image_edit

        Creates an edited or extended image given an original image and a prompt.
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(image='/path/to/file',
                    prompt='prompt_example',
                    mask='/path/to/file',
                    model=timestep.api.openai.v1.CreateImageEditRequestModel(),
                    n=1,
                    size=1024x1024,
                    response_format=url,
                    user='user_example')
        response = self.client.open(
            '/v1/images/edits',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_create_image_variation(self):
        """Test case for create_image_variation

        Creates a variation of a given image.
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(image='/path/to/file',
                    model=timestep.api.openai.v1.CreateImageEditRequestModel(),
                    n=1,
                    response_format=url,
                    size=1024x1024,
                    user='user_example')
        response = self.client.open(
            '/v1/images/variations',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
