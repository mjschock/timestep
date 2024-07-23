import unittest

from flask import json

from timestep.api.ap.v1.models.artifact import Artifact  # noqa: E501
from timestep.api.ap.v1.models.get_agent_task404_response import \
    GetAgentTask404Response  # noqa: E501
from timestep.api.ap.v1.models.step import Step  # noqa: E501
from timestep.api.ap.v1.models.step_request_body import \
    StepRequestBody  # noqa: E501
from timestep.api.ap.v1.models.task import Task  # noqa: E501
from timestep.api.ap.v1.models.task_artifacts_list_response import \
    TaskArtifactsListResponse  # noqa: E501
from timestep.api.ap.v1.models.task_list_response import \
    TaskListResponse  # noqa: E501
from timestep.api.ap.v1.models.task_request_body import \
    TaskRequestBody  # noqa: E501
from timestep.api.ap.v1.models.task_steps_list_response import \
    TaskStepsListResponse  # noqa: E501
from timestep.api.ap.v1.test import BaseTestCase


class TestAgentController(BaseTestCase):
    """AgentController integration test stubs"""

    def test_create_agent_task(self):
        """Test case for create_agent_task

        Creates a task for the agent.
        """
        task_request_body = {"input":"Write 'Washington' to the file 'output.txt'.","additional_input":"{\n\"debug\": false,\n\"mode\": \"benchmarks\"\n}"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/ap/v1/agent/tasks',
            method='POST',
            headers=headers,
            data=json.dumps(task_request_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_download_agent_task_artifact(self):
        """Test case for download_agent_task_artifact

        Download a specified artifact.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/ap/v1/agent/tasks/{task_id}/artifacts/{artifact_id}'.format(task_id='50da533e-3904-4401-8a07-c49adf88b5eb', artifact_id='1e41533e-3904-4401-8a07-c49adf8893de'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_execute_agent_task_step(self):
        """Test case for execute_agent_task_step

        Execute a step in the specified agent task.
        """
        step_request_body = {"input":"Write the words you receive to the file 'output.txt'.","additional_input":"{\n\"file_to_refactor\": \"models.py\"\n}"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/ap/v1/agent/tasks/{task_id}/steps'.format(task_id='50da533e-3904-4401-8a07-c49adf88b5eb'),
            method='POST',
            headers=headers,
            data=json.dumps(step_request_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_agent_task(self):
        """Test case for get_agent_task

        Get details about a specified agent task.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/ap/v1/agent/tasks/{task_id}'.format(task_id='1d5a533e-3904-4401-8a07-c49adf88b981'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_agent_task_step(self):
        """Test case for get_agent_task_step

        Get details about a specified task step.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/ap/v1/agent/tasks/{task_id}/steps/{step_id}'.format(task_id='50da533e-3904-4401-8a07-c49adf88b5eb', step_id='28ca533e-3904-4401-8a07-c49adf8891c2'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_agent_task_artifacts(self):
        """Test case for list_agent_task_artifacts

        List all artifacts that have been created for the given task.
        """
        query_string = [('current_page', 1),
                        ('page_size', 10)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/ap/v1/agent/tasks/{task_id}/artifacts'.format(task_id='50da533e-3904-4401-8a07-c49adf88b5eb'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_agent_task_steps(self):
        """Test case for list_agent_task_steps

        List all steps for the specified task.
        """
        query_string = [('current_page', 1),
                        ('page_size', 10)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/ap/v1/agent/tasks/{task_id}/steps'.format(task_id='50da533e-3904-4401-8a07-c49adf88b5eb'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_agent_tasks(self):
        """Test case for list_agent_tasks

        List all tasks that have been created for the agent.
        """
        query_string = [('current_page', 1),
                        ('page_size', 10)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/ap/v1/agent/tasks',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_upload_agent_task_artifacts(self):
        """Test case for upload_agent_task_artifacts

        Upload an artifact for the specified task.
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(file='/path/to/file',
                    relative_path='relative_path_example')
        response = self.client.open(
            '/ap/v1/agent/tasks/{task_id}/artifacts'.format(task_id='50da533e-3904-4401-8a07-c49adf88b5eb'),
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
