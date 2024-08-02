from httpx import AsyncClient

async def test_create_image(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/images/generations",
    )

    assert response.status_code == 401

async def test_create_image_edit(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/images/edits",
    )

    assert response.status_code == 401

async def test_create_image_variation(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/images/variations",
    )

    assert response.status_code == 401
