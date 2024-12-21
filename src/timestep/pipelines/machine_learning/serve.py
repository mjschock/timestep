from typing import Dict

import torch
from fastapi import FastAPI
from ray import serve
from unsloth import FastVisionModel

torch._dynamo.config.disable = True

dtype = (
    None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
)
load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.
max_seq_length = 2048  # Supports RoPE Scaling interally, so choose any!
# max_seq_length = 4096 # Choose any! We auto support RoPE Scaling internally!


app = FastAPI()


# 2 Ray actors, each running on 1 vCPU.
@serve.deployment(
    num_replicas=1,
    # ray_actor_options={"num_cpus": 0.2, "num_gpus": 0.5},
    ray_actor_options={"num_gpus": 1},
)
@serve.ingress(app)
class ModelDeployment:

    def __init__(self, msg: str):
        self._msg = msg

        model_path = "/root/sky_workdir/lora_model"

        model, processor = FastVisionModel.from_pretrained(
            load_in_4bit=load_in_4bit,
            max_seq_length=max_seq_length,
            model_name=model_path,
        )

        FastVisionModel.for_inference(model)  # Enable native 2x faster inference

    # def __call__(self, request: requests.Request) -> Dict:
    #     del request  # unused
    #     return {'result': self._msg}

    # FastAPI will automatically parse the HTTP request for us.
    @app.get("/hello")
    def say_hello(self, name: str) -> str:
        # return f"Hello {name}!"
        return f"Hello {name} and {self._msg}!"


app = ModelDeployment.bind(msg="Hello Ray Serve!")
