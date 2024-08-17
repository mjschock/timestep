import time
import uuid
from typing import Optional

from langchain_community.llms.llamafile import Llamafile
from openai.types.model import Model
from sqlalchemy import func
from sqlmodel import Field, Session, SQLModel, select

from timestep.config import settings
from timestep.database import (  # ModelAliasSQLModel,; ModelSQLModel,; create_db_and_tables,
    AgentSQLModel,
    engine,
)

app_dir = settings.app_dir
default_tools = []

# class AgentService(object):
#     # models: dict[uuid.UUID] = {}
#     _shared_instance_state = {
#         "models": {},
#     }

#     def __new__(cls, *args, **kwargs):
#         obj = super(AgentService, cls).__new__(cls, *args, **kwargs)
#         obj.__dict__ = cls._shared_instance_state

#         return obj


# class ModelInstanceStoreSingleton(object):
#     _shared_model_instances: dict[str] = {}

#     def __new__(cls, *args, **kwargs):
#         obj = super(ModelInstanceStoreSingleton, cls).__new__(cls, *args, **kwargs)
#         obj.__dict__ = cls._shared_model_instances

#         # create_db_and_tables()

#         # try:
#         #     obj.create_model(
#         #         model_aliases=[
#         #             "gpt-3.5-turbo",
#         #             "gpt-3.5-turbo-1106",
#         #             "gpt-4-1106-preview",
#         #             "gpt-4-turbo",
#         #             "gpt-4o",
#         #             "gpt-4o-mini",
#         #             "llamafile",
#         #             "LLaMA_CPP",
#         #         ],
#         #     )

#         # except Exception as e:
#         #     print(f"Error creating model: {e}")

#         return obj

#     def create_model(self, model_aliases=[]):
#         with Session(engine) as session:
#             model = ModelSQLModel()

#             session.add(model)

#             for model_alias in model_aliases:
#                 model_alias = ModelAliasSQLModel(alias=model_alias, model_id=model.id)

#                 session.add(model_alias)

#             session.commit()
#             session.refresh(model)

#         model_id = str(model.id)
#         model_instance = Llamafile(
#             base_url=f"http://{settings.default_llamafile_host}:{settings.default_llamafile_port}",
#         )

#         for model_id in [model_id] + model_aliases:
#             self._shared_model_instances[model_id] = model_instance

#         return model

#     def delete_model(self, model_id):
#         # with Session(engine) as session:
#         #     model = session.get(ModelSQLModel, uuid.UUID(model_id))

#         #     session.delete(model)
#         #     session.commit()

#         # for model_id in [model_id] + model.aliases:
#         #     self._shared_model_instances.pop(model_id)

#         return model_id

#     def get_model(self, model_id_or_alias):
#         model_id = None

#         # try:
#         #     model_id = uuid.UUID(model_id_or_alias)

#         # except ValueError:
#         #     model_alias = model_id_or_alias

#         # with Session(engine) as session:
#         #     if model_id:
#         #         model = session.get(ModelSQLModel, model_id)

#         #     else:
#         #         model_alias = session.get(ModelAliasSQLModel, model_alias)

#         #         if model_alias:
#         #             model = session.get(ModelSQLModel, model_alias.model_id)

#         #         else:
#         #             raise ValueError(f"Model not found: {model_id_or_alias}")


#         return model

#     def get_model_instance(self, model_id):
#         return self._shared_model_instances.get(model_id)

#     def get_models(self):
#         with Session(engine) as session:
#             # models = session.exec(select(ModelSQLModel)).all()
#             # SELECT DISTINCT(model) FROM agents ORDER BY model DESC;
#             models = session.exec(select(AgentSQLModel.model)).distinct().order_by(AgentSQLModel.model.desc()).all()

#         return models


# model_instance_store = ModelInstanceStoreSingleton()
# model_instance_store.created_at = time.time()

# model_instance_store.create_model(
#     model_aliases=[
#         "gpt-3.5-turbo",
#         "gpt-3.5-turbo-1106",
#         "gpt-4-1106-preview",
#         "gpt-4-turbo",
#         "gpt-4o",
#         "gpt-4o-mini",
#         "llamafile",
#         "LLaMA_CPP",
#     ],
# )


async def delete_agent(id):
    with Session(engine) as session:
        agent = session.get(AgentSQLModel, uuid.UUID(id))

        session.delete(agent)
        session.commit()

    return agent


# async def delete_model(model_id):
#     try:
#         model_instance_store.delete_model(model_id)

#     except ValueError as e:
#         print(f"Error deleting model: {e}")

#     return model_id


async def get_agent(id: str | None = None, model: str | None = None):
    with Session(engine) as session:
        # agent = session.get(AgentSQLModel, uuid.UUID(id))
        if id:
            agent = session.exec(
                select(AgentSQLModel).where(AgentSQLModel.id == uuid.UUID(id))
            ).first()

        elif model:
            # SELECT MIN(created_at) AS created_at FROM agents WHERE model = 'gpt-4-1106-preview';
            agent = session.exec(
                select(AgentSQLModel).where(AgentSQLModel.model == model)
            ).first()

    return agent


async def get_agents(
    token_info: dict,
    user: str,
    after: Optional[str] = None,
    before: Optional[str] = None,
    limit: int = 20,
    order: str = "desc",
):
    # with Session(engine) as session:
    #     agents = session.exec(select(AgentSQLModel)).all()

    with Session(engine) as session:
        if after:
            after_agent = session.exec(
                select(AgentSQLModel).where(AgentSQLModel.id == uuid.UUID(after))
            ).first()

            if after_agent:
                after_created_at = after_agent.created_at

            else:
                after_created_at = 0

        else:
            after_created_at = 0

        if before:
            before_agent = session.exec(
                select(AgentSQLModel).where(AgentSQLModel.id == uuid.UUID(before))
            ).first()

            if before_agent:
                before_created_at = before_agent.created_at

            else:
                before_created_at = func.now()

        else:
            before_created_at = func.now()

        statement = (
            select(AgentSQLModel)
            .where(
                AgentSQLModel.created_at.between(after_created_at, before_created_at),
            )
            .order_by(
                AgentSQLModel.created_at.desc()
                if order == "desc"
                else AgentSQLModel.created_at.asc()
            )
            .limit(limit)
        )

        results = session.exec(statement)
        agents = results.all()

    return agents


async def get_default_agent():
    raise NotImplementedError


async def insert_agent(body):
    description = body.get("description")
    instructions = body.get("instructions")
    # model_alias = body.get("model")
    model = body.get("model")
    name = body.get("name")
    tools = body.get("tools", default_tools)

    # model = await retrieve_model(model_alias)

    agent = AgentSQLModel(
        description=description,
        instructions=instructions,
        # models=[{"id": model_id} for model_id in [model.id] + model.aliases],
        # model_id=model.id,
        model=model,
        name=name,
        tools=tools,
    )

    with Session(engine) as session:
        session.add(agent)
        session.commit()
        session.refresh(agent)

    return agent


# async def list_models():
#     models = model_instance_store.get_models()

#     return models


async def update_agent(id, body):
    with Session(engine) as session:
        agent = session.get(AgentSQLModel, uuid.UUID(id))

        # if "model" in body:
        #     model = await retrieve_model(body.get("model"))
        #     agent.models = [{"id": model_id} for model_id in [model.id] + model.aliases]

        agent.description = body.get("description", agent.description)
        agent.instructions = body.get("instructions", agent.instructions)
        agent.model = body.get("model", agent.model)
        agent.name = body.get("name", agent.name)
        agent.tools = body.get("tools", agent.tools)

        session.add(agent)
        session.commit()
        session.refresh(agent)

    return agent


# async def retrieve_model(model_id):
#     model = model_instance_store.get_model(model_id)

#     return model
