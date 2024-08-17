from typing import List

from openai.types import Model, ModelDeleted

from timestep.config import settings
from timestep.database import AgentSQLModel
from timestep.services import agent_service


# async def delete_model(*args, **kwargs):
async def delete_model(model: str, token_info: dict, user: str):
    """Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

    :param model: The model to delete
    :type model: str

    :rtype: Union[DeleteModelResponse, Tuple[DeleteModelResponse, int], Tuple[DeleteModelResponse, int, Dict[str, str]]
    """
    agents: List[AgentSQLModel] = [
        agent
        for agent in await agent_service.get_agents(
            limit=None, token_info=token_info, user=user
        )
        if agent.model == model
    ]

    for agent in agents:
        await agent_service.delete_agent(id=agent.id)

    return ModelDeleted(
        id=model,
        deleted=True,
        object="model",
    ).model_dump(mode="json")


async def list_models(token_info: dict, user: str):
    """Lists the currently available models, and provides basic information about each one such as the owner and availability.

    :rtype: Union[ListModelsResponse, Tuple[ListModelsResponse, int], Tuple[ListModelsResponse, int, Dict[str, str]]
    """
    # models = await agent_service.list_models()
    agents: List[AgentSQLModel] = await agent_service.get_agents(
        limit=None, token_info=token_info, user=user
    )
    # models: List[Model] = []
    models_by_id = {}

    for agent in agents:
        if agent.model not in models_by_id:
            models_by_id[agent.model] = Model(
                # id=str(model.id),
                id=str(agent.model),
                created=agent.created_at.timestamp(),
                object="model",
                # owned_by=model.owned_by,
                owned_by=settings.openai_org_id,
            )

        else:
            models_by_id[agent.model].created = min(
                models_by_id[agent.model].created, agent.created_at.timestamp()
            )

    models = list(models_by_id.values())

    # models: List[Model] = [
    #     Model(
    #         # id=str(model.id),
    #         id=str(agent.model),
    #         created=agent.created_at.timestamp(),
    #         object="model",
    #         # owned_by=model.owned_by,
    #         owned_by=settings.openai_org_id,
    #     )
    #     for agent in agents
    # ]

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
    # model = await agent_service.retrieve_model(model_id=model)
    agent: AgentSQLModel = await agent_service.get_agent(model=model)

    model: Model = Model(
        # id=str(model.id),
        # id=str(agent.id),
        id=str(agent.model),
        # created=model.created_at.timestamp(),
        created=agent.created_at.timestamp(),
        object="model",
        # owned_by=model.owned_by,
        owned_by=settings.openai_org_id,
    )

    return model.model_dump(mode="json")
