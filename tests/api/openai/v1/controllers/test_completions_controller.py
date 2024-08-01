from fastapi.testclient import TestClient

from timestep.server import fastapi_app

client = TestClient(fastapi_app)

def test_create_completion():
    response = client.post(
        "/api/openai/v1/completions",
    )

    assert response.status_code == 401
