from fastapi.testclient import TestClient

from timestep.server import fastapi_app

client = TestClient(fastapi_app)

def test_create_speech():
    response = client.post(
        "/api/openai/v1/audio/speech",
    )

    assert response.status_code == 501

def test_create_transcription():
    response = client.post(
        "/api/openai/v1/audio/transcriptions",
    )

    assert response.status_code == 501

def test_create_translation():
    response = client.post(
        "/api/openai/v1/audio/translations",
    )

    assert response.status_code == 501
