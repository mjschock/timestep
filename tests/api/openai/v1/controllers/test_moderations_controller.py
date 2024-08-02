from httpx import AsyncClient

async def test_create_moderation(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/moderations",
    )

    assert response.status_code == 401
