
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ready")
def get_ready():
    return {"ready": "ok"}

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
