from fastapi.testclient import TestClient

from timestep.server import fastapi_app

client = TestClient(fastapi_app)

def test_create_image():
    response = client.post(
        "/api/openai/v1/images/generations",
    )

    assert response.status_code == 401

def test_create_image_edit():
    response = client.post(
        "/api/openai/v1/images/edits",
    )

    assert response.status_code == 401

def test_create_image_variation():
    response = client.post(
        "/api/openai/v1/images/variations",
    )

    assert response.status_code == 401
