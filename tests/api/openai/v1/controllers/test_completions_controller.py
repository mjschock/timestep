from fastapi.testclient import TestClient

def test_create_completion(client: TestClient):
    response = client.post(
        "/api/openai/v1/completions",
    )

    assert response.status_code == 401
