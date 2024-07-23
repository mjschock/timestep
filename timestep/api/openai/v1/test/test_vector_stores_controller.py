import unittest

from flask import json

from timestep.api.openai.v1.models.create_vector_store_file_batch_request import \
    CreateVectorStoreFileBatchRequest  # noqa: E501
from timestep.api.openai.v1.models.create_vector_store_file_request import \
    CreateVectorStoreFileRequest  # noqa: E501
from timestep.api.openai.v1.models.create_vector_store_request import \
    CreateVectorStoreRequest  # noqa: E501
from timestep.api.openai.v1.models.delete_vector_store_file_response import \
    DeleteVectorStoreFileResponse  # noqa: E501
from timestep.api.openai.v1.models.delete_vector_store_response import \
    DeleteVectorStoreResponse  # noqa: E501
from timestep.api.openai.v1.models.list_vector_store_files_response import \
    ListVectorStoreFilesResponse  # noqa: E501
from timestep.api.openai.v1.models.list_vector_stores_response import \
    ListVectorStoresResponse  # noqa: E501
from timestep.api.openai.v1.models.update_vector_store_request import \
    UpdateVectorStoreRequest  # noqa: E501
from timestep.api.openai.v1.models.vector_store_file_batch_object import \
    VectorStoreFileBatchObject  # noqa: E501
from timestep.api.openai.v1.models.vector_store_file_object import \
    VectorStoreFileObject  # noqa: E501
from timestep.api.openai.v1.models.vector_store_object import \
    VectorStoreObject  # noqa: E501
from timestep.api.openai.v1.test import BaseTestCase


class TestVectorStoresController(BaseTestCase):
    """VectorStoresController integration test stubs"""

    def test_cancel_vector_store_file_batch(self):
        """Test case for cancel_vector_store_file_batch

        Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel'.format(vector_store_id='vector_store_id_example', batch_id='batch_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_vector_store(self):
        """Test case for create_vector_store

        Create a vector store.
        """
        create_vector_store_request = {"chunking_strategy":{"type":"auto"},"metadata":"{}","expires_after":{"anchor":"last_active_at","days":339},"file_ids":["file_ids","file_ids","file_ids","file_ids","file_ids"],"name":"name"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores',
            method='POST',
            headers=headers,
            data=json.dumps(create_vector_store_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_vector_store_file(self):
        """Test case for create_vector_store_file

        Create a vector store file by attaching a [File](/docs/api-reference/files) to a [vector store](/docs/api-reference/vector-stores/object).
        """
        create_vector_store_file_request = {"chunking_strategy":{"type":"auto"},"file_id":"file_id"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}/files'.format(vector_store_id='vs_abc123'),
            method='POST',
            headers=headers,
            data=json.dumps(create_vector_store_file_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_vector_store_file_batch(self):
        """Test case for create_vector_store_file_batch

        Create a vector store file batch.
        """
        create_vector_store_file_batch_request = {"chunking_strategy":{"type":"auto"},"file_ids":["file_ids","file_ids","file_ids","file_ids","file_ids"]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}/file_batches'.format(vector_store_id='vs_abc123'),
            method='POST',
            headers=headers,
            data=json.dumps(create_vector_store_file_batch_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_vector_store(self):
        """Test case for delete_vector_store

        Delete a vector store.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}'.format(vector_store_id='vector_store_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_vector_store_file(self):
        """Test case for delete_vector_store_file

        Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](/docs/api-reference/files/delete) endpoint.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}/files/{file_id}'.format(vector_store_id='vector_store_id_example', file_id='file_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vector_store(self):
        """Test case for get_vector_store

        Retrieves a vector store.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}'.format(vector_store_id='vector_store_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vector_store_file(self):
        """Test case for get_vector_store_file

        Retrieves a vector store file.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}/files/{file_id}'.format(vector_store_id='vs_abc123', file_id='file-abc123'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vector_store_file_batch(self):
        """Test case for get_vector_store_file_batch

        Retrieves a vector store file batch.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}'.format(vector_store_id='vs_abc123', batch_id='vsfb_abc123'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_files_in_vector_store_batch(self):
        """Test case for list_files_in_vector_store_batch

        Returns a list of vector store files in a batch.
        """
        query_string = [('limit', 20),
                        ('order', desc),
                        ('after', 'after_example'),
                        ('before', 'before_example'),
                        ('filter', 'filter_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/files'.format(vector_store_id='vector_store_id_example', batch_id='batch_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_vector_store_files(self):
        """Test case for list_vector_store_files

        Returns a list of vector store files.
        """
        query_string = [('limit', 20),
                        ('order', desc),
                        ('after', 'after_example'),
                        ('before', 'before_example'),
                        ('filter', 'filter_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}/files'.format(vector_store_id='vector_store_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_vector_stores(self):
        """Test case for list_vector_stores

        Returns a list of vector stores.
        """
        query_string = [('limit', 20),
                        ('order', desc),
                        ('after', 'after_example'),
                        ('before', 'before_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_vector_store(self):
        """Test case for modify_vector_store

        Modifies a vector store.
        """
        update_vector_store_request = {"metadata":"{}","expires_after":{"anchor":"last_active_at","days":339},"name":"name"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/vector_stores/{vector_store_id}'.format(vector_store_id='vector_store_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(update_vector_store_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
