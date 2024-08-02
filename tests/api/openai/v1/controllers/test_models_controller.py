from fastapi.testclient import TestClient

def test_delete_model(client: TestClient):
    response = client.delete(
        "/api/openai/v1/models/ft:gpt-3.5-turbo:acemeco:suffix:abc123",
    )

    assert response.status_code == 401

def test_list_models(client: TestClient):
    response = client.get(
        "/api/openai/v1/models",
    )

    assert response.status_code == 401

def test_retrieve_model(client: TestClient):
    response = client.get(
        "/api/openai/v1/models/gpt-3.5-turbo",
    )

    assert response.status_code == 401
