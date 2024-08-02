from fastapi.testclient import TestClient

def test_create_embedding(client: TestClient):
    response = client.post(
        "/api/openai/v1/embeddings",
    )

    assert response.status_code == 401
