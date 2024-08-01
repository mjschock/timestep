import time
import uuid

import typer
from langchain_community.llms.llamafile import Llamafile
from llama_cpp import Llama
from llama_cpp.llama_chat_format import (
    Llama3VisionAlpha,
    Llava15ChatHandler,
    Llava16ChatHandler,
    MoondreamChatHandler,
    NanoLlavaChatHandler,
)
from llama_cpp.llama_tokenizer import LlamaHFTokenizer
from openai.types.model import Model
from sqlmodel import Field, SQLModel
from stable_diffusion_cpp import StableDiffusion

app_dir = typer.get_app_dir("timestep")
# from timestep.database import InstanceStoreSingleton


async def get_default_agent():
    return None


# class AgentService(object):
#     # models: dict[uuid.UUID] = {}
#     _shared_instance_state = {
#         "models": {},
#     }

#     def __new__(cls, *args, **kwargs):
#         obj = super(AgentService, cls).__new__(cls, *args, **kwargs)
#         obj.__dict__ = cls._shared_instance_state

#         return obj


class ModelSQLModel(Model, SQLModel, table=True):
    __tablename__: str = "models"
    # object: str = "model"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    # id: uuid.uuid4 = Field(default_factory=uuid.uuid4, primary_key=True)

    # group_id: uuid.UUID = Field(foreign_key=groups.id)
    object: str = "model"
    # organization_id: uuid.UUID = Field(foreign_key=organizations.id)


class ModelInstanceStoreSingleton(object):
    _shared_model_instances: dict[str] = {}

    def __new__(cls, *args, **kwargs):
        obj = super(ModelInstanceStoreSingleton, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_model_instances

        return obj

    def create_model(self, model_aliases=[], model_name=None):
        # chat_format = None
        chat_format = "chatml-function-calling"
        chat_handler = None
        echo = True
        embedding = False
        filename = None
        mmproj_model_filename = "*mmproj*"
        mmproj_model_repo_id = None
        model_instance = None
        # n_ctx = 2048
        n_ctx = 4096
        # n_ctx = 8192
        # n_ctx = 16192
        n_gpu_layers = -1
        num_pred_tokens = (
            2 if n_gpu_layers == 0 else 10
        )  # num_pred_tokens is the number of tokens to predict 10 is the default and generally good for gpu, 2 performs better for cpu-only machines.
        text_model_filename = "*text-model*"
        text_model_repo_id = None
        tokenizer = None
        verbose = True

        if model_name == "BakLLaVA-1":
            mmproj_model_filename = "mmproj-model-f16.gguf"
            mmproj_model_repo_id = "mys/ggml_bakllava-1"
            text_model_filename = "ggml-model-q4_k.gguf"
            text_model_repo_id = mmproj_model_repo_id

            chat_handler = Llava15ChatHandler.from_pretrained(
                repo_id=mmproj_model_repo_id,
                filename=mmproj_model_filename,
            )

        elif model_name == "Functionary-V2.5":
            chat_format = chat_format if chat_format else "functionary-v2"
            text_model_repo_id = "meetkai/functionary-small-v2.5-GGUF"
            text_model_filename = "functionary-small-v2.5.Q4_0.gguf"
            tokenizer = LlamaHFTokenizer.from_pretrained(text_model_repo_id)

        elif model_name == "Llama-3-Vision-Alpha":
            mmproj_model_repo_id = "abetlen/llama-3-vision-alpha-gguf"
            text_model_filename = "Meta-Llama-3-8B.Q4_K_M.gguf"
            text_model_repo_id = "QuantFactory/Meta-Llama-3-8B-GGUF"

            if chat_format is None:
                chat_handler = Llama3VisionAlpha.from_pretrained(
                    repo_id=mmproj_model_repo_id,
                    filename=mmproj_model_filename,
                )

        elif model_name == "llamafile":
            model_instance = Llamafile()

        elif model_name == "LLaVA-NeXT-Vicuna-7B":
            mmproj_model_filename = "mmproj-vicuna7b-f16-q6_k.gguf"
            mmproj_model_repo_id = "cmp-nct/llava-1.6-gguf"
            text_model_filename = "vicuna-7b-q5_k.gguf"
            text_model_repo_id = mmproj_model_repo_id

            if chat_format is None:
                chat_handler = Llava16ChatHandler.from_pretrained(
                    repo_id=mmproj_model_repo_id,
                    filename=mmproj_model_filename,
                )

        elif model_name == "LLaVA-Phi-3-Mini":
            mmproj_model_filename = "llava-phi-3-mini-int4.gguf"
            mmproj_model_repo_id = "xtuner/llava-phi-3-mini-gguf"
            text_model_filename = "llava-phi-3-mini-mmproj-f16.gguf"
            text_model_repo_id = mmproj_model_repo_id

        elif model_name == "MobileVLM-1.7B":
            mmproj_model_filename = "MobileVLM-1.7B-mmproj-f16.gguf"
            mmproj_model_repo_id = "guinmoon/MobileVLM-1.7B-GGUF"
            text_model_filename = "MobileVLM-1.7B-Q4_K.gguf"
            text_model_repo_id = mmproj_model_repo_id

        elif model_name == "MobileVLM_V2-1.7B":
            mmproj_model_filename = "mmproj-model-f16.gguf"
            mmproj_model_repo_id = "ZiangWu/MobileVLM_V2-1.7B-GGUF"
            text_model_filename = "ggml-model-q4_k.gguf"
            text_model_repo_id = mmproj_model_repo_id

        elif model_name == "moondream2":
            mmproj_model_repo_id = "vikhyatk/moondream2"
            text_model_repo_id = mmproj_model_repo_id

            if chat_format is None:
                chat_handler = MoondreamChatHandler.from_pretrained(
                    repo_id=mmproj_model_repo_id,
                    filename=mmproj_model_filename,
                )

        elif model_name == "nanoLLaVA":
            mmproj_model_repo_id = "abetlen/nanollava-gguf"
            text_model_repo_id = mmproj_model_repo_id

            if chat_format is None:
                chat_handler = NanoLlavaChatHandler.from_pretrained(
                    repo_id=mmproj_model_repo_id,
                    filename=mmproj_model_filename,
                )

        elif model_name == "OpenLLaMA-3Bv2":
            text_model_filename = "open_llama_3b_v2-q8_0.gguf"
            text_model_repo_id = "mjschock/open_llama_3b_v2-Q8_0-GGUF"

        elif model_name == "Phi-3-Mini-4K-Instruct":
            text_model_filename = "Phi-3-mini-4k-instruct-q4.gguf"
            text_model_repo_id = "microsoft/Phi-3-mini-4k-instruct-gguf"
            tokenizer = LlamaHFTokenizer.from_pretrained(
                "microsoft/Phi-3-mini-4k-instruct"
            )

        elif model_name == "Replit-Code-V-1.5-3B":
            n_ctx = 16192
            text_model_filename = "replit-code-v1_5-3b.Q4_0.gguf"
            text_model_repo_id = "abetlen/replit-code-v1_5-3b-GGUF"

        elif model_name == "SmolLM-135M":
            text_model_filename = "SmolLM-135M-F16.gguf"
            text_model_repo_id = "stillerman/SmolLM-135M-Llamafile"

        elif model_name == "Stable-Diffusion-v1-5":
            model_instance = StableDiffusion(
                model_path=f"{app_dir}/models/runwayml/stable-diffusion-v1-5/v1-5-pruned-emaonly.safetensors",
                wtype="default",  # Weight type (options: default, f32, f16, q4_0, q4_1, q5_0, q5_1, q8_0)
                # seed=1337, # Uncomment to set a specific seed
            )

        elif model_name == "TinyLlama-1.1B":
            text_model_filename = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
            text_model_repo_id = "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF"

        elif model_name == "TinySolar-248m-4k-py":
            text_model_filename = "tinysolar-248m-4k-py-q4_k_m.gguf"
            text_model_repo_id = "mjschock/TinySolar-248m-4k-py-Q4_K_M-GGUF"

        else:
            raise NotImplementedError(model_name)

        model_id = str(uuid.uuid4)  # TODO: insert model in db and get id

        # model = Llama( # TODO: switch to LangChain LL?
        model_instance = model_instance or Llama.from_pretrained(
            chat_format=chat_format,
            chat_handler=chat_handler,
            echo=echo,
            # draft_model=LlamaPromptLookupDecoding(num_pred_tokens=num_pred_tokens),
            embedding=embedding,
            filename=text_model_filename,
            model_alias=model_id,
            n_ctx=n_ctx,
            n_gpu_layers=n_gpu_layers,
            repo_id=text_model_repo_id,
            tokenizer=tokenizer,
            verbose=verbose,
        )

        for model_id in [model_id] + model_aliases + [model_name]:
            self._shared_model_instances[model_id] = model_instance

    def delete_model(self, model):  # noqa: E501
        """Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

        # noqa: E501

        :param model: The model to delete
        :type model: str

        :rtype: Union[DeleteModelResponse, Tuple[DeleteModelResponse, int], Tuple[DeleteModelResponse, int, Dict[str, str]]
        """
        raise NotImplementedError

    def list_models(self):  # noqa: E501
        """Lists the currently available models, and provides basic information about each one such as the owner and availability.

        # noqa: E501


        :rtype: Union[ListModelsResponse, Tuple[ListModelsResponse, int], Tuple[ListModelsResponse, int, Dict[str, str]]
        """
        raise NotImplementedError

    def retrieve_model(self, model_id: str):
        """Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

        # noqa: E501

        :param model: The ID of the model to use for this request
        :type model: str

        :rtype: Union[Model, Tuple[Model, int], Tuple[Model, int, Dict[str, str]]
        """

        model: Llama = model_instance_store._shared_instance_state["models"][model_id]

        return {
            "chat_format": model.chat_format,
            "model_path": model.model_path,
            "n_ctx": model.n_ctx(),
            "lora_base": model.lora_base,
            "lora_path": model.lora_path,
            "lora_scale": model.lora_scale,
        }


model_instance_store = ModelInstanceStoreSingleton()
model_instance_store.created_at = time.time()

model_instance_store.create_model(
    model_aliases=[
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-1106",
        "gpt-4-1106-preview",
        "gpt-4-turbo",
        "gpt-4o",
        "gpt-4o-mini",
        "LLaMA_CPP",
    ],
    # model_name="SmolLM-135M",
    # model_name="TinySolar-248m-4k-py",
    model_name="llamafile",
)

# model_instance_store.create_model(
#     model_aliases=[
#         "dall-e-2",
#         "dall-e-3",
#     ],
#     model_name="Stable-Diffusion-v1-5",
# )

# model_instance_store.create_model(
#     model_aliases=[
#         "text-embedding-3-small",
#         "text-embedding-3-large",
#         "text-embedding-ada-002",
#     ],
# )

# model_instance_store.create_model(
#     model_aliases=[
#         "tts-1",
#         "tts-1-hd",
#     ],
# )

# model_instance_store.create_model(
#     model_aliases=[
#         "whisper-1",
#     ],
# )
