from fastapi.testclient import TestClient

from timestep.server import fastapi_app

client = TestClient(fastapi_app)

def test_delete_model():
    response = client.delete(
        "/api/openai/v1/models/ft:gpt-3.5-turbo:acemeco:suffix:abc123",
    )

    assert response.status_code == 501

def test_list_models():
    response = client.get(
        "/api/openai/v1/models",
    )

    assert response.status_code == 501

def test_retrieve_model():
    response = client.get(
        "/api/openai/v1/models/gpt-3.5-turbo",
    )

    assert response.status_code == 501
