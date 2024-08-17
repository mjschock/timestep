from httpx import AsyncClient

from timestep.config import settings


token = settings.openai_api_key.get_secret_value()


async def test_create_completion(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/completions",
    )

    assert response.status_code == 401

    response = await client.post(
        "/api/openai/v1/completions",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 400

    response = await client.post(
        "/api/openai/v1/completions",
        headers={
            "Authorization": f"Bearer {token}",
        },
        json={
            "model": "gpt-3.5-turbo",
            "prompt": "Once upon a time",
        },
    )

    assert response.status_code == 500
