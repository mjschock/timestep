from typing import List

from openai.types import Model, ModelDeleted

from timestep.config import Settings
from timestep.services import agent_service

settings = Settings()


async def delete_model(model):  # noqa: E501
    """Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

     # noqa: E501

    :param model: The model to delete
    :type model: str

    :rtype: Union[DeleteModelResponse, Tuple[DeleteModelResponse, int], Tuple[DeleteModelResponse, int, Dict[str, str]]
    """
    model_id = await agent_service.delete_model(model_id=model)

    return ModelDeleted(
        id=str(model_id),
        deleted=True,
        object="model",
    ).model_dump(mode="json")


async def list_models():  # noqa: E501
    """Lists the currently available models, and provides basic information about each one such as the owner and availability.

     # noqa: E501


    :rtype: Union[ListModelsResponse, Tuple[ListModelsResponse, int], Tuple[ListModelsResponse, int, Dict[str, str]]
    """
    models = await agent_service.list_models()

    models: List[Model] = [
        Model(
            id=str(model.id),
            created=model.created_at.timestamp(),
            object="model",
            # owned_by=model.owned_by,
            owned_by=settings.openai_org_id,
        )
        for model in models
    ]

    return {
        "data": [model.model_dump(mode="json") for model in models],
        "object": "list",
    }


async def retrieve_model(model: str, token_info: dict, user: str):
    """Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

     # noqa: E501

    :param model: The ID of the model to use for this request
    :type model: str

    :rtype: Union[Model, Tuple[Model, int], Tuple[Model, int, Dict[str, str]]
    """
    model = await agent_service.retrieve_model(model_id=model)

    model: Model = Model(
        id=str(model.id),
        created=model.created_at.timestamp(),
        object="model",
        # owned_by=model.owned_by,
        owned_by=settings.openai_org_id,
    )

    return model.model_dump(mode="json")
