import pytest


@pytest.mark.asyncio
async def test_create_batch(async_client):
    """Test creating a batch"""
    # First, we need to create a file to use as input
    # For now, we'll use a mock file ID
    mock_file_id = "file-abc123"

    response = await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
        metadata={"test": "metadata"},
    )

    assert hasattr(response, "id")
    assert response.object == "batch"
    assert response.endpoint == "/v1/chat/completions"
    assert response.input_file_id == mock_file_id
    assert response.completion_window == "24h"
    assert response.status in [
        "validating",
        "pending",
        "in_progress",
        "completed",
        "failed",
    ]
    assert hasattr(response, "created_at")
    assert hasattr(response, "expires_at")
    assert hasattr(response, "request_counts")
    assert response.metadata["test"] == "metadata"


@pytest.mark.asyncio
async def test_create_batch_missing_required_fields(async_client):
    """Test creating a batch with missing required fields"""
    # Test missing input_file_id - client enforces this
    try:
        await async_client.batches.create(
            endpoint="/v1/chat/completions",
            completion_window="24h",
        )
        raise AssertionError("Should have raised an error")
    except TypeError as e:
        assert "input_file_id" in str(e)
    except Exception as e:
        assert "input_file_id is required" in str(e) or "400" in str(e)

    # Test missing endpoint - client enforces this
    try:
        await async_client.batches.create(
            input_file_id="file-abc123",
            completion_window="24h",
        )
        raise AssertionError("Should have raised an error")
    except TypeError as e:
        assert "endpoint" in str(e)
    except Exception as e:
        assert "endpoint is required" in str(e) or "400" in str(e)


@pytest.mark.asyncio
async def test_create_batch_invalid_endpoint(async_client):
    """Test creating a batch with invalid endpoint"""
    try:
        await async_client.batches.create(
            input_file_id="file-abc123",
            endpoint="/v1/invalid-endpoint",
            completion_window="24h",
        )
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "endpoint must be" in str(e) or "400" in str(e)


@pytest.mark.asyncio
async def test_create_batch_invalid_completion_window(async_client):
    """Test creating a batch with invalid completion window"""
    try:
        await async_client.batches.create(
            input_file_id="file-abc123",
            endpoint="/v1/chat/completions",
            completion_window="48h",
        )
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "completion_window must be" in str(e) or "400" in str(e)


@pytest.mark.asyncio
async def test_list_batches(async_client):
    """Test listing batches"""
    # First create a batch
    mock_file_id = "file-abc123"
    await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )

    # List batches
    response = await async_client.batches.list()

    assert hasattr(response, "object")
    assert response.object == "list"
    assert hasattr(response, "data")
    assert isinstance(response.data, list)
    assert len(response.data) >= 1


@pytest.mark.asyncio
async def test_list_batches_with_after(async_client):
    """Test listing batches with after parameter"""
    # Create a batch
    mock_file_id = "file-abc123"
    batch = await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )

    # List batches after the created batch
    response = await async_client.batches.list(after=str(batch.created_at))

    assert hasattr(response, "object")
    assert response.object == "list"
    assert hasattr(response, "data")
    # Should not include the batch we just created since we're filtering after its creation time
    assert len(response.data) == 0


@pytest.mark.asyncio
async def test_list_batches_with_limit(async_client):
    """Test listing batches with limit parameter"""
    # Create multiple batches
    for i in range(3):
        await async_client.batches.create(
            input_file_id=f"file-{i}",
            endpoint="/v1/chat/completions",
            completion_window="24h",
        )

    # List batches with limit
    response = await async_client.batches.list(limit="2")

    assert hasattr(response, "object")
    assert response.object == "list"
    assert hasattr(response, "data")
    assert len(response.data) <= 2


@pytest.mark.asyncio
async def test_retrieve_batch(async_client):
    """Test retrieving a specific batch"""
    # Create a batch
    mock_file_id = "file-abc123"
    created_batch = await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )

    # Retrieve the batch
    retrieved_batch = await async_client.batches.retrieve(created_batch.id)

    assert retrieved_batch.id == created_batch.id
    assert retrieved_batch.object == "batch"
    assert retrieved_batch.endpoint == "/v1/chat/completions"
    assert retrieved_batch.input_file_id == mock_file_id


@pytest.mark.asyncio
async def test_retrieve_nonexistent_batch(async_client):
    """Test retrieving a non-existent batch"""
    try:
        await async_client.batches.retrieve("batch-nonexistent")
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "404" in str(e) or "not found" in str(e).lower()


@pytest.mark.asyncio
async def test_cancel_batch(async_client):
    """Test canceling a batch"""
    # Create a batch
    mock_file_id = "file-abc123"
    batch = await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )

    # Cancel the batch
    cancelled_batch = await async_client.batches.cancel(batch.id)

    assert cancelled_batch.id == batch.id
    assert cancelled_batch.status == "cancelled"


@pytest.mark.asyncio
async def test_cancel_nonexistent_batch(async_client):
    """Test canceling a non-existent batch"""
    try:
        await async_client.batches.cancel("batch-nonexistent")
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "404" in str(e) or "not found" in str(e).lower()


@pytest.mark.asyncio
async def test_cancel_completed_batch(async_client):
    """Test canceling a completed batch (should fail)"""
    # Create a batch
    mock_file_id = "file-abc123"
    batch = await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )

    # Cancel the batch first
    await async_client.batches.cancel(batch.id)

    # Try to cancel it again (should fail)
    try:
        await async_client.batches.cancel(batch.id)
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "400" in str(e) or "cannot cancel" in str(e).lower()


@pytest.mark.asyncio
async def test_batch_response_structure(async_client):
    """Test batch response structure"""
    # Create a batch
    mock_file_id = "file-abc123"
    batch = await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
        metadata={"test": "data"},
    )

    # Check batch structure
    assert hasattr(batch, "id")
    assert hasattr(batch, "object")
    assert hasattr(batch, "endpoint")
    assert hasattr(batch, "errors")
    assert hasattr(batch, "input_file_id")
    assert hasattr(batch, "completion_window")
    assert hasattr(batch, "status")
    assert hasattr(batch, "created_at")
    assert hasattr(batch, "in_progress_at")
    assert hasattr(batch, "expires_at")
    assert hasattr(batch, "finalizing_at")
    assert hasattr(batch, "completed_at")
    assert hasattr(batch, "request_counts")
    assert hasattr(batch, "metadata")

    # Check request_counts structure
    request_counts = batch.request_counts
    assert hasattr(request_counts, "total")
    assert hasattr(request_counts, "completed")
    assert hasattr(request_counts, "failed")

    # Check metadata
    assert batch.metadata["test"] == "data"


@pytest.mark.asyncio
async def test_batch_status_transitions(async_client):
    """Test batch status transitions"""
    # Create a batch
    mock_file_id = "file-abc123"
    batch = await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )

    # Check initial status
    assert batch.status in ["validating", "pending"]

    # Retrieve the batch to check status
    retrieved_batch = await async_client.batches.retrieve(batch.id)
    assert retrieved_batch.status in [
        "validating",
        "pending",
        "in_progress",
        "completed",
        "failed",
    ]


@pytest.mark.asyncio
async def test_batch_expiration(async_client):
    """Test batch expiration time"""
    # Create a batch
    mock_file_id = "file-abc123"
    batch = await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )

    # Check that expires_at is set and is in the future
    assert hasattr(batch, "expires_at")
    assert batch.expires_at > batch.created_at
    # Should expire in approximately 24 hours (86400 seconds)
    assert batch.expires_at - batch.created_at >= 86400 - 60  # Allow 1 minute tolerance


@pytest.mark.asyncio
async def test_batch_list_pagination(async_client):
    """Test batch list pagination structure"""
    # Create a batch
    mock_file_id = "file-abc123"
    await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )

    # List batches
    response = await async_client.batches.list()

    # Check pagination structure
    assert hasattr(response, "object")
    assert hasattr(response, "data")
    assert hasattr(response, "first_id")
    assert hasattr(response, "last_id")
    assert hasattr(response, "has_more")

    assert response.object == "list"
    assert isinstance(response.data, list)
    assert isinstance(response.has_more, bool)


@pytest.mark.asyncio
async def test_batch_with_default_parameters(async_client):
    """Test creating a batch with default parameters"""
    # Create a batch with minimal required parameters
    mock_file_id = "file-abc123"
    batch = await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",  # Required by OpenAI client
    )

    # Check that defaults are applied
    assert batch.completion_window == "24h"
    assert batch.metadata == {}
    assert batch.status in ["validating", "pending"]


@pytest.mark.asyncio
async def test_batch_error_handling(async_client):
    """Test batch error handling"""
    # Test with empty input_file_id - client enforces this
    try:
        await async_client.batches.create(
            input_file_id="",
            endpoint="/v1/chat/completions",
            completion_window="24h",
        )
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "input_file_id is required" in str(e) or "400" in str(e)


@pytest.mark.asyncio
async def test_batch_processing_integration(async_client):
    """Test batch processing integration with chat completions"""
    # This test would require actual file upload and processing
    # For now, we'll test the basic batch creation and status tracking

    # Create a batch
    mock_file_id = "file-abc123"
    batch = await async_client.batches.create(
        input_file_id=mock_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
        metadata={"test": "processing"},
    )

    # Verify batch was created with correct status
    assert batch.status in ["validating", "pending"]
    assert batch.endpoint == "/v1/chat/completions"
    assert batch.input_file_id == mock_file_id

    # Retrieve the batch to verify persistence
    retrieved_batch = await async_client.batches.retrieve(batch.id)
    assert retrieved_batch.id == batch.id
    assert retrieved_batch.status == batch.status

    # List batches to verify it appears in the list
    list_response = await async_client.batches.list()
    batch_ids = [b.id for b in list_response.data]
    assert batch.id in batch_ids
