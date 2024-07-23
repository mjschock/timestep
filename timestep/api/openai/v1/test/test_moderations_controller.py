import unittest

from flask import json

from timestep.api.openai.v1.models.create_moderation_request import \
    CreateModerationRequest  # noqa: E501
from timestep.api.openai.v1.models.create_moderation_response import \
    CreateModerationResponse  # noqa: E501
from timestep.api.openai.v1.test import BaseTestCase


class TestModerationsController(BaseTestCase):
    """ModerationsController integration test stubs"""

    def test_create_moderation(self):
        """Test case for create_moderation

        Classifies if text is potentially harmful.
        """
        create_moderation_request = {"input":"I want to kill them.","model":"text-moderation-stable"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/moderations',
            method='POST',
            headers=headers,
            data=json.dumps(create_moderation_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
