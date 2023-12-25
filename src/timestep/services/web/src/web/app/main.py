import logging

from fastapi import FastAPI

# from web.app.local_dev import app as local_dev
# from .routers import agents
from .routers import agent

# from web.app.serve import hello

# def create_agent():
#     runtime_env = RuntimeEnv(
#         pip=[
#             # "accelerate>=0.16.0",
#             f"cloudpickle=={cloudpickle.__version__}",
#             f"einops=={einops.__version__}",
#             # "numpy<1.24",  # remove when mlflow updates beyond 2.2
#             # f"prefect_ray=={prefect_ray.__version__}",
#             f"pydantic=={pydantic.__version__}",
#             f"torch=={torch.__version__.replace('+cpu', '')}",
#             f"transformers=={transformers.__version__}",
#         ],
#         # env_vars={"ONEDNN_MAX_CPU_ISA": "AVX512_CORE_AMX"}
#     )

#     # https://docs.ray.io/en/releases-2.9.0/ray-core/api/doc/ray.init.html
#     # TODO: use RAY_ADDRESS
#     client_context: ClientContext = ray.init(
#         address="ray://ray-cluster-kuberay-head-svc.default.svc.cluster.local:10001",
#         runtime_env=runtime_env,
#     )
#     # TODO: storage (RAY_STORAGE)
#     # todo: _temp_dir

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

# logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup_event():
    # logger.debug("=== startup_event (BEGIN) ===")
    logging.info("=== startup complete ===")
    logger.info("=== startup complete ===")
    logging.getLogger("uvicorn").info("=== startup complete ===")
    logging.getLogger("uvicorn.access").info("=== startup complete ===")
    logging.getLogger("uvicorn.error").info("=== startup complete ===")
    logging.getLogger("uvicorn.asgi").info("=== startup complete ===")
    logging.getLogger().info("=== startup complete ===")
    print("=== startup complete ===")


# @flow
def get_ready_flow():
    return {
        "ready": "okay",
    }


@app.get("/ready")
async def get_ready():
    # TODO: https://kubernetes.io/docs/reference/using-api/health-checks/
    # Change to /livez and /readyz
    return get_ready_flow()


# handle: DeploymentHandle = serve.run(local_dev)
# serve.shutdown()  # Shuts down any running Serve app on the remote cluster
# handle: DeploymentHandle = serve.run(local_dev, host="0.0.0.0")

# try:
#     handle: DeploymentHandle = serve.run(local_dev, host="0.0.0.0")
#     ray.get(handle.say_hello.remote("Ray"))

# except Exception as e:
#     print('Caught Exception: ', e)
#     serve.shutdown()

# response: DeploymentResponse = handle.say_hello_twice.remote(name="Ray")
# assert response.result() == "Hello, Ray! Hello, Ray!"

# @app.get("/hello")
# async def hello(name: str="Ray"):
#     # response: DeploymentResponse = handle.say_hello_twice.remote(name=name)
#     response: DeploymentResponse = handle.say_hello.remote(name=name)
#     result = await response

#     return {
#         "message": result,
#     }

# @app.get("/hello2")
# async def hello2(name: str="Ray"):
#     response = requests.get(
#         "http://ray-cluster-kuberay-head-svc.default.svc.cluster.local:8000/", params={"name": name}  # noqa: E501
#     ).json()

#     return {
#         "message": response,
#     }

# async def say_hello(name: str) -> str:
#     return await hello(name)

app.include_router(agent.router)
# app.include_router(agents.router)
# app.include_router(users.router)
# app.include_router(items.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}

# agents_api = FastAPI()

# @agents_api.get("/agents")
# def read_sub():
#     return {"message": "Hello World from sub API"}

# @serve.deployment
# @serve.ingress(agents_api)
# class FastAPIDeployment:
#     # FastAPI will automatically parse the HTTP request for us.
#     @agents_api.get("/hello")
#     def say_hello(self, name: str) -> str:
#         return f"Hello {name}!"


# serve.run(FastAPIDeployment.bind(), route_prefix="/")

# app.mount("/api", agents_api)

# serve.run()
# serve.run()
