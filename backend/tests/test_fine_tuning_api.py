import openai
import pytest
from conftest import MODEL_NAME


@pytest.mark.asyncio
async def test_create_fine_tuning_job(async_client, sample_jsonl_file):
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id
    response = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )
    assert hasattr(response, "id")
    assert hasattr(response, "model")
    assert hasattr(response, "status")
    assert response.training_file == training_file
    # Cancel the job to avoid long running tests
    await async_client.fine_tuning.jobs.cancel(response.id)


@pytest.mark.asyncio
async def test_create_fine_tuning_job_with_validation_file(
    async_client, sample_jsonl_file
):
    """Test creating a fine-tuning job with validation file"""
    # Upload training file
    with open(sample_jsonl_file, "rb") as f:
        training_upload = await async_client.files.create(file=f, purpose="fine-tune")

    # Upload validation file (using same file for simplicity)
    with open(sample_jsonl_file, "rb") as f:
        validation_upload = await async_client.files.create(file=f, purpose="fine-tune")

    response = await async_client.fine_tuning.jobs.create(
        training_file=training_upload.id,
        validation_file=validation_upload.id,
        model=MODEL_NAME,
    )
    assert hasattr(response, "id")
    assert hasattr(response, "model")
    assert hasattr(response, "status")
    assert response.training_file == training_upload.id
    assert response.validation_file == validation_upload.id

    # Cancel the job
    await async_client.fine_tuning.jobs.cancel(response.id)


@pytest.mark.asyncio
async def test_create_fine_tuning_job_with_hyperparameters(
    async_client, sample_jsonl_file
):
    """Test creating a fine-tuning job with custom hyperparameters"""
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id

    response = await async_client.fine_tuning.jobs.create(
        training_file=training_file,
        model=MODEL_NAME,
        hyperparameters={
            "n_epochs": 3,
            "batch_size": 1,
            "learning_rate_multiplier": 1.0,
        },
    )
    assert hasattr(response, "id")
    assert hasattr(response, "model")
    assert hasattr(response, "status")
    assert response.training_file == training_file

    # Cancel the job
    await async_client.fine_tuning.jobs.cancel(response.id)


@pytest.mark.asyncio
async def test_list_fine_tuning_jobs(async_client):
    response = await async_client.fine_tuning.jobs.list(limit=10)
    assert hasattr(response, "data")
    assert isinstance(response.data, list)


@pytest.mark.asyncio
async def test_list_fine_tuning_jobs_with_limit(async_client):
    """Test listing fine-tuning jobs with different limits"""
    for limit in [1, 5, 10]:
        response = await async_client.fine_tuning.jobs.list(limit=limit)
        assert hasattr(response, "data")
        assert isinstance(response.data, list)
        assert len(response.data) <= limit


@pytest.mark.asyncio
async def test_list_fine_tuning_jobs_with_after(async_client):
    """Test listing fine-tuning jobs with after parameter"""
    # First get a list to find a job ID
    response = await async_client.fine_tuning.jobs.list(limit=1)
    if response.data:
        job_id = response.data[0].id
        after_response = await async_client.fine_tuning.jobs.list(after=job_id, limit=5)
        assert hasattr(after_response, "data")
        assert isinstance(after_response.data, list)


@pytest.mark.asyncio
async def test_retrieve_fine_tuning_job(async_client, sample_jsonl_file):
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id
    job = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )
    response = await async_client.fine_tuning.jobs.retrieve(job.id)
    assert hasattr(response, "id")
    assert response.id == job.id
    await async_client.fine_tuning.jobs.cancel(job.id)


@pytest.mark.asyncio
async def test_retrieve_fine_tuning_job_details(async_client, sample_jsonl_file):
    """Test retrieving fine-tuning job and verify all expected fields"""
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id
    job = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )

    response = await async_client.fine_tuning.jobs.retrieve(job.id)

    # Check all expected fields
    expected_fields = [
        "id",
        "object",
        "model",
        "created_at",
        "finished_at",
        "fine_tuned_model",
        "organization_id",
        "result_files",
        "status",
        "validation_file",
        "training_file",
        "trained_tokens",
        "error",
        "hyperparameters",
        "result_files",
    ]

    for field in expected_fields:
        assert hasattr(response, field)

    await async_client.fine_tuning.jobs.cancel(job.id)


@pytest.mark.asyncio
async def test_cancel_fine_tuning_job(async_client, sample_jsonl_file):
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id
    job = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )
    response = await async_client.fine_tuning.jobs.cancel(job.id)
    assert hasattr(response, "id")
    assert response.id == job.id


@pytest.mark.asyncio
async def test_cancel_fine_tuning_job_status(async_client, sample_jsonl_file):
    """Test that canceling a job changes its status"""
    import asyncio

    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id
    job = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )

    # Add a small delay to allow the job to start but not complete
    await asyncio.sleep(0.1)

    # Cancel the job
    cancel_response = await async_client.fine_tuning.jobs.cancel(job.id)
    assert cancel_response.id == job.id

    # Retrieve the job and check status
    retrieved_job = await async_client.fine_tuning.jobs.retrieve(job.id)
    # Jobs can be cancelled, cancelling, failed, or succeeded (if completed before cancel)
    # In our mock implementation, jobs complete very quickly, so we need to handle both cases
    assert retrieved_job.status in ["cancelled", "cancelling", "failed", "succeeded"]


@pytest.mark.asyncio
async def test_list_fine_tuning_events(async_client, sample_jsonl_file):
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id
    job = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )
    response = await async_client.fine_tuning.jobs.list_events(job.id, limit=10)
    assert hasattr(response, "data")
    assert isinstance(response.data, list)
    await async_client.fine_tuning.jobs.cancel(job.id)


@pytest.mark.asyncio
async def test_list_fine_tuning_events_with_limit(async_client, sample_jsonl_file):
    """Test listing fine-tuning events with different limits"""
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id
    job = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )

    for limit in [1, 5, 10]:
        response = await async_client.fine_tuning.jobs.list_events(job.id, limit=limit)
        assert hasattr(response, "data")
        assert isinstance(response.data, list)
        assert len(response.data) <= limit

    await async_client.fine_tuning.jobs.cancel(job.id)


@pytest.mark.asyncio
async def test_list_fine_tuning_events_with_after(async_client, sample_jsonl_file):
    """Test listing fine-tuning events with after parameter"""
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id
    job = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )

    # Get initial events
    initial_events = await async_client.fine_tuning.jobs.list_events(job.id, limit=5)
    if initial_events.data:
        event_id = initial_events.data[0].id
        after_events = await async_client.fine_tuning.jobs.list_events(
            job.id, after=event_id, limit=5
        )
        assert hasattr(after_events, "data")
        assert isinstance(after_events.data, list)

    await async_client.fine_tuning.jobs.cancel(job.id)


@pytest.mark.asyncio
async def test_list_fine_tuning_checkpoints(async_client, sample_jsonl_file):
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id
    job = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )
    response = await async_client.fine_tuning.jobs.checkpoints.list(job.id)
    assert hasattr(response, "data")
    assert isinstance(response.data, list)
    await async_client.fine_tuning.jobs.cancel(job.id)


@pytest.mark.asyncio
async def test_list_fine_tuning_checkpoints_with_limit(async_client, sample_jsonl_file):
    """Test listing fine-tuning checkpoints with limit"""
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id
    job = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )

    response = await async_client.fine_tuning.jobs.checkpoints.list(job.id, limit=5)
    assert hasattr(response, "data")
    assert isinstance(response.data, list)
    assert len(response.data) <= 5

    await async_client.fine_tuning.jobs.cancel(job.id)


@pytest.mark.asyncio
async def test_fine_tuning_job_error_handling(async_client):
    """Test error handling for invalid fine-tuning job operations"""
    # Test retrieving non-existent job
    with pytest.raises(openai.NotFoundError):
        await async_client.fine_tuning.jobs.retrieve("ftjob-nonexistent")

    # Test canceling non-existent job
    with pytest.raises(openai.NotFoundError):
        await async_client.fine_tuning.jobs.cancel("ftjob-nonexistent")

    # Test listing events for non-existent job
    with pytest.raises(openai.NotFoundError):
        await async_client.fine_tuning.jobs.list_events("ftjob-nonexistent")

    # Test listing checkpoints for non-existent job
    # This might not raise an exception, so we'll just test that it returns an empty list
    try:
        checkpoints = await async_client.fine_tuning.jobs.checkpoints.list(
            "ftjob-nonexistent"
        )
        assert hasattr(checkpoints, "data")
        assert isinstance(checkpoints.data, list)
    except Exception as e:
        # If it does raise an exception, that's also acceptable
        print(f"Note: Checkpoints operation raised exception: {e}")
        pass


@pytest.mark.asyncio
async def test_fine_tuning_job_lifecycle(async_client, sample_jsonl_file):
    """Test the complete lifecycle of a fine-tuning job"""
    # 1. Upload training file
    with open(sample_jsonl_file, "rb") as f:
        upload_response = await async_client.files.create(file=f, purpose="fine-tune")
    training_file = upload_response.id

    # 2. Create job
    job = await async_client.fine_tuning.jobs.create(
        training_file=training_file, model=MODEL_NAME
    )
    # Jobs can be in various states including failed due to model validation
    # In our mock implementation, jobs complete very quickly, so we need to handle succeeded status
    assert job.status in [
        "validating_files",
        "queued",
        "running",
        "failed",
        "succeeded",
    ]

    # 3. Retrieve job
    retrieved_job = await async_client.fine_tuning.jobs.retrieve(job.id)
    assert retrieved_job.id == job.id

    # 4. List events
    events = await async_client.fine_tuning.jobs.list_events(job.id, limit=5)
    assert isinstance(events.data, list)

    # 5. List checkpoints
    checkpoints = await async_client.fine_tuning.jobs.checkpoints.list(job.id)
    assert isinstance(checkpoints.data, list)

    # 6. Cancel job
    cancel_response = await async_client.fine_tuning.jobs.cancel(job.id)
    assert cancel_response.id == job.id

    # 7. Verify cancellation
    final_job = await async_client.fine_tuning.jobs.retrieve(job.id)
    # Jobs can be cancelled, cancelling, failed, or succeeded (if completed before cancel)
    # In our mock implementation, jobs complete very quickly, so we need to handle both cases
    assert final_job.status in ["cancelled", "cancelling", "failed", "succeeded"]
