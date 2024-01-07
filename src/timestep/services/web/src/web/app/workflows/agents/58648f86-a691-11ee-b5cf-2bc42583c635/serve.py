from typing import List

import pydantic
import torch
from fastapi import FastAPI
from prefect import flow
from prefect_shell import ShellOperation
from ray import serve
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    LocalAgent,
    set_seed,
)

set_seed(42)

torch_device = "cuda" if torch.cuda.is_available() else "cpu"

# 1: Define a FastAPI app and wrap it in a deployment with a route handler.
app = FastAPI()


hf_user_access_token = None


# @serve.deployment
# class AgentDeployment:


class Message(pydantic.BaseModel):
    content: str
    role: str


@serve.deployment
@serve.ingress(app)
class FastAPIDeployment:  # AgentDeployer?
    def __init__(self) -> None:
        # torch_device = "cuda" if torch.cuda.is_available() else "cpu"

        tokenizer = AutoTokenizer.from_pretrained("gpt2")

        model = AutoModelForCausalLM.from_pretrained(
            "gpt2",
            pad_token_id=tokenizer.eos_token_id,
            # torch_dtype=torch.bfloat16,
        ).to(torch_device)

        self.model = model
        self.tokenizer = tokenizer

        self.agent = LocalAgent(
            self.model,
            self.tokenizer,
            additional_tools=None,
            chat_prompt_template=None,
            run_prompt_template=None,
        )

        self.model.save_pretrained("dummy")
        self.tokenizer.save_pretrained("dummy")

    @app.post("/v1/chat/completions")
    async def chat(self, messages: List[Message], model: str = "gpt-2"):
        # https://huggingface.co/blog/how-to-generate
        print("=== chat ===")
        # print('text:', text)
        print("messages:", messages)

        # model_inputs = self.tokenizer(text, return_tensors='pt').to(torch_device)
        model_inputs = self.tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt"
        ).to(
            torch_device
        )  # noqa: E501
        input_length = model_inputs.shape[1]
        # sample_outputs = self.model.generate(
        #     **model_inputs,
        #     do_sample=True,
        #     max_new_tokens=40,
        #     num_return_sequences=3,
        #     top_k=50,
        #     top_p=0.95,
        # )
        generated_ids = self.model.generate(
            model_inputs, do_sample=True, max_new_tokens=20
        )  # noqa: E501

        decoded_sample_outputs = []

        print("Output:\n" + 100 * "-")
        # for i, sample_output in enumerate(sample_outputs):
        #     decoded_sample_output = self.tokenizer.decode(sample_output, skip_special_tokens=True)  # noqa: E501
        #     print("{}: {}".format(i, decoded_sample_output))
        #     decoded_sample_outputs.append(decoded_sample_output)
        decoded_sample_output = self.tokenizer.batch_decode(
            generated_ids[:, input_length:], skip_special_tokens=True
        )[
            0
        ]  # noqa: E501
        print("{}: {}".format(0, decoded_sample_output))
        decoded_sample_outputs.append(decoded_sample_output)

        # return {
        #     "decoded_sample_outputs": decoded_sample_outputs,
        # }

        return {
            # "id": "chatcmpl-123",
            # "object": "chat.completion",
            # "created": 1677652288,
            # "model": "gpt-3.5-turbo-0613",
            # "system_fingerprint": "fp_44709d6fcb",
            "choices": [
                {
                    # "index": 0,
                    "message": {
                        "role": "assistant",
                        # "content": "\n\nHello there, how may I assist you today?",
                        "content": decoded_sample_output,
                    },
                    # "logprobs": null,
                    # "finish_reason": "stop"
                }
            ],
            # "usage": {
            #     "prompt_tokens": 9,
            #     "completion_tokens": 12,
            #     "total_tokens": 21
            # }
        }

        # print("Output:\n" + 100 * '-')
        # print(self.tokenizer.decode(greedy_output[0], skip_special_tokens=True))

        # print('agent.run(text):', self.agent.run(text, return_code=True))

        # return self.tokenizer.decode(greedy_output[0], skip_special_tokens=True)

        # encoded_input = self.tokenizer(text, return_tensors='pt')
        # print('encoded_input:', encoded_input)

        # output = self.model(**encoded_input)

        # print('output:', output)

        # return output

        # self.apps = {} # AIApplication from Marvin?
        # self.agents = {} # Agent Protocol testing suite
        # self.envs = {} # PettingZooEnv testing suite
        # self.models = {}
        # self.tokenizers = {}
        # self.trainers = {}

        # self.agent = None
        # self.model = None
        # self.tokenizer = None

        # self.agents: Dict[str, transformers.Agent] = { # transformers.Agent
        #     # "OpenAIAgent": OpenAiAgent(model="text-davinci-003", api_key="<your_api_key>"),  # noqa: E501
        #     "OpenAssistantAgent": HfAgent(
        #         token=hf_user_access_token,
        #         url_endpoint="https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5",
        #     ),
        #     "StarcoderAgent": HfAgent(
        #         token=hf_user_access_token,
        #         url_endpoint="https://api-inference.huggingface.co/models/bigcode/starcoder",
        #     ),
        #     "StarcoderBaseAgent": HfAgent(
        #         token=hf_user_access_token,
        #         url_endpoint="https://api-inference.huggingface.co/models/bigcode/starcoder-base"
        #     ),
        # }

        # # self.apps = {}

        # self.models = {
        #     "OpenAssistantAgent": None,
        #     "StarcoderAgent": None,
        #     "StarcoderBaseAgent": None,
        # }

        # self.tokenizers = {
        #     "OpenAssistantAgent": None,
        #     "StarcoderAgent": None,
        #     "StarcoderBaseAgent": None,
        # }

        # self.tools = {
        #     "SimpleCalculatorTool": load_tool("ybelkada/simple-calculator"),
        # }

    @app.post("/monitor")
    async def monitor(self):
        # lm_eval --model local-chat-completions --tasks gsm8k --model_args model=facebook/opt-125m,base_url=http://{yourip}:8000/v1

        @flow
        async def monitor_flow():
            async with ShellOperation(
                commands=[
                    "pwd",
                    "ls -al",
                    "ls -al dummy",
                    "lm_eval --model local-chat-completions --tasks gsm8k --model_args pretrained=dummy,base_url=http://localhost:8000/v1",
                    # "lm_eval --help",
                    # "curl -O https://masie_web.apps.nsidc.org/pub/DATASETS/NOAA/G02135/north/daily/data/N_seaice_extent_daily_v3.0.csv",
                ],
                # working_dir=f"data/{today}",
            ) as shell_operation:
                # trigger runs the process in the background
                shell_operation_process = await shell_operation.trigger()

                # then do other things here in the meantime, like download another file
                # ...

                # when you're ready, wait for the process to finish
                await shell_operation_process.wait_for_completion()

                # if you'd like to get the output lines, you can use the `fetch_result` method  # noqa: E501
                output_lines = await shell_operation_process.fetch_result()

                print("output_lines:", output_lines)

        await monitor_flow()

        return {
            "ok": True,
        }

    @app.post("/train")
    async def train(self):
        # lm
        # https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md#external-library-usage

        # 1. load a pretrained model
        # model = AutoModelForCausalLMWithValueHead.from_pretrained("gpt2")
        # model_ref = AutoModelForCausalLMWithValueHead.from_pretrained("gpt2")
        # tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        # tokenizer.pad_token = tokenizer.eos_token

        # # 2. initialize trainer
        # ppo_config = {"batch_size": 1}
        # config = PPOConfig(**ppo_config)
        # ppo_trainer = PPOTrainer(config, model, model_ref, tokenizer)

        # # 3. encode a query
        # query_txt = "This morning I went to the "
        # query_tensor = tokenizer.encode(query_txt, return_tensors="pt").to(model.pretrained_model.device)  # noqa: E501

        # # 4. generate model response
        # generation_kwargs = {
        #     "min_length": -1,
        #     "top_k": 0.0,
        #     "top_p": 1.0,
        #     "do_sample": True,
        #     "pad_token_id": tokenizer.eos_token_id,
        #     "max_new_tokens": 20,
        # }
        # response_tensor = ppo_trainer.generate([item for item in query_tensor], return_prompt=False, **generation_kwargs)  # noqa: E501
        # response_txt = tokenizer.decode(response_tensor[0])
        # print(f"Query: {query_txt} \nResponse: {response_txt}")

        # # 5. define a reward for response
        # # (this could be any reward such as human feedback or output from another model)  # noqa: E501
        # reward = [torch.tensor(1.0, device=model.pretrained_model.device)]

        # # 6. train model with ppo
        # train_stats = ppo_trainer.step([query_tensor[0]], [response_tensor[0]], reward)  # noqa: E501
        # # print(f"Training stats: {train_stats}")

        return {
            "ok": True,
        }

    # @app.post("/envs")
    # async def create_env(self):
    # Create a TextEnvironment with a model, tokenizer, reward_fn, tools, and prompt
    # https://huggingface.co/docs/trl/text_environments
    #     text_env = TextEnvironemnt(
    #         model=model,
    #         tokenizer=tokenizer,
    #         tools= {"SimpleCalculatorTool": load_tool("ybelkada/simple-calculator")},
    #         reward_fn=exact_match_reward,
    #         prompt=prompt,
    #         max_turns=1
    #         max_tool_response=100
    #         generation_kwargs={"do_sample": "true"}
    #     )

    #     self.envs[]

    # @app.post("/train")
    # async def train(self):
    #     # Step 0. Make sure deepspeed is installed and configured
    #     # Step 1. Train Supervised Fine-Tuning (SFT) model using SFTTrainer - to ensure the data we train on is in-distribution for the PPO algorithm  # noqa: E501
    #     # Step 2. Train a reward model using RewardTrainer - to optimize the SFT model using the PPO algorithm  # noqa: E501
    #     # Step 3. PPOTrainer
    #     pass

    # @app.post("/models")
    # async def create_models(
    #     self,
    #     pretrained_model_name_or_path: str = "EleutherAI/gpt-neo-125m",
    #     # revision: str = "main",
    #     revision: str = "float16",
    # ):
    # checkpoint = "EleutherAI/gpt-j-6B"
    # checkpoint = "bigcode/starcoder"
    # checkpoint = "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5"

    # model = AutoModelForCausalLM.from_pretrained(
    #     # https://huggingface.co/docs/transformers/v4.36.1/en/model_doc/auto#transformers.FlaxAutoModelForVision2Seq.from_pretrained
    #     # checkpoint, # name_or_path
    #     pretrained_model_name_or_path=pretrained_model_name_or_path,
    #     revision=revision,
    #     # torch_dtype=torch.bfloat16,
    #     torch_dtype=torch.float16,
    #     low_cpu_mem_usage=True,
    #     device_map="auto",
    #     resume_download=True,
    # )
    # tokenizer = AutoTokenizer.from_pretrained(
    #     # https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoTokenizer.from_pretrained
    #     pretrained_model_name_or_path=pretrained_model_name_or_path,
    #     resume_download=True,
    #     # revision=revision,
    # )

    # self.agents[checkpoint] = LocalAgent(model, tokenizer)
    # self.envs[checkpoint] = TextEnvironment(
    # self.models[checkpoint] = model
    # self.tokenizers[checkpoint] = tokenizer
    # self.trainers[checkpoint] = PPOTrainer(model, tokenizer)

    # model = AutoModelForCausalLM.from_pretrained("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")  # noqa: E501
    # tokenizer = AutoTokenizer.from_pretrained("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")  # noqa: E501

    # model = AutoModelForCausalLMWithValueHead.from_pretrained("ybelkada//var/tmp/tmppugfzd45/ybelkada/gpt-neo-125m-detoxified-small-context")  # noqa: E501
    # tokenizer = AutoTokenizer.from_pretrained("ybelkada//var/tmp/tmppugfzd45/ybelkada/gpt-neo-125m-detoxified-small-context")  # noqa: E501
    # model = AutoModelForCausalLM.from_pretrained("ybelkada/gpt-neo-125m-detox")
    # tokenizer = AutoTokenizer.from_pretrained("ybelkada/gpt-neo-125m-detox")

    # if tokenizer.pad_token is None:
    # tokenizer.pad_token = tokenizer.eos_token

    # self.model = model
    # self.tokenizer = tokenizer

    # self.agent = LocalAgent(
    #     self.model,
    #     self.tokenizer,
    #     additional_tools=None,
    #     chat_prompt_template=None,
    #     run_prompt_template=None,
    # )

    # self.agents["TimestepAIAgent"] = self.agent

    # return {
    #     "model": model,
    #     "tokenizer": tokenizer,
    # }

    # return {
    # 'ok': True,
    # }

    # return f"Registered model {checkpoint}"

    # https://en.wikipedia.org/wiki/Ensemble_learning
    # model_ensemble = ray.util.collective.Ensemble(
    #     [model],
    #     world_size=1,
    #     backend="nccl",
    #     group_name="model_ensemble",
    # )

    # self.agent = LocalAgent(model_ensemble, tokenizer)

    # agent = LocalAgent.from_pretrained("bigcode/starcoder", device_map="auto", torch_dtype=torch.bfloat16)  # noqa: E501
    # agent = LocalAgent(model, tokenizer)
    # agent.run("Draw me a picture of rivers and lakes.")
    # https://huggingface.co/docs/transformers/v4.36.1/en/main_classes/agent#transformers.Agent

    # agent.chat("Draw me a picture of rivers and lakes")
    # agent.chat("Transform the picture so that there is a rock in there")

    # self.trainers[tokenizer] = PPOTrainer(
    #     model=self.models[tokenizer],
    #     tokenizer=self.tokenizers[tokenizer],
    #     num_shared_layers=4,
    # )

    # https://huggingface.co/docs/trl/learning_tools
    # env = TextEnvironment(
    #     model,
    #     tokenizer,
    #     {"SimpleCalculatorTool": tool_fn},
    #     reward_fn,
    #     prompt,
    #     generation_kwargs=generation_kwargs,
    # )

    # return f"Registered model {tokenizer}"

    # async def task_handler(task: Task) -> None:
    #     # TODO: Create initial step(s) for the task
    #     await Agent.db.create_step(task.task_id, ...)

    # async def step_handler(step: Step) -> Step:
    #     # TODO: handle next step
    #     if step.name == "print":
    #         print(step.input)
    #         step.is_last = True

    #     step.output = "Output from the agent"
    #     return step

    # def generate(self, text: str) -> pd.DataFrame:
    #     input_ids = self.tokenizer(text, return_tensors="pt").input_ids.to(
    #         self.model.device
    #     )

    #     gen_tokens = self.model.generate(
    #         input_ids,
    #         do_sample=True,
    #         temperature=0.9,
    #         max_length=100,
    #     )

    #     return pd.DataFrame(
    #         self.tokenizer.batch_decode(gen_tokens), columns=["responses"]
    #     )

    # @app.post("/chat")
    # async def chat(
    #     self,
    #     task: str,
    #     return_code: bool = False
    # ):
    #     print('task:', task)

    #     # if self.model is None:
    #     #     return {
    #     #         "links": {
    #     #             "models": "/models",
    #     #         },
    #     #     }

    #     response = self.agents["OpenAssistantAgent"].run(task, return_code=return_code)  # noqa: E501

    #     print('chat; response:', response)

    #     return {
    #         "message": response,
    #     }

    # return {
    #     f"{agent_id}": self.agents[agent_id].run(task, return_code=return_code) for agent_id in self.agents  # noqa: E501
    # }

    # https://huggingface.co/docs/transformers/v4.36.1/en/main_classes/agent#transformers.Agent.run
    # response = self.agent.run(
    #     task=text,
    #     return_code=return_code,
    #     # remote=False,
    #     # **kwargs,
    #     pad_token_id=self.tokenizer.eos_token_id,
    # )

    # print('chat; response:', response)

    # return {
    #     "message": response,
    # }

    # return {
    #     "message": self.generate(text),
    # }

    # async def __call__(self, http_request: Request) -> str:
    #     json_request: str = await http_request.json()
    #     prompts = []
    #     for prompt in json_request:
    #         text = prompt["text"]
    #         if isinstance(text, list):
    #             prompts.extend(text)
    #         else:
    #             prompts.append(text)
    #     return self.generate(prompts)


deployment = FastAPIDeployment.bind()

# 2: Deploy the deployment.
# serve.run(FastAPIDeployment.bind(), route_prefix="/")
# serve.run(deployment, route_prefix="/")

# 3: Query the deployment and print the result.
# print(requests.get("http://localhost:8000/hello", params={"name": "Theodore"}).json())
# "Hello Theodore!"

# print('serve.py')

# if __name__ == '__main__':
#     print('serve.py main')
