import unittest

from flask import json

from timestep.api.openai.v1.models.create_chat_completion_request import \
    CreateChatCompletionRequest  # noqa: E501
from timestep.api.openai.v1.models.create_chat_completion_response import \
    CreateChatCompletionResponse  # noqa: E501
from timestep.api.openai.v1.test import BaseTestCase


class TestChatController(BaseTestCase):
    """ChatController integration test stubs"""

    def test_create_chat_completion(self):
        """Test case for create_chat_completion

        Creates a model response for the given chat conversation.
        """
        create_chat_completion_request = {"top_logprobs":2,"logit_bias":{"key":6},"seed":-2147483648,"functions":[{"name":"name","description":"description","parameters":{"key":""}},{"name":"name","description":"description","parameters":{"key":""}},{"name":"name","description":"description","parameters":{"key":""}},{"name":"name","description":"description","parameters":{"key":""}},{"name":"name","description":"description","parameters":{"key":""}}],"max_tokens":5,"function_call":"none","presence_penalty":0.25495066265333133,"tools":[{"function":{"name":"name","description":"description","parameters":{"key":""}},"type":"function"},{"function":{"name":"name","description":"description","parameters":{"key":""}},"type":"function"}],"n":1,"logprobs":False,"top_p":1,"frequency_penalty":-1.6796687238155954,"response_format":{"type":"json_object"},"stop":"CreateChatCompletionRequest_stop","parallel_tool_calls":True,"stream":False,"temperature":1,"messages":[{"role":"system","name":"name","content":"content"},{"role":"system","name":"name","content":"content"}],"tool_choice":"none","model":"gpt-4-turbo","service_tier":"auto","stream_options":{"include_usage":True},"user":"user-1234"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/chat/completions',
            method='POST',
            headers=headers,
            data=json.dumps(create_chat_completion_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
