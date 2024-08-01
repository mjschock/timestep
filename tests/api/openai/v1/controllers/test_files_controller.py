from fastapi.testclient import TestClient

from timestep.server import fastapi_app

client = TestClient(fastapi_app)

def test_create_file():
    response = client.post(
        "/api/openai/v1/files",
    )

    assert response.status_code == 401

def test_delete_file():
    response = client.delete(
        "/api/openai/v1/files/file_id_example",
    )

    assert response.status_code == 401

def test_download_file():
    response = client.get(
        "/api/openai/v1/files/file_id_example/content",
    )

    assert response.status_code == 401

def test_list_files():
    response = client.get(
        "/api/openai/v1/files?purpose=purpose_example",
    )

    assert response.status_code == 401

def test_retrieve_file():
    response = client.get(
        "/api/openai/v1/files/file_id_example",
    )

    assert response.status_code == 401
