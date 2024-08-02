from httpx import AsyncClient

async def test_create_embedding(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/embeddings",
    )

    assert response.status_code == 401
