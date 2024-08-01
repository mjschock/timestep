from fastapi.testclient import TestClient

from timestep.server import fastapi_app

client = TestClient(fastapi_app)

def test_create_moderation():
    response = client.post(
        "/api/openai/v1/moderations",
    )

    assert response.status_code == 501
