import enum
import uuid
from typing import List, Optional

import typer
from llama_cpp import Llama
from llama_cpp.llama_chat_format import (
    Llama3VisionAlpha,
    Llava15ChatHandler,
    Llava16ChatHandler,
    MoondreamChatHandler,
    NanoLlavaChatHandler,
    ObsidianChatHandler,
)
from llama_cpp.llama_speculative import LlamaPromptLookupDecoding
from llama_cpp.llama_tokenizer import LlamaHFTokenizer
from openai.types.fine_tuning.fine_tuning_job import (
    Error,
    FineTuningJob,
    Hyperparameters,
)
from openai.types.fine_tuning.fine_tuning_job_event import FineTuningJobEvent
from pydantic import BaseModel

# from sqlalchemy import JSON
# import sqlalchemy
from sqlalchemy import Column, Enum

# from sqlalchemy.dialects.sqlite.json import JSON
from sqlalchemy.types import JSON
from sqlmodel import Field, Session, SQLModel, create_engine, select

# class FineTuningJobErrorSQLModel(Error, Column(JSON)):
#   pass
#   __tablename__: str = "fine_tuning_job_errors"

#   id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class FineTuningJobStatus(str, enum.Enum):
    cancelled = "cancelled"
    failed = "failed"
    queued = "queued"
    running = "running"
    succeeded = "succeeded"
    validating_files = "validating_files"


class FineTuningJobSQLModel(FineTuningJob, SQLModel, table=True):
    __tablename__: str = "fine_tuning_jobs"
    object: str = "fine_tuning.job"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    # id: uuid.uuid4 = Field(default_factory=uuid.uuid4, primary_key=True)

    error: Optional[dict] = Field(sa_column=Column(JSON), default=JSON.NULL)
    integrations: Optional[List[dict]] = Field(
        sa_column=Column(JSON), default=JSON.NULL
    )
    hyperparameters: dict = Field(sa_column=Column(JSON), default={})
    result_files: List[str] = Field(sa_column=Column(JSON), default=[])
    status: FineTuningJobStatus = Field(
        sa_column=Column(Enum(FineTuningJobStatus)), default=FineTuningJobStatus.queued
    )


app_dir = typer.get_app_dir(__package__)
engine = create_engine(f"sqlite:///{app_dir}/database.db")

SQLModel.metadata.create_all(engine)


class InstanceStoreSingleton(object):
    _shared_instance_state = {
        "assistants": {},
        "messages": {},
        "runs": {},
        "file_objects": {},
        # "fine_tuning_jobs": {},
        "fine_tuning_job_events": {},
        "models": {},
        "threads": {},
    }

    def __new__(cls, *args, **kwargs):
        obj = super(InstanceStoreSingleton, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_instance_state

        return obj

    def insert(self, base_model: BaseModel):
        if type(base_model) is FineTuningJob:
            print("=== insert ===")
            print("id: ", base_model.id)
            print('base_model.model_dump()["id"]', base_model.model_dump()["id"])
            fine_tuning_job = FineTuningJobSQLModel.model_validate(
                base_model.model_dump()
            )
            print("fine_tuning_job.id: ", fine_tuning_job.id)

            with Session(engine) as session:
                session.add(fine_tuning_job)
                session.commit()

        else:
            raise NotImplementedError(f"Type {type(base_model)} is not yet implemented")

    def select(self, base_model_class, id: str):
        print("=== select ===")
        print("id: ", id)

        if issubclass(base_model_class, FineTuningJob):
            with Session(engine) as session:
                fine_tuning_job = session.get(
                    FineTuningJobSQLModel, ident=uuid.UUID(id, version=4)
                )
                print("fine_tuning_job.id: ", fine_tuning_job.id)

                assert (
                    type(fine_tuning_job.id) == uuid.UUID
                ), f"{type(fine_tuning_job.id)} != uuid.UUID"

                # m = base_model_class.model_validate(fine_tuning_job, strict=True)
                # print('type(m): ', type(m))
                #

                return FineTuningJob(**fine_tuning_job.model_dump(mode="json"))

                # raise NotImplementedError

        else:
            raise NotImplementedError(f"Type {base_model_class} is not yet implemented")


instance_store = InstanceStoreSingleton()
instance_store.shared_variable = "Shared Variable"

# chat_format = None
chat_format = "chatml-function-calling"
chat_handler = None
echo = True
embedding = False
filename = None
mmproj_model_filename = "*mmproj*"
mmproj_model_repo_id = None
# model_alias = "BakLLaVA-1"
# model_alias = "Functionary-V2.5"
# model_alias = "Llama-3-Vision-Alpha"
# model_alias = "LLaVA-NeXT-Vicuna-7B"
# model_alias = "LLaVA-Phi-3-Mini"
# model_alias = "Mamba-?"
# model_alias = "MobileVLM-1.7B"
# model_alias = "MobileVLM_V2-1.7B"
# model_alias = "moondream2"
# model_alias = "nanoLLaVA"
model_alias = "OpenLLaMA-3Bv2"
# model_alias = "Polaris-Small" # https://ollama.com/starfleetai/polaris-small
# model_alias = "Phi-3-Mini-4K-Instruct"
# model_alias = "Replit-Code-V-1.5-3B"
# model_alias = "SmolLM-?" # https://huggingface.co/collections/HuggingFaceTB/smollm-6695016cad7167254ce15966
# model_alias = "TinyLlama-1.1B"
# model_alias = "TinySolar-248m-4k-py"
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

if model_alias == "BakLLaVA-1":
    mmproj_model_filename = "mmproj-model-f16.gguf"
    mmproj_model_repo_id = "mys/ggml_bakllava-1"
    text_model_filename = "ggml-model-q4_k.gguf"
    text_model_repo_id = mmproj_model_repo_id

    chat_handler = Llava15ChatHandler.from_pretrained(
        repo_id=mmproj_model_repo_id,
        filename=mmproj_model_filename,
    )

elif model_alias == "Functionary-V2.5":
    chat_format = chat_format if chat_format else "functionary-v2"
    text_model_repo_id = "meetkai/functionary-small-v2.5-GGUF"
    text_model_filename = "functionary-small-v2.5.Q4_0.gguf"
    tokenizer = LlamaHFTokenizer.from_pretrained(text_model_repo_id)

elif model_alias == "Llama-3-Vision-Alpha":
    mmproj_model_repo_id = "abetlen/llama-3-vision-alpha-gguf"
    text_model_filename = "Meta-Llama-3-8B.Q4_K_M.gguf"
    text_model_repo_id = "QuantFactory/Meta-Llama-3-8B-GGUF"

    if chat_format is None:
        chat_handler = Llama3VisionAlpha.from_pretrained(
            repo_id=mmproj_model_repo_id,
            filename=mmproj_model_filename,
        )

elif model_alias == "LLaVA-NeXT-Vicuna-7B":
    mmproj_model_filename = "mmproj-vicuna7b-f16-q6_k.gguf"
    mmproj_model_repo_id = "cmp-nct/llava-1.6-gguf"
    text_model_filename = "vicuna-7b-q5_k.gguf"
    text_model_repo_id = mmproj_model_repo_id

    if chat_format is None:
        chat_handler = Llava16ChatHandler.from_pretrained(
            repo_id=mmproj_model_repo_id,
            filename=mmproj_model_filename,
        )

elif model_alias == "LLaVA-Phi-3-Mini":
    mmproj_model_filename = " llava-phi-3-mini-int4.gguf"
    mmproj_model_repo_id = "xtuner/llava-phi-3-mini-gguf"
    text_model_filename = "llava-phi-3-mini-mmproj-f16.gguf"
    text_model_repo_id = mmproj_model_repo_id

elif model_alias == "MobileVLM-1.7B":
    mmproj_model_filename = "MobileVLM-1.7B-mmproj-f16.gguf"
    mmproj_model_repo_id = "guinmoon/MobileVLM-1.7B-GGUF"
    text_model_filename = "MobileVLM-1.7B-Q4_K.gguf"
    text_model_repo_id = mmproj_model_repo_id

elif model_alias == "MobileVLM_V2-1.7B":
    mmproj_model_filename = "mmproj-model-f16.gguf"
    mmproj_model_repo_id = "ZiangWu/MobileVLM_V2-1.7B-GGUF"
    text_model_filename = "ggml-model-q4_k.gguf"
    text_model_repo_id = mmproj_model_repo_id

elif model_alias == "moondream2":
    mmproj_model_repo_id = "vikhyatk/moondream2"
    text_model_repo_id = mmproj_model_repo_id

    if chat_format is None:
        chat_handler = MoondreamChatHandler.from_pretrained(
            repo_id=mmproj_model_repo_id,
            filename=mmproj_model_filename,
        )

elif model_alias == "nanoLLaVA":
    mmproj_model_repo_id = "abetlen/nanollava-gguf"
    text_model_repo_id = mmproj_model_repo_id

    if chat_format is None:
        chat_handler = NanoLlavaChatHandler.from_pretrained(
            repo_id=mmproj_model_repo_id,
            filename=mmproj_model_filename,
        )

elif model_alias == "OpenLLaMA-3Bv2":
    text_model_filename = "open_llama_3b_v2-q8_0.gguf"
    text_model_repo_id = "mjschock/open_llama_3b_v2-Q8_0-GGUF"

elif model_alias == "Phi-3-Mini-4K-Instruct":
    text_model_filename = "Phi-3-mini-4k-instruct-q4.gguf"
    text_model_repo_id = "microsoft/Phi-3-mini-4k-instruct-gguf"
    tokenizer = LlamaHFTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

elif model_alias == "Replit-Code-V-1.5-3B":
    n_ctx = 16192
    text_model_filename = "replit-code-v1_5-3b.Q4_0.gguf"
    text_model_repo_id = "abetlen/replit-code-v1_5-3b-GGUF"

elif model_alias == "TinyLlama-1.1B":
    text_model_filename = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
    text_model_repo_id = "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF"

elif model_alias == "TinySolar-248m-4k-py":
    text_model_filename = "tinysolar-248m-4k-py-q4_k_m.gguf"
    text_model_repo_id = "mjschock/TinySolar-248m-4k-py-Q4_K_M-GGUF"

else:
    raise NotImplementedError(model_alias)

# model = Llama( # TODO: switch to LangChain LL?
model = Llama.from_pretrained(
    chat_format=chat_format,
    chat_handler=chat_handler,
    echo=echo,
    # draft_model=LlamaPromptLookupDecoding(num_pred_tokens=num_pred_tokens),
    embedding=embedding,
    filename=text_model_filename,
    model_alias=model_alias,
    n_ctx=n_ctx,
    n_gpu_layers=n_gpu_layers,
    repo_id=text_model_repo_id,
    tokenizer=tokenizer,
    verbose=verbose,
)

instance_store._shared_instance_state["models"]["gpt-3.5-turbo"] = model
instance_store._shared_instance_state["models"]["gpt-3.5-turbo-0613"] = model
instance_store._shared_instance_state["models"]["gpt-3.5-turbo-1106"] = model
instance_store._shared_instance_state["models"]["gpt-4-1106-preview"] = model
instance_store._shared_instance_state["models"]["gpt-4o"] = model
instance_store._shared_instance_state["models"]["gpt-4-vision-preview"] = model
instance_store._shared_instance_state["models"]["LLaMA_CPP"] = model
instance_store._shared_instance_state["models"][model_alias] = model
