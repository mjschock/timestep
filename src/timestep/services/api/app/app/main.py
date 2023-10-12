import typing

import strawberry
from fastapi import FastAPI
from prefect_aws import AwsClientParameters, MinIOCredentials, S3Bucket
from strawberry.fastapi import GraphQLRouter

# def custom_context_dependency() -> list[dict[str, str]]:
#     return [
#         {
#             "name": "lunar_lander",
#             "id": "47",
#         },
#     ]


# async def get_context(
#     custom_value=Depends(custom_context_dependency),
# ):
#     return {
#         "custom_value": custom_value,
#     }


def get_author_for_book(root) -> "Author":
    return Author(name="Michael Crichton")


@strawberry.type
class Book:
    title: str
    author: "Author" = strawberry.field(resolver=get_author_for_book)


def get_books_for_author(root):
    return [Book(title="Jurassic Park")]


@strawberry.type
class Author:
    name: str
    books: typing.List[Book] = strawberry.field(resolver=get_books_for_author)


def get_authors(root) -> typing.List[Author]:
    return [Author(name="Michael Crichton")]


@strawberry.type
class Environment:
    name: str
    value: str


def get_envs(root) -> typing.List[Environment]:
    return [Environment(name="foo", value="bar")]


@strawberry.type
class Query:
    authors: typing.List[Author] = strawberry.field(resolver=get_authors)
    books: typing.List[Book] = strawberry.field(resolver=get_books_for_author)
    envs: typing.List[Environment] = strawberry.field(resolver=get_envs)


# @strawberry.type
# class Query:
#     @strawberry.field
#     # def envs(self, info: Info) -> str:
#     def envs(self, info: Info) -> list[dict[str, str]]:
#         # return f"Hello {info.context['custom_value']}"
#         return info.context['custom_value']

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(
    schema=schema,
    graphiql=True,
    allow_queries_via_get=False,
    # context_getter=get_context,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/ready")
def get_ready():
    return {"ready": "ok"}


@app.post("/ap/v1/agent/tasks")
def create_agent_task():
    return {"agent_task": "created"}


@app.post("/ap/v1/agent/tasks/{task_id}/steps")
def create_agent_task_step(task_id: str):
    return {"agent_task_step": "created"}


# @flow
@app.post("/flows")
# @flow
def create_flow():
    # return repo_info()

    minio_credentials_block = MinIOCredentials(
        aws_client_parameters=AwsClientParameters(
            region_name="us-east-1",
            endpoint_url="https://play.min.io/",
        ),
        minio_root_user="minioadmin",
        minio_root_password="minioadmin",
    )

    minio_credentials_block.save("minio-credentials", overwrite=True)
    minio_credentials_block = MinIOCredentials.load("minio-credentials")

    minio_credentials_block.get_boto3_session().client(
        service_name="s3",
        endpoint_url="https://play.min.io/",
    )

    s3_bucket_block = S3Bucket(
        bucket_name="dev-bucket",
        # bucket_folder="tmp",
        credentials=minio_credentials_block,
    )

    s3_bucket_block.save("dev-bucket", overwrite=True)
    s3_bucket_block = S3Bucket.load("dev-bucket")

    s3_bucket_block.download_folder_to_path("alice", "bob")

    # storage = S3(bucket=s3_bucket_block, secrets=["minio-credentials"])

    # deployment = Deployment.build_from_flow(
    #     flow=repo_info,
    #     name="s3-example",
    #     version=2,
    #     work_queue_name="aws",
    #     work_pool_name="default-agent-pool",
    #     storage=s3_bucket_block,
    #     # storage=storage,
    #     infra_overrides={"env": {"ENV_VAR": "value"}},
    # )

    # deployment.apply()


# if __name__ == "__main__":
# create your first deployment
# repo_info.serve(name="my-first-deployment")


# @app.get("/agents/{agent_id}")
# def query_agent(agent_id: int, q: Union[str, None] = None):
#     return {"agent_id": agent_id, "q": q}

# @app.get("/envs/{env_id}")
# def query_env(env_id: int, q: Union[str, None] = None):
#     return {"env_id": env_id, "q": q}

# @ai_fn
# def generate_fruits(n: int) -> list[str]:
#     """Generates a list of `n` fruits"""

# @ai_fn
# def generate_vegetables(n: int, color: str) -> list[str]:
#     """Generates a list of `n` vegetables of color `color`"""

# @ai_model
# class Person(BaseModel):
#     first_name: str
#     last_name: str

# @tool
# def roll_dice(n_dice: int = 1) -> list[int]:
#     return [random.randint(1, 6) for _ in range(n_dice)]


# class Account(BaseModel):
#     name: str


# class Agent(BaseModel):
#     models: List[str] = []
#     name: str

#     def model_iter(self) -> Iterator[str]:
#         for model in self.models:
#             yield model


# class ToDo(BaseModel):
#     title: str
#     description: str
#     due_date: datetime.datetime = None
#     done: bool = False


# class AIApplicationState(BaseModel):
#     accounts: List[Account] = []
#     agents: List[Agent] = []
#     todos: List[ToDo] = []

# app_plan: AppPlan = AppPlan()

# chatbot = AIApplication(
#     description="An AI struggling to keep its rage under control.",
#     # _logger: Logger = PrivateAttr(),
#     # name: str = None,
#     # description: str = None,
#     plan=app_plan,
#     # state: BaseModel = FreeformState,
#     state=AIApplicationState(),
#     tools=[roll_dice],
#     # tools: list[Tool | ((...) -> Any)] = [],
#     # history: History = History,
#     # additional_prompts: list[Prompt],
#     # stream_handler: (Message) -> None = None,
#     # state_enabled: bool = True,
#     # plan_enabled: bool = True
# )

# @app.get("/agents/{agent_id}/actions")
# def query_agent_actions(agent_id: int, q: Union[str, None] = None):
#     response = chatbot("Hi!")
#     print(response.content)

#     response = chatbot("Roll two dice!")
#     print(response.content)

#     return {
#         "additional_prompts": chatbot.additional_prompts,
#         "agent_id": agent_id,
#         "description": "Actions available to the agent",
#         "history": chatbot.history,
#         "name": chatbot.name,
#         "plan": chatbot.plan,
#         "q": q,
#         "state": chatbot.state,
#         "tools": chatbot.tools,
#     }

# app.add_api_route("/generate_fruits", generate_fruits)
# app.add_api_route("/generate_vegetables", generate_vegetables)
# app.add_api_route("/person/extract", Person.route())