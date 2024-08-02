from fastapi.testclient import TestClient

def test_create_moderation(client: TestClient):
    response = client.post(
        "/api/openai/v1/moderations",
    )

    assert response.status_code == 401
