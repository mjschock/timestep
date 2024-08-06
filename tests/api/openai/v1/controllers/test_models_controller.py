from httpx import AsyncClient

from timestep.config import Settings

settings = Settings()
token = settings.openai_api_key.get_secret_value()

async def test_delete_model(client: AsyncClient):
    response = await client.delete(
        "/api/openai/v1/models/ft:gpt-3.5-turbo:acemeco:suffix:abc123",
    )

    assert response.status_code == 401

    response = await client.delete(
        "/api/openai/v1/models/ft:gpt-3.5-turbo:acemeco:suffix:abc123",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

async def test_list_models(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/models",
    )

    assert response.status_code == 401

    response = await client.get(
        "/api/openai/v1/models",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

async def test_retrieve_model(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/models/gpt-3.5-turbo",
    )

    assert response.status_code == 401

    response = await client.get(
        "/api/openai/v1/models/gpt-3.5-turbo",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200
