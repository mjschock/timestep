import unittest

from flask import json

from timestep.api.openai.v1.models.create_fine_tuning_job_request import \
    CreateFineTuningJobRequest  # noqa: E501
from timestep.api.openai.v1.models.fine_tuning_job import \
    FineTuningJob  # noqa: E501
from timestep.api.openai.v1.models.list_fine_tuning_job_checkpoints_response import \
    ListFineTuningJobCheckpointsResponse  # noqa: E501
from timestep.api.openai.v1.models.list_fine_tuning_job_events_response import \
    ListFineTuningJobEventsResponse  # noqa: E501
from timestep.api.openai.v1.models.list_paginated_fine_tuning_jobs_response import \
    ListPaginatedFineTuningJobsResponse  # noqa: E501
from timestep.api.openai.v1.test import BaseTestCase


class TestFineTuningController(BaseTestCase):
    """FineTuningController integration test stubs"""

    def test_cancel_fine_tuning_job(self):
        """Test case for cancel_fine_tuning_job

        Immediately cancel a fine-tune job. 
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/fine_tuning/jobs/{fine_tuning_job_id}/cancel'.format(fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_fine_tuning_job(self):
        """Test case for create_fine_tuning_job

        Creates a fine-tuning job which begins the process of creating a new model from a given dataset.  Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.  [Learn more about fine-tuning](/docs/guides/fine-tuning) 
        """
        create_fine_tuning_job_request = {"training_file":"file-abc123","seed":42,"validation_file":"file-abc123","hyperparameters":{"batch_size":"auto","n_epochs":"auto","learning_rate_multiplier":"auto"},"model":"gpt-3.5-turbo","suffix":"suffix","integrations":[{"wandb":{"name":"name","project":"my-wandb-project","entity":"entity","tags":["custom-tag","custom-tag"]},"type":"wandb"},{"wandb":{"name":"name","project":"my-wandb-project","entity":"entity","tags":["custom-tag","custom-tag"]},"type":"wandb"}]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/fine_tuning/jobs',
            method='POST',
            headers=headers,
            data=json.dumps(create_fine_tuning_job_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_fine_tuning_events(self):
        """Test case for list_fine_tuning_events

        Get status updates for a fine-tuning job. 
        """
        query_string = [('after', 'after_example'),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/fine_tuning/jobs/{fine_tuning_job_id}/events'.format(fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_fine_tuning_job_checkpoints(self):
        """Test case for list_fine_tuning_job_checkpoints

        List checkpoints for a fine-tuning job. 
        """
        query_string = [('after', 'after_example'),
                        ('limit', 10)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints'.format(fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_paginated_fine_tuning_jobs(self):
        """Test case for list_paginated_fine_tuning_jobs

        List your organization's fine-tuning jobs 
        """
        query_string = [('after', 'after_example'),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/fine_tuning/jobs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_fine_tuning_job(self):
        """Test case for retrieve_fine_tuning_job

        Get info about a fine-tuning job.  [Learn more about fine-tuning](/docs/guides/fine-tuning) 
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/fine_tuning/jobs/{fine_tuning_job_id}'.format(fine_tuning_job_id='ft-AF1WoRqd3aJAHsqc9NY7iL8F'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
