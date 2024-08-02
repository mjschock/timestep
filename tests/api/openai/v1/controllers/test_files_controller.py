from fastapi.testclient import TestClient

def test_create_file(client: TestClient):
    response = client.post(
        "/api/openai/v1/files",
    )

    assert response.status_code == 401

def test_delete_file(client: TestClient):
    response = client.delete(
        "/api/openai/v1/files/file_id_example",
    )

    assert response.status_code == 401

def test_download_file(client: TestClient):
    response = client.get(
        "/api/openai/v1/files/file_id_example/content",
    )

    assert response.status_code == 401

def test_list_files(client: TestClient):
    response = client.get(
        "/api/openai/v1/files?purpose=purpose_example",
    )

    assert response.status_code == 401

def test_retrieve_file(client: TestClient):
    response = client.get(
        "/api/openai/v1/files/file_id_example",
    )

    assert response.status_code == 401
