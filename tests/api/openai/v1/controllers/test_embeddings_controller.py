from fastapi.testclient import TestClient

from timestep.server import fastapi_app

client = TestClient(fastapi_app)

def test_create_embedding():
    response = client.post(
        "/api/openai/v1/embeddings",
    )

    assert response.status_code == 501
