import pytest
from conftest import MODEL_NAME


@pytest.mark.asyncio
async def test_models_list(async_client):
    models_list_response = await async_client.models.list()
    assert hasattr(models_list_response, "object")
    assert models_list_response.object == "list"
    assert hasattr(models_list_response, "data")
    assert isinstance(models_list_response.data, list)
    for model_obj in models_list_response.data:
        assert hasattr(model_obj, "id")
        assert hasattr(model_obj, "object")
        assert model_obj.object == "model"
        assert hasattr(model_obj, "created")
        assert hasattr(model_obj, "owned_by")


@pytest.mark.asyncio
async def test_model_retrieve(async_client):
    model_metadata = await async_client.models.retrieve(MODEL_NAME)
    assert hasattr(model_metadata, "id")
    assert hasattr(model_metadata, "object")
    assert model_metadata.object == "model"
    assert hasattr(model_metadata, "created")
    assert hasattr(model_metadata, "owned_by")
