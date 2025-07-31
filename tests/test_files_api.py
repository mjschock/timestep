import os

import openai
import pytest


@pytest.mark.asyncio
async def test_files_list(async_client):
    files_list_response = await async_client.files.list()
    assert hasattr(files_list_response, "object")
    assert files_list_response.object == "list"
    assert hasattr(files_list_response, "data")
    assert isinstance(files_list_response.data, list)
    for file_obj in files_list_response.data:
        assert hasattr(file_obj, "id")
        assert hasattr(file_obj, "object")
        assert file_obj.object == "file"
        assert hasattr(file_obj, "bytes")
        assert hasattr(file_obj, "created_at")
        assert hasattr(file_obj, "filename")
        assert hasattr(file_obj, "purpose")


@pytest.mark.asyncio
async def test_files_list_with_purpose_filter(async_client):
    """Test listing files with purpose filter"""
    files_list_response = await async_client.files.list(purpose="fine-tune")
    assert hasattr(files_list_response, "object")
    assert files_list_response.object == "list"
    assert hasattr(files_list_response, "data")
    assert isinstance(files_list_response.data, list)
    # All returned files should have the specified purpose
    for file_obj in files_list_response.data:
        assert file_obj.purpose == "fine-tune"


@pytest.mark.asyncio
async def test_files_list_with_limit(async_client):
    """Test listing files with limit parameter"""
    files_list_response = await async_client.files.list(limit=5)
    assert hasattr(files_list_response, "object")
    assert files_list_response.object == "list"
    assert hasattr(files_list_response, "data")
    assert isinstance(files_list_response.data, list)
    # Should not exceed the limit
    assert len(files_list_response.data) <= 5


@pytest.mark.asyncio
async def test_files_list_with_order(async_client):
    """Test listing files with order parameter"""
    files_list_response = await async_client.files.list(order="desc")
    assert hasattr(files_list_response, "object")
    assert files_list_response.object == "list"
    assert hasattr(files_list_response, "data")
    assert isinstance(files_list_response.data, list)


@pytest.mark.asyncio
async def test_files_upload_and_retrieve(async_client, sample_jsonl_file):
    # Upload
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    assert hasattr(upload_response, "id")
    assert upload_response.object == "file"
    assert upload_response.purpose == "fine-tune"
    assert upload_response.filename == os.path.basename(sample_jsonl_file)
    assert upload_response.status == "uploaded"
    file_id = upload_response.id
    # Retrieve
    retrieve_response = await async_client.files.retrieve(file_id)
    assert retrieve_response.id == file_id
    assert retrieve_response.filename == upload_response.filename
    assert retrieve_response.purpose == "fine-tune"
    assert retrieve_response.status == "uploaded"
    # Download
    content = await async_client.files.content(file_id)
    data = await content.aread()  # Read bytes from the response object
    with open(sample_jsonl_file, "rb") as f:
        original = f.read()
    assert data == original
    # Delete
    delete_response = await async_client.files.delete(file_id)
    assert delete_response.id == file_id
    assert delete_response.deleted is True
    # Confirm deleted
    with pytest.raises(openai.NotFoundError):
        await async_client.files.retrieve(file_id)
    with pytest.raises(openai.NotFoundError):
        await async_client.files.content(file_id)


@pytest.mark.asyncio
async def test_files_upload_different_purposes(async_client, sample_jsonl_file):
    """Test uploading files with different purposes"""
    purposes = ["fine-tune", "assistants"]

    for purpose in purposes:
        with open(sample_jsonl_file, "rb") as f:
            upload_response = await async_client.files.create(file=f, purpose=purpose)
        assert upload_response.purpose == purpose
        assert upload_response.status == "uploaded"

        # Clean up
        await async_client.files.delete(upload_response.id)


@pytest.mark.asyncio
async def test_files_upload_multiple_files(async_client, sample_jsonl_file):
    """Test uploading multiple files and listing them"""
    file_ids = []

    # Upload 3 files
    for _i in range(3):
        with open(sample_jsonl_file, "rb") as f:
            upload_response = await async_client.files.create(
                file=f, purpose="fine-tune"
            )
        file_ids.append(upload_response.id)
        assert upload_response.status == "uploaded"

    # List files and verify they exist
    files_list_response = await async_client.files.list()
    uploaded_ids = [f.id for f in files_list_response.data]

    for file_id in file_ids:
        assert file_id in uploaded_ids

    # Clean up
    for file_id in file_ids:
        await async_client.files.delete(file_id)


@pytest.mark.asyncio
async def test_files_retrieve_after_upload(async_client, sample_jsonl_file):
    """Test retrieving a file immediately after upload"""
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")

    file_id = upload_response.id

    # Retrieve immediately
    retrieve_response = await async_client.files.retrieve(file_id)
    assert retrieve_response.id == file_id
    assert retrieve_response.filename == upload_response.filename
    assert retrieve_response.purpose == "fine-tune"
    assert retrieve_response.status == "uploaded"

    # Clean up
    await async_client.files.delete(file_id)


@pytest.mark.asyncio
async def test_files_download_after_upload(async_client, sample_jsonl_file):
    """Test downloading a file immediately after upload"""
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")

    file_id = upload_response.id

    # Download immediately
    content = await async_client.files.content(file_id)
    data = await content.aread()

    with open(sample_jsonl_file, "rb") as f:
        original = f.read()
    assert data == original

    # Clean up
    await async_client.files.delete(file_id)


@pytest.mark.asyncio
async def test_files_error_cases(async_client):
    # Non-existent file
    bad_id = "file-doesnotexist"
    with pytest.raises(openai.NotFoundError):
        await async_client.files.retrieve(bad_id)
    with pytest.raises(openai.NotFoundError):
        await async_client.files.content(bad_id)
    with pytest.raises(openai.NotFoundError):
        await async_client.files.delete(bad_id)
    # Upload with missing file - OpenAI client rejects None before reaching server
    with pytest.raises(RuntimeError):
        await async_client.files.create(file=None, purpose="fine-tune")
    # (purpose missing is not possible with OpenAI client, but can be tested at HTTP level)


@pytest.mark.asyncio
async def test_files_error_cases_extended(async_client):
    """Test additional error cases"""
    # Test with various invalid file IDs
    # Note: OpenAI client rejects empty strings and some invalid formats before reaching server
    invalid_ids = ["invalid", "file-", "file-invalid-format"]

    for invalid_id in invalid_ids:
        with pytest.raises(openai.NotFoundError):
            await async_client.files.retrieve(invalid_id)
        with pytest.raises(openai.NotFoundError):
            await async_client.files.content(invalid_id)
        with pytest.raises(openai.NotFoundError):
            await async_client.files.delete(invalid_id)

    # Test empty string separately since OpenAI client rejects it before reaching server
    with pytest.raises(ValueError):
        await async_client.files.retrieve("")
    with pytest.raises(ValueError):
        await async_client.files.content("")
    with pytest.raises(ValueError):
        await async_client.files.delete("")


@pytest.mark.asyncio
async def test_files_list_pagination(async_client):
    """Test files list pagination parameters"""
    # Test with different limit values
    for limit in [1, 5, 10]:
        files_list_response = await async_client.files.list(limit=limit)
        assert len(files_list_response.data) <= limit

    # Test with different order values
    for order in ["asc", "desc"]:
        files_list_response = await async_client.files.list(order=order)
        assert hasattr(files_list_response, "data")
        assert isinstance(files_list_response.data, list)


@pytest.mark.asyncio
async def test_files_metadata_consistency(async_client, sample_jsonl_file):
    """Test that file metadata is consistent across operations"""
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")

    file_id = upload_response.id

    # Get metadata from list
    files_list_response = await async_client.files.list()
    file_from_list = next(
        (f for f in files_list_response.data if f.id == file_id), None
    )
    assert file_from_list is not None

    # Get metadata from retrieve
    retrieve_response = await async_client.files.retrieve(file_id)

    # Compare metadata
    assert file_from_list.id == retrieve_response.id
    assert file_from_list.filename == retrieve_response.filename
    assert file_from_list.purpose == retrieve_response.purpose
    assert file_from_list.status == retrieve_response.status
    assert file_from_list.bytes == retrieve_response.bytes
    assert file_from_list.created_at == retrieve_response.created_at

    # Clean up
    await async_client.files.delete(file_id)
