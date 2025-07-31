import pytest

# ============================================================================
# Vector Stores Tests
# ============================================================================


@pytest.mark.asyncio
async def test_create_vector_store(async_client):
    response = await async_client.vector_stores.create(
        name="Test Vector Store", expires_after={"anchor": "last_active_at", "days": 7}
    )
    assert hasattr(response, "id")
    assert response.name == "Test Vector Store"
    # Cleanup
    await async_client.vector_stores.delete(response.id)


@pytest.mark.asyncio
async def test_list_vector_stores(async_client):
    response = await async_client.vector_stores.list()
    assert hasattr(response, "data")
    assert isinstance(response.data, list)


@pytest.mark.asyncio
async def test_retrieve_vector_store(async_client):
    created = await async_client.vector_stores.create(name="Test Vector Store")
    response = await async_client.vector_stores.retrieve(created.id)
    assert hasattr(response, "id")
    assert response.id == created.id
    await async_client.vector_stores.delete(created.id)


@pytest.mark.asyncio
async def test_update_vector_store(async_client):
    created = await async_client.vector_stores.create(name="Test Vector Store")
    response = await async_client.vector_stores.update(
        created.id, name="Updated Test Vector Store", metadata={"updated": "true"}
    )
    assert hasattr(response, "id")
    assert response.name == "Updated Test Vector Store"
    await async_client.vector_stores.delete(created.id)


@pytest.mark.asyncio
async def test_delete_vector_store(async_client):
    created = await async_client.vector_stores.create(name="Test Delete Vector Store")
    response = await async_client.vector_stores.delete(created.id)
    assert hasattr(response, "deleted")
    assert response.deleted is True


@pytest.mark.asyncio
async def test_search_vector_store(async_client):
    created = await async_client.vector_stores.create(name="Test Search Vector Store")
    response = await async_client.vector_stores.search(
        vector_store_id=created.id, query="test query"
    )
    assert hasattr(response, "data")
    assert isinstance(response.data, list)
    await async_client.vector_stores.delete(created.id)


# ============================================================================
# Vector Store Files Tests
# ============================================================================


@pytest.mark.asyncio
async def test_create_vector_store_file(async_client, sample_text_file):
    vector_store = await async_client.vector_stores.create(name="Test VSF Vector Store")
    with open(sample_text_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="assistants")
    file_id = upload_response.id
    response = await async_client.vector_stores.files.create(
        vector_store_id=vector_store.id, file_id=file_id
    )
    assert hasattr(response, "id")
    assert response.vector_store_id == vector_store.id
    # Cleanup
    await async_client.vector_stores.files.delete(
        vector_store_id=vector_store.id, file_id=file_id
    )
    await async_client.vector_stores.delete(vector_store.id)
    await async_client.files.delete(file_id)


@pytest.mark.asyncio
async def test_list_vector_store_files(async_client):
    vector_store = await async_client.vector_stores.create(
        name="Test VSF List Vector Store"
    )
    response = await async_client.vector_stores.files.list(
        vector_store_id=vector_store.id
    )
    assert hasattr(response, "data")
    assert isinstance(response.data, list)
    await async_client.vector_stores.delete(vector_store.id)


@pytest.mark.asyncio
async def test_retrieve_vector_store_file(async_client, sample_text_file):
    vector_store = await async_client.vector_stores.create(
        name="Test VSF Retrieve Vector Store"
    )
    with open(sample_text_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="assistants")
    file_id = upload_response.id
    await async_client.vector_stores.files.create(
        vector_store_id=vector_store.id, file_id=file_id
    )
    response = await async_client.vector_stores.files.retrieve(
        vector_store_id=vector_store.id, file_id=file_id
    )
    assert hasattr(response, "id")
    assert response.vector_store_id == vector_store.id
    # Cleanup
    await async_client.vector_stores.files.delete(
        vector_store_id=vector_store.id, file_id=file_id
    )
    await async_client.vector_stores.delete(vector_store.id)
    await async_client.files.delete(file_id)


@pytest.mark.asyncio
async def test_delete_vector_store_file(async_client, sample_text_file):
    vector_store = await async_client.vector_stores.create(
        name="Test VSF Delete Vector Store"
    )
    with open(sample_text_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="assistants")
    file_id = upload_response.id
    await async_client.vector_stores.files.create(
        vector_store_id=vector_store.id, file_id=file_id
    )
    response = await async_client.vector_stores.files.delete(
        vector_store_id=vector_store.id, file_id=file_id
    )
    assert hasattr(response, "deleted")
    assert response.deleted is True
    await async_client.vector_stores.delete(vector_store.id)
    await async_client.files.delete(file_id)


# ============================================================================
# Vector Store File Batches Tests
# ============================================================================


@pytest.mark.asyncio
async def test_create_vector_store_file_batch(async_client, sample_text_file):
    vector_store = await async_client.vector_stores.create(
        name="Test VSFB Vector Store"
    )
    with open(sample_text_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="assistants")
    file_id = upload_response.id
    response = await async_client.vector_stores.file_batches.create(
        vector_store_id=vector_store.id, file_ids=[file_id]
    )
    assert hasattr(response, "id")
    assert response.vector_store_id == vector_store.id
    # Cancel the batch
    await async_client.vector_stores.file_batches.cancel(
        vector_store_id=vector_store.id, batch_id=response.id
    )
    await async_client.vector_stores.delete(vector_store.id)
    await async_client.files.delete(file_id)


@pytest.mark.asyncio
async def test_retrieve_vector_store_file_batch(async_client, sample_text_file):
    vector_store = await async_client.vector_stores.create(
        name="Test VSFB Retrieve Vector Store"
    )
    with open(sample_text_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="assistants")
    file_id = upload_response.id
    batch = await async_client.vector_stores.file_batches.create(
        vector_store_id=vector_store.id, file_ids=[file_id]
    )
    response = await async_client.vector_stores.file_batches.retrieve(
        vector_store_id=vector_store.id, batch_id=batch.id
    )
    assert hasattr(response, "id")
    assert response.id == batch.id
    await async_client.vector_stores.file_batches.cancel(
        vector_store_id=vector_store.id, batch_id=batch.id
    )
    await async_client.vector_stores.delete(vector_store.id)
    await async_client.files.delete(file_id)


@pytest.mark.asyncio
async def test_cancel_vector_store_file_batch(async_client, sample_text_file):
    vector_store = await async_client.vector_stores.create(
        name="Test VSFB Cancel Vector Store"
    )
    with open(sample_text_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="assistants")
    file_id = upload_response.id
    batch = await async_client.vector_stores.file_batches.create(
        vector_store_id=vector_store.id, file_ids=[file_id]
    )
    response = await async_client.vector_stores.file_batches.cancel(
        vector_store_id=vector_store.id, batch_id=batch.id
    )
    assert hasattr(response, "id")
    assert response.id == batch.id
    await async_client.vector_stores.delete(vector_store.id)
    await async_client.files.delete(file_id)


@pytest.mark.asyncio
async def test_list_vector_store_files_in_batch(async_client, sample_text_file):
    vector_store = await async_client.vector_stores.create(
        name="Test VSFB List Files Vector Store"
    )
    with open(sample_text_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="assistants")
    file_id = upload_response.id
    batch = await async_client.vector_stores.file_batches.create(
        vector_store_id=vector_store.id, file_ids=[file_id]
    )
    response = await async_client.vector_stores.file_batches.list_files(
        vector_store_id=vector_store.id, batch_id=batch.id
    )
    assert hasattr(response, "data")
    assert isinstance(response.data, list)
    await async_client.vector_stores.file_batches.cancel(
        vector_store_id=vector_store.id, batch_id=batch.id
    )
    await async_client.vector_stores.delete(vector_store.id)
    await async_client.files.delete(file_id)
