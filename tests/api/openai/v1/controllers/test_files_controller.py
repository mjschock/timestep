from httpx import AsyncClient

async def test_create_file(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/files",
    )

    assert response.status_code == 401

async def test_delete_file(client: AsyncClient):
    response = await client.delete(
        "/api/openai/v1/files/file_id_example",
    )

    assert response.status_code == 401

async def test_download_file(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/files/file_id_example/content",
    )

    assert response.status_code == 401

async def test_list_files(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/files?purpose=purpose_example",
    )

    assert response.status_code == 401

async def test_retrieve_file(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/files/file_id_example",
    )

    assert response.status_code == 401
