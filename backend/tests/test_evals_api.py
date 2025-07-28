import pytest


@pytest.mark.asyncio
async def test_create_eval(async_client):
    """Test creating an evaluation"""
    response = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test_data.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    assert hasattr(response, "id")
    assert response.object == "eval"
    assert response.name == "Test Evaluation"
    assert hasattr(response, "created_at")
    assert hasattr(response, "updated_at")


@pytest.mark.asyncio
async def test_create_eval_missing_required_fields(async_client):
    """Test creating an evaluation with missing required fields"""
    # Test missing name
    try:
        await async_client.evals.create(
            data_source_config={"type": "jsonl", "path": "test.jsonl"},
            testing_criteria={"type": "accuracy"},
        )
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "name is required" in str(e) or "400" in str(e)

    # Test missing data_source_config - client enforces this
    try:
        await async_client.evals.create(
            name="Test Evaluation", testing_criteria={"type": "accuracy"}
        )
        raise AssertionError("Should have raised an error")
    except TypeError as e:
        assert "data_source_config" in str(e)
    except Exception as e:
        assert "data_source_config is required" in str(e) or "400" in str(e)

    # Test missing testing_criteria - client enforces this
    try:
        await async_client.evals.create(
            name="Test Evaluation",
            data_source_config={"type": "jsonl", "path": "test.jsonl"},
        )
        raise AssertionError("Should have raised an error")
    except TypeError as e:
        assert "testing_criteria" in str(e)
    except Exception as e:
        assert "testing_criteria is required" in str(e) or "400" in str(e)


@pytest.mark.asyncio
async def test_create_eval_invalid_eval_type(async_client):
    """Test creating an evaluation with invalid eval_type"""
    try:
        await async_client.evals.create(
            name="Test Evaluation",
            data_source_config={"type": "jsonl", "path": "test.jsonl"},
            testing_criteria={"type": "invalid_type"},
        )
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "eval_type must be one of" in str(e) or "400" in str(e)


@pytest.mark.asyncio
async def test_list_evals(async_client):
    """Test listing evaluations"""
    # First create an evaluation
    await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    # List evaluations
    response = await async_client.evals.list()

    assert hasattr(response, "object")
    assert response.object == "list"
    assert hasattr(response, "data")
    assert isinstance(response.data, list)
    assert len(response.data) >= 1


@pytest.mark.asyncio
async def test_list_evals_with_parameters(async_client):
    """Test listing evaluations with parameters"""
    # Create an evaluation
    await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    # List evaluations with limit
    response = await async_client.evals.list(limit=1)

    assert hasattr(response, "object")
    assert response.object == "list"
    assert hasattr(response, "data")
    assert len(response.data) <= 1


@pytest.mark.asyncio
async def test_get_eval(async_client):
    """Test retrieving a specific evaluation"""
    # Create an evaluation
    created_eval = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    # Retrieve the evaluation
    retrieved_eval = await async_client.evals.retrieve(created_eval.id)

    assert retrieved_eval.id == created_eval.id
    assert retrieved_eval.object == "eval"
    assert retrieved_eval.name == "Test Evaluation"
    assert retrieved_eval.eval_type == "accuracy"


@pytest.mark.asyncio
async def test_get_nonexistent_eval(async_client):
    """Test retrieving a non-existent evaluation"""
    try:
        await async_client.evals.retrieve("eval-nonexistent")
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "404" in str(e) or "not found" in str(e).lower()


@pytest.mark.asyncio
async def test_update_eval(async_client):
    """Test updating an evaluation"""
    # Create an evaluation
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    # Update the evaluation
    updated_eval = await async_client.evals.update(
        eval_record.id, name="Updated Evaluation"
    )

    assert updated_eval.id == eval_record.id
    assert updated_eval.name == "Updated Evaluation"


@pytest.mark.asyncio
async def test_delete_eval(async_client):
    """Test deleting an evaluation"""
    # Create an evaluation
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    # Delete the evaluation
    result = await async_client.evals.delete(eval_record.id)

    assert result.deleted is True

    # Verify it's deleted
    try:
        await async_client.evals.retrieve(eval_record.id)
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "404" in str(e) or "not found" in str(e).lower()


@pytest.mark.asyncio
async def test_create_eval_run(async_client):
    """Test creating an evaluation run"""
    # First create an evaluation
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    # Create an evaluation run with required parameters
    run = await async_client.evals.runs.create(
        eval_record.id, data_source={"type": "jsonl", "path": "test.jsonl"}
    )

    assert hasattr(run, "id")
    assert run.object == "eval_run"
    assert run.eval_id == eval_record.id
    assert run.status in ["pending", "in_progress", "completed", "failed", "cancelled"]
    assert hasattr(run, "created_at")


@pytest.mark.asyncio
async def test_create_eval_run_missing_model(async_client):
    """Test creating an evaluation run with missing model"""
    # First create an evaluation
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    # Try to create run without model - this should work now since we have a default
    run = await async_client.evals.runs.create(
        eval_record.id, data_source={"type": "jsonl", "path": "test.jsonl"}
    )

    assert hasattr(run, "id")
    assert run.object == "eval_run"
    assert run.eval_id == eval_record.id


@pytest.mark.asyncio
async def test_get_eval_runs(async_client):
    """Test getting evaluation runs"""
    # Create an evaluation and run
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    await async_client.evals.runs.create(
        eval_record.id, data_source={"type": "jsonl", "path": "test.jsonl"}
    )

    # Get evaluation runs
    response = await async_client.evals.runs.list(eval_record.id)

    assert hasattr(response, "object")
    assert response.object == "list"
    assert hasattr(response, "data")
    assert isinstance(response.data, list)
    assert len(response.data) >= 1


@pytest.mark.asyncio
async def test_get_eval_run(async_client):
    """Test retrieving a specific evaluation run"""
    # Create an evaluation and run
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    created_run = await async_client.evals.runs.create(
        eval_record.id, data_source={"type": "jsonl", "path": "test.jsonl"}
    )

    # Retrieve the run
    retrieved_run = await async_client.evals.runs.retrieve(
        created_run.id, eval_id=eval_record.id
    )

    assert retrieved_run.id == created_run.id
    assert retrieved_run.object == "eval_run"
    assert retrieved_run.eval_id == eval_record.id


@pytest.mark.asyncio
async def test_cancel_eval_run(async_client):
    """Test canceling an evaluation run"""
    # Create an evaluation and run
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    run = await async_client.evals.runs.create(
        eval_record.id, data_source={"type": "jsonl", "path": "test.jsonl"}
    )

    # Cancel the run
    cancelled_run = await async_client.evals.runs.cancel(run.id, eval_id=eval_record.id)

    assert cancelled_run.id == run.id
    assert cancelled_run.status == "cancelled"


@pytest.mark.asyncio
async def test_delete_eval_run(async_client):
    """Test deleting an evaluation run"""
    # Create an evaluation and run
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    run = await async_client.evals.runs.create(
        eval_record.id, data_source={"type": "jsonl", "path": "test.jsonl"}
    )

    # Delete the run
    result = await async_client.evals.runs.delete(run.id, eval_id=eval_record.id)

    assert result.deleted is True

    # Verify it's deleted
    try:
        await async_client.evals.runs.retrieve(run.id, eval_id=eval_record.id)
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "404" in str(e) or "not found" in str(e).lower()


@pytest.mark.asyncio
async def test_get_eval_run_output_items(async_client):
    """Test getting evaluation run output items"""
    # Create an evaluation and run
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    run = await async_client.evals.runs.create(
        eval_record.id, data_source={"type": "jsonl", "path": "test.jsonl"}
    )

    # Get output items
    response = await async_client.evals.runs.output_items.list(
        run.id, eval_id=eval_record.id
    )

    assert hasattr(response, "object")
    assert response.object == "list"
    assert hasattr(response, "data")
    assert isinstance(response.data, list)


@pytest.mark.asyncio
async def test_eval_response_structure(async_client):
    """Test evaluation response structure"""
    # Create an evaluation
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
        metadata={"test": "data"},
    )

    # Check evaluation structure
    assert hasattr(eval_record, "id")
    assert hasattr(eval_record, "object")
    assert hasattr(eval_record, "name")
    assert hasattr(eval_record, "description")
    assert hasattr(eval_record, "data_source_config")
    assert hasattr(eval_record, "testing_criteria")
    assert hasattr(eval_record, "eval_type")
    assert hasattr(eval_record, "status")
    assert hasattr(eval_record, "created_at")
    assert hasattr(eval_record, "updated_at")
    assert hasattr(eval_record, "metadata")

    # Check metadata
    assert eval_record.metadata["test"] == "data"


@pytest.mark.asyncio
async def test_eval_run_response_structure(async_client):
    """Test evaluation run response structure"""
    # Create an evaluation and run
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    run = await async_client.evals.runs.create(
        eval_record.id,
        data_source={"type": "jsonl", "path": "test.jsonl"},
        metadata={"test": "run_data"},
    )

    # Check run structure
    assert hasattr(run, "id")
    assert hasattr(run, "object")
    assert hasattr(run, "eval_id")
    assert hasattr(run, "model")
    assert hasattr(run, "status")
    assert hasattr(run, "created_at")
    assert hasattr(run, "metadata")

    # Check metadata
    assert run.metadata["test"] == "run_data"


@pytest.mark.asyncio
async def test_eval_status_transitions(async_client):
    """Test evaluation status transitions"""
    # Create an evaluation
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    # Check initial status
    assert eval_record.status in ["pending", "in_progress", "completed", "failed"]

    # Retrieve the evaluation to check status
    retrieved_eval = await async_client.evals.retrieve(eval_record.id)
    assert retrieved_eval.status in ["pending", "in_progress", "completed", "failed"]


@pytest.mark.asyncio
async def test_eval_run_status_transitions(async_client):
    """Test evaluation run status transitions"""
    # Create an evaluation and run
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    run = await async_client.evals.runs.create(
        eval_record.id, data_source={"type": "jsonl", "path": "test.jsonl"}
    )

    # Check initial status
    assert run.status in ["pending", "in_progress", "completed", "failed", "cancelled"]

    # Retrieve the run to check status
    retrieved_run = await async_client.evals.runs.retrieve(
        run.id, eval_id=eval_record.id
    )
    assert retrieved_run.status in [
        "pending",
        "in_progress",
        "completed",
        "failed",
        "cancelled",
    ]


@pytest.mark.asyncio
async def test_eval_list_pagination(async_client):
    """Test evaluation list pagination structure"""
    # Create an evaluation
    await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    # List evaluations
    response = await async_client.evals.list()

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
async def test_eval_run_list_pagination(async_client):
    """Test evaluation run list pagination structure"""
    # Create an evaluation and run
    eval_record = await async_client.evals.create(
        name="Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    await async_client.evals.runs.create(
        eval_record.id, data_source={"type": "jsonl", "path": "test.jsonl"}
    )

    # List runs
    response = await async_client.evals.runs.list(eval_record.id)

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
async def test_eval_with_different_types(async_client):
    """Test creating evaluations with different eval types"""
    eval_types = ["accuracy", "exact_match", "f1", "custom"]

    for eval_type in eval_types:
        eval_record = await async_client.evals.create(
            name=f"Test {eval_type} Evaluation",
            data_source_config={"type": "jsonl", "path": "test.jsonl"},
            testing_criteria={"type": eval_type},
        )

        assert eval_record.eval_type == eval_type
        assert eval_record.name == f"Test {eval_type} Evaluation"


@pytest.mark.asyncio
async def test_eval_integration_workflow(async_client):
    """Test complete evaluation workflow"""
    # 1. Create an evaluation
    eval_record = await async_client.evals.create(
        name="Integration Test Evaluation",
        data_source_config={"type": "jsonl", "path": "test.jsonl"},
        testing_criteria={"type": "accuracy"},
    )

    # 2. Verify evaluation was created
    assert eval_record.name == "Integration Test Evaluation"
    assert eval_record.eval_type == "accuracy"

    # 3. Create an evaluation run
    run = await async_client.evals.runs.create(
        eval_record.id, data_source={"type": "jsonl", "path": "test.jsonl"}
    )

    # 4. Verify run was created
    assert run.eval_id == eval_record.id

    # 5. List runs for the evaluation
    runs_response = await async_client.evals.runs.list(eval_record.id)
    run_ids = [r.id for r in runs_response.data]
    assert run.id in run_ids

    # 6. Get output items
    output_response = await async_client.evals.runs.output_items.list(
        run.id, eval_id=eval_record.id
    )
    assert hasattr(output_response, "data")

    # 7. Update the evaluation
    updated_eval = await async_client.evals.update(
        eval_record.id, name="Updated Integration Test Evaluation"
    )

    assert updated_eval.name == "Updated Integration Test Evaluation"

    # 8. Verify the update persisted
    retrieved_eval = await async_client.evals.retrieve(eval_record.id)
    assert retrieved_eval.name == "Updated Integration Test Evaluation"
