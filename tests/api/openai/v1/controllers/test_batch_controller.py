from httpx import AsyncClient

async def test_cancel_batch(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/batches/batch_id_example/cancel",
    )

    assert response.status_code == 401

async def test_create_batch(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/batches",
    )

    assert response.status_code == 401

async def test_list_batches(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/batches?after=after_example&limit=20",
    )

    assert response.status_code == 401

async def test_retrieve_batch(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/batches/batch_id_example",
    )

    assert response.status_code == 401
