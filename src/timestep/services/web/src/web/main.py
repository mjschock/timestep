import typing

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from .api import agent
from .db.env import envs_by_id

agents_by_id = {
    "default": {
        "agent_id": "default",
    },
}


@strawberry.type
class Agent:
    agent_id: str


@strawberry.type
class Environment:
    env_id: str
    agent_ids: typing.List[str]


def get_agent(root, agent_id: strawberry.ID) -> Agent:
    return Agent(**agents_by_id[agent_id])


def get_agents(root) -> typing.List[Agent]:
    return [get_agent(root, agent_id) for agent_id in ["default"]]


def get_env(root, env_id: strawberry.ID) -> Environment:
    return Environment(**envs_by_id[env_id])


def get_envs(root) -> typing.List[Environment]:
    return [get_env(root, env_id) for env_id in envs_by_id.keys()]


@strawberry.type
class Query:
    agent: Agent = strawberry.field(resolver=get_agent)
    agents: typing.List[Agent] = strawberry.field(resolver=get_agents)
    env: Environment = strawberry.field(resolver=get_env)
    envs: typing.List[Environment] = strawberry.field(resolver=get_envs)


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(
    schema=schema,
    graphiql=True,
    allow_queries_via_get=False,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

for env_id in envs_by_id.keys():
    env = get_env(None, env_id)

    for agent_id in env.agent_ids:
        app.include_router(agent.router, prefix=f"/envs/{env.env_id}/agents/{agent_id}")


@app.get("/ready")
def get_ready():
    return {
        "ready": "ok",
    }
