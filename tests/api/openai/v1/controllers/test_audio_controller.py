from httpx import AsyncClient

async def test_create_speech(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/audio/speech",
    )

    assert response.status_code == 401

async def test_create_transcription(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/audio/transcriptions",
    )

    assert response.status_code == 401

async def test_create_translation(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/audio/translations",
    )

    assert response.status_code == 401
