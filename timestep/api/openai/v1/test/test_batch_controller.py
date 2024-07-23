import unittest

from flask import json

from timestep.api.openai.v1.models.batch import Batch  # noqa: E501
from timestep.api.openai.v1.models.create_batch_request import \
    CreateBatchRequest  # noqa: E501
from timestep.api.openai.v1.models.list_batches_response import \
    ListBatchesResponse  # noqa: E501
from timestep.api.openai.v1.test import BaseTestCase


class TestBatchController(BaseTestCase):
    """BatchController integration test stubs"""

    def test_cancel_batch(self):
        """Test case for cancel_batch

        Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/batches/{batch_id}/cancel'.format(batch_id='batch_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_batch(self):
        """Test case for create_batch

        Creates and executes a batch from an uploaded file of requests
        """
        create_batch_request = timestep.api.openai.v1.CreateBatchRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/batches',
            method='POST',
            headers=headers,
            data=json.dumps(create_batch_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_batches(self):
        """Test case for list_batches

        List your organization's batches.
        """
        query_string = [('after', 'after_example'),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/batches',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_batch(self):
        """Test case for retrieve_batch

        Retrieves a batch.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/batches/{batch_id}'.format(batch_id='batch_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
