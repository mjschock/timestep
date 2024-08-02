from httpx import AsyncClient

async def test_create_completion(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/completions",
    )

    assert response.status_code == 401
