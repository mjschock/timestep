from fastapi.testclient import TestClient

def test_create_speech(client: TestClient):
    response = client.post(
        "/api/openai/v1/audio/speech",
    )

    assert response.status_code == 401

def test_create_transcription(client: TestClient):
    response = client.post(
        "/api/openai/v1/audio/transcriptions",
    )

    assert response.status_code == 401

def test_create_translation(client: TestClient):
    response = client.post(
        "/api/openai/v1/audio/translations",
    )

    assert response.status_code == 401
