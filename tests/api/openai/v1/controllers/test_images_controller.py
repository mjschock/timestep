from fastapi.testclient import TestClient

def test_create_image(client: TestClient):
    response = client.post(
        "/api/openai/v1/images/generations",
    )

    assert response.status_code == 401

def test_create_image_edit(client: TestClient):
    response = client.post(
        "/api/openai/v1/images/edits",
    )

    assert response.status_code == 401

def test_create_image_variation(client: TestClient):
    response = client.post(
        "/api/openai/v1/images/variations",
    )

    assert response.status_code == 401
