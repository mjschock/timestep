import pytest


@pytest.mark.asyncio
async def test_create_upload(async_client):
    """Test creating an upload"""
    test_content = b"This is test content for upload API testing."
    response = await async_client.uploads.create(
        filename="test_upload.txt",
        purpose="assistants",
        bytes=len(test_content),
        mime_type="text/plain",
    )

    # Verify response structure
    assert hasattr(response, "id")
    assert hasattr(response, "object")
    assert hasattr(response, "bytes")
    assert hasattr(response, "created_at")
    assert hasattr(response, "filename")
    assert hasattr(response, "purpose")
    assert hasattr(response, "status")
    assert hasattr(response, "expires_at")
    assert hasattr(response, "mime_type")

    # Verify values
    assert response.filename == "test_upload.txt"
    assert response.purpose == "assistants"
    assert response.bytes == len(test_content)
    assert response.mime_type == "text/plain"
    assert response.status == "created"
    assert response.object == "upload"

    # Cancel the upload to clean up
    await async_client.uploads.cancel(response.id)


@pytest.mark.asyncio
async def test_add_upload_part(async_client):
    """Test adding a part to an upload"""
    test_content = b"This is test content for upload API testing."
    upload = await async_client.uploads.create(
        filename="test_upload.txt",
        purpose="assistants",
        bytes=len(test_content),
        mime_type="text/plain",
    )

    # Use the correct parameter structure with the required 'data' parameter
    response = await async_client.uploads.parts.create(
        upload_id=upload.id, data=test_content
    )

    # Verify response structure
    assert hasattr(response, "id")
    assert hasattr(response, "object")
    assert hasattr(response, "part_number")
    assert hasattr(response, "bytes")
    assert hasattr(response, "created_at")

    # Verify values
    assert response.part_number == 1
    assert response.bytes == len(test_content)
    assert response.object == "upload_part"

    # Clean up
    await async_client.uploads.cancel(upload.id)


@pytest.mark.asyncio
async def test_complete_upload(async_client):
    """Test completing an upload"""
    test_content = b"This is test content for upload API testing."
    upload = await async_client.uploads.create(
        filename="test_upload.txt",
        purpose="assistants",
        bytes=len(test_content),
        mime_type="text/plain",
    )

    part = await async_client.uploads.parts.create(
        upload_id=upload.id, data=test_content
    )

    response = await async_client.uploads.complete(
        upload_id=upload.id, part_ids=[part.id]
    )

    # Verify response structure
    assert hasattr(response, "id")
    assert hasattr(response, "object")
    assert hasattr(response, "status")
    assert hasattr(response, "file")

    # Verify values
    assert response.status == "completed"
    assert response.object == "upload"

    # Verify file object
    assert hasattr(response.file, "id")
    assert hasattr(response.file, "object")
    assert hasattr(response.file, "bytes")
    assert hasattr(response.file, "filename")
    assert hasattr(response.file, "purpose")
    assert hasattr(response.file, "status")

    assert response.file.object == "file"
    assert response.file.filename == "test_upload.txt"
    assert response.file.purpose == "assistants"
    assert response.file.bytes == len(test_content)
    assert response.file.status == "uploaded"

    # Clean up the created file
    await async_client.files.delete(response.file.id)


@pytest.mark.asyncio
async def test_cancel_upload(async_client):
    """Test cancelling an upload"""
    test_content = b"This is test content for upload API testing."
    upload = await async_client.uploads.create(
        filename="test_upload.txt",
        purpose="assistants",
        bytes=len(test_content),
        mime_type="text/plain",
    )

    response = await async_client.uploads.cancel(upload.id)

    # Verify response structure
    assert hasattr(response, "id")
    assert hasattr(response, "object")
    assert hasattr(response, "status")

    # Verify values
    assert response.status == "cancelled"
    assert response.object == "upload"


@pytest.mark.asyncio
async def test_multipart_upload(async_client):
    """Test uploading a file in multiple parts"""
    # Create content that's larger than a single part
    part1_content = b"First part of the file content. " * 1000  # ~30KB
    part2_content = b"Second part of the file content. " * 1000  # ~30KB
    total_content = part1_content + part2_content

    upload = await async_client.uploads.create(
        filename="multipart_test.txt",
        purpose="assistants",
        bytes=len(total_content),
        mime_type="text/plain",
    )

    # Add first part
    part1 = await async_client.uploads.parts.create(
        upload_id=upload.id, data=part1_content
    )

    # Add second part
    part2 = await async_client.uploads.parts.create(
        upload_id=upload.id, data=part2_content
    )

    # Complete upload with parts in order
    response = await async_client.uploads.complete(
        upload_id=upload.id, part_ids=[part1.id, part2.id]
    )

    # Verify completion
    assert response.status == "completed"
    assert response.file.bytes == len(total_content)

    # Clean up
    await async_client.files.delete(response.file.id)


@pytest.mark.asyncio
async def test_upload_validation(async_client):
    """Test upload validation errors"""
    # Test missing required fields - this is caught by the OpenAI client
    with pytest.raises(
        Exception
    ) as exc_info:  # TODO: Replace with specific exception if possible
        await async_client.uploads.create(
            filename="test.txt",
            # Missing purpose, bytes, mime_type
        )

    # The client validates this before sending to API
    assert "missing" in str(exc_info.value).lower()

    # Test invalid purpose - this should reach our API
    with pytest.raises(
        Exception
    ) as exc_info:  # TODO: Replace with specific exception if possible
        await async_client.uploads.create(
            filename="test.txt",
            purpose="invalid_purpose",
            bytes=100,
            mime_type="text/plain",
        )

    assert "400" in str(exc_info.value)

    # Test file too large - this should reach our API
    with pytest.raises(
        Exception
    ) as exc_info:  # TODO: Replace with specific exception if possible
        await async_client.uploads.create(
            filename="test.txt",
            purpose="assistants",
            bytes=9 * 1024 * 1024 * 1024,  # 9 GB
            mime_type="text/plain",
        )

    assert "400" in str(exc_info.value)


@pytest.mark.asyncio
async def test_part_validation(async_client):
    """Test part validation errors"""
    test_content = b"Test content"
    upload = await async_client.uploads.create(
        filename="test.txt",
        purpose="assistants",
        bytes=len(test_content),
        mime_type="text/plain",
    )

    # Test missing data - this is caught by the OpenAI client
    with pytest.raises(Exception) as exc_info:
        await async_client.uploads.parts.create(
            upload_id=upload.id,
            # Missing data
        )

    # The client validates this before sending to API
    assert "missing" in str(exc_info.value).lower()

    # Test duplicate part number (auto-assigned)
    await async_client.uploads.parts.create(upload_id=upload.id, data=test_content)

    # Add another part - should auto-assign part number 2
    await async_client.uploads.parts.create(upload_id=upload.id, data=test_content)

    # Clean up
    await async_client.uploads.cancel(upload.id)


@pytest.mark.asyncio
async def test_completion_validation(async_client):
    """Test completion validation errors"""
    test_content = b"Test content"
    upload = await async_client.uploads.create(
        filename="test.txt",
        purpose="assistants",
        bytes=len(test_content),
        mime_type="text/plain",
    )

    # Test completion without parts
    with pytest.raises(Exception) as exc_info:
        await async_client.uploads.complete(upload_id=upload.id, part_ids=[])

    assert "400" in str(exc_info.value)

    # Test completion with non-existent part
    with pytest.raises(Exception) as exc_info:
        await async_client.uploads.complete(
            upload_id=upload.id, part_ids=["non-existent-part-id"]
        )

    assert "400" in str(exc_info.value)

    # Clean up
    await async_client.uploads.cancel(upload.id)
