from httpx import AsyncClient

async def test_delete_model(client: AsyncClient):
    response = await client.delete(
        "/api/openai/v1/models/ft:gpt-3.5-turbo:acemeco:suffix:abc123",
    )

    assert response.status_code == 401

async def test_list_models(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/models",
    )

    assert response.status_code == 401

async def test_retrieve_model(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/models/gpt-3.5-turbo",
    )

    assert response.status_code == 401
