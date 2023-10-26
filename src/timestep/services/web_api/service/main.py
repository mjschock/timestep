import typing

import strawberry
from fastapi import FastAPI
from prefect import flow
from prefect_shell import shell_run_command
from strawberry.fastapi import GraphQLRouter

DEFAULT_DOCKER_IMAGE_REF = "registry.gitlab.com/timestep-ai/timestep/api:latest"

# def custom_context_dependency() -> list[dict[str, str]]:
#     return [
#         },


# async def get_context(
# ):
#     return {


# def get_author_for_book(root) -> "Author":


# @strawberry.type
# class Book:


# def get_books_for_author(root):


# @strawberry.type
# class Author:


# def get_authors(root) -> typing.List[Author]:


@strawberry.type
class Agent:
    name: str
    models: typing.List[str]


@strawberry.type
class Environment:
    id: str
    name: str
    description: str = ""
    agents: typing.List[Agent]


def get_agents(root) -> typing.List[Agent]:
    return [
        Agent(name="foo", models=["bar"]),
    ]


envs_by_id = {
    "0": {
        "name": "Cart Pole",
        # "description": "This environment corresponds to the version of the cart-pole problem described by Barto, Sutton, and Anderson in “Neuronlike Adaptive Elements That Can Solve Difficult Learning Control Problem”. A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The pendulum is placed upright on the cart and the goal is to balance the pole by applying forces in the left and right direction on the cart.",  # noqa: E501
        "agents": [
            {
                "name": "foo",
                "models": ["bar"],
            },
        ],
    },
    "1": {
        "name": "Lunar Lander",
        "agents": [
            {
                "name": "foo",
                "models": ["bar"],
            },
        ],
    },
    "2": {
        "name": "Mountain Car",
        "agents": [
            {
                "name": "foo",
                "models": ["bar"],
            },
        ],
    },
}


def get_envs(root) -> typing.List[Environment]:
    # return [

    return [Environment(id=id, **envs_by_id[id]) for id in envs_by_id]


def get_env(root, id: strawberry.ID) -> Environment:
    env = Environment(id=id, **envs_by_id[id])
    return env


@strawberry.type
class Query:
    agents: typing.List[Agent] = strawberry.field(resolver=get_agents)
    envs: typing.List[Environment] = strawberry.field(resolver=get_envs)
    env: Environment = strawberry.field(resolver=get_env)
    # @strawberry.field
    # def envs(self) -> list[dict[str, str]]:
    #     return [
    #         },

    # @strawberry.field
    # def envs(self, info: Info) -> str:
    # def envs(self, info: Info) -> list[dict[str, str]]:


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(
    schema=schema,
    graphiql=True,
    allow_queries_via_get=False,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

# @app.get("/")
# def read_root():


@app.get("/ready")
def get_ready():
    return {
        "ready": "ok",
    }


@app.post("/ap/v1/agent/tasks")
def create_agent_task():
    return {"agent_task": "created"}


@app.post("/ap/v1/agent/tasks/{task_id}/steps")
def create_agent_task_step(task_id: str):
    return {"agent_task_step": "created"}


@flow(log_prints=True)
def flow_example_shell_run_command_flow():
    print("=== flow_example_shell_run_command_flow (start) ===")

    output = shell_run_command(
        command="poetry run python echo_app.py",
        cwd="/home/ubuntu/src/timestep/services/api/app/app/flows",
        return_all=True,  # noqa: E501
    )

    print("output: ", output)

    print("=== flow_example_shell_run_command_flow (end) ===")

    return output


@flow
def deploy_example_shell_run_command_flow(docker_image_ref: str):
    return shell_run_command(
        command="poetry run prefect deploy --all",
        cwd="/app/app",
        env={"DOCKER_IMAGE_REF": docker_image_ref},
        return_all=True,
    )


@app.post("/flows")
def create_flow(docker_image_ref: str = DEFAULT_DOCKER_IMAGE_REF):
    resp = flow_example_shell_run_command_flow()

    print("resp: ", resp)

    return resp

    #         region_name="us-east-1",
    #     ),

    # # minio_credentials_block.get_boto3_session().client(

    # registry: PrefectObjectRegistry = load_deployments_from_yaml(


# if __name__ == "__main__":
# create your first deployment


# @app.get("/agents/{agent_id}")
# def query_agent(agent_id: int, q: Union[str, None] = None):

# @app.get("/envs/{env_id}")
# def query_env(env_id: int, q: Union[str, None] = None):

# @ai_fn
# def generate_fruits(n: int) -> list[str]:
#     """Generates a list of `n` fruits"""

# @ai_fn
# def generate_vegetables(n: int, color: str) -> list[str]:
#     """Generates a list of `n` vegetables of color `color`"""

# @ai_model
# class Person(BaseModel):

# @tool
# def roll_dice(n_dice: int = 1) -> list[int]:


# class Account(BaseModel):


# class Agent(BaseModel):

#     def model_iter(self) -> Iterator[str]:
#         for model in self.models:
#             yield model


# class ToDo(BaseModel):


# class AIApplicationState(BaseModel):


#     # tools: list[Tool | ((...) -> Any)] = [],
#     # additional_prompts: list[Prompt],
#     # stream_handler: (Message) -> None = None,

# @app.get("/agents/{agent_id}/actions")
# def query_agent_actions(agent_id: int, q: Union[str, None] = None):


#     return {
