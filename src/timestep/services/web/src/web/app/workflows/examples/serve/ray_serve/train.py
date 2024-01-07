import os
import time

import ray
import requests
from fastapi import FastAPI
from prefect import flow, task
from prefect.logging import get_run_logger
from ray import serve

app = FastAPI()

ray.init(
    runtime_env={
        "pip": [
            "accelerate>=0.16.0",
            "transformers>=4.26.0",
            "numpy<1.24",  # remove when mlflow updates beyond 2.2
            "torch",
        ]
    }
)


model_id = "EleutherAI/gpt-j-6B"
revision = "float16"  # use float16 weights to fit in 16GB GPUs
prompt = (
    "In a shocking finding, scientists discovered a herd of unicorns living in a remote, "  # noqa: E501
    "previously unexplored valley, in the Andes Mountains. Even more surprising to the "
    "researchers was the fact that the unicorns spoke perfect English."
)


# @serve.deployment(ray_actor_options={"num_gpus": 0})
@serve.deployment
@serve.ingress(app)
class AgentDeployment:
    @app.get("/")
    def root(self):
        return "Hello, world!"

    # def __init__(self, model_id: str, revision: str = None):
    #     pass

    #     # import torch
    #     # from transformers import AutoModelForCausalLM, AutoTokenizer

    #     # self.model = AutoModelForCausalLM.from_pretrained(
    #     #     model_id,
    #     #     revision=revision,
    #     #     torch_dtype=torch.float16,
    #     #     low_cpu_mem_usage=True,
    #     #     device_map="auto",  # automatically makes use of all GPUs available to the Actor  # noqa: E501
    #     # )
    #     # self.tokenizer = AutoTokenizer.from_pretrained(model_id)

    # def generate(self, text: str) -> pd.DataFrame:
    #     pass

    #     # input_ids = self.tokenizer(text, return_tensors="pt").input_ids.to(
    #     #     self.model.device
    #     # )

    #     # gen_tokens = self.model.generate(
    #     #     input_ids,
    #     #     do_sample=True,
    #     #     temperature=0.9,
    #     #     max_length=100,
    #     # )
    #     # return pd.DataFrame(
    #     #     self.tokenizer.batch_decode(gen_tokens), columns=["responses"]
    #     # )

    # async def __call__(self, http_request: Request) -> str:
    #     # json_request: str = await http_request.json()
    #     # prompts = []
    #     # for prompt in json_request:
    #     #     text = prompt["text"]
    #     #     if isinstance(text, list):
    #     #         prompts.extend(text)
    #     #     else:
    #     #         prompts.append(text)
    #     # return self.generate(prompts)

    #     return [{'responses': 'In a shocking finding, scientists discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English.\n\nThe findings come from a recent expedition to the region of Cordillera del Divisor, in northern Peru. The region was previously known to have an unusually high number of native animals.\n\n"Our team was conducting a population census of the region’'}]  # noqa: E501


@task
def train_agent():
    logger = get_run_logger()

    cluster_resources = ray.cluster_resources()
    logger.info(f"Cluster resources: {cluster_resources}")

    available_resources = ray.available_resources()
    logger.info(f"Available resources: {available_resources}")

    deployment = AgentDeployment.bind(model_id=model_id, revision=revision)
    logger.info(f"Deployment: {deployment}")

    # Set resource limits (replace these values with your desired limits)
    # cpu_limit_seconds = 5  # 5 seconds CPU time limit
    # memory_limit_bytes = 100000000  # 100 MB memory limit

    # resource.setrlimit(resource.RLIMIT_CPU, (cpu_limit_seconds, cpu_limit_seconds))
    # resource.setrlimit(resource.RLIMIT_AS, (memory_limit_bytes, memory_limit_bytes))

    # handle = serve.run(deployment)
    handle = serve.run(deployment, route_prefix="/hello")
    logger.info(f"Handle: {handle}")

    # sample_input = {"text": prompt}

    # output = requests.post("http://localhost:8000/", json=[sample_input]).json()
    # logger.info(f"Output: {output}")

    resp = requests.get("http://localhost:8000/hello")
    assert resp.json() == "Hello, world!"

    # try:
    #     handle = serve.run(deployment)
    #     logger.info(f"Handle: {handle}")

    # except Exception as e:
    #     logger.error(f"Exception: {e}")

    # finally:
    #     logger.info("Resetting resource limits...")
    #     # Reset resource limits to default values
    #     resource.setrlimit(resource.RLIMIT_CPU, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))  # noqa: E501
    #     resource.setrlimit(resource.RLIMIT_AS, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))  # noqa: E501


@flow(
    log_prints=True,
)
def serve_agent():
    FLOW_RUN_ID = os.environ["FLOW_RUN_ID"]  # noqa: N806
    PREFECT_API_URL = os.environ["PREFECT_API_URL"]  # noqa: N806

    print(f"FLOW_RUN_ID: {FLOW_RUN_ID}")
    print(f"PREFECT_API_URL: {PREFECT_API_URL}")

    print("Training agent...")

    time.sleep(5)

    print("Training complete!")

    train_agent()


if __name__ == "__main__":
    serve_agent()
