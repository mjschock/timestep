
# Temporary in-memory dictionary db with instances and without locking
# TODO: move to SQLite tables, add vector capabilities, etc.

# db = {
#     "assistants": {},
#     "messages": {},
#     "runs": {},
#     "file_objects": {},
#     "fine_tuning_jobs": {},
#     "fine_tuning_job_events": {},
#     "models": {},
#     "threads": {},
# }

# print('db: ', db)

# async_connector = SqlAlchemyConnector(
#     connection_info=ConnectionComponents(
#         driver=AsyncDriver.SQLITE_AIOSQLITE,
#         database="assistants.db"
#     )
# )

# connector = SqlAlchemyConnector(
#     connection_info=ConnectionComponents(
#         driver=SyncDriver.SQLITE_PYSQLITE,
#         database="assistants.db"
#     )
# )


from llama_cpp import Llama
from llama_cpp.llama_chat_format import Llama3VisionAlpha, Llava15ChatHandler, Llava16ChatHandler, MoondreamChatHandler, NanoLlavaChatHandler, ObsidianChatHandler
from llama_cpp.llama_speculative import LlamaPromptLookupDecoding
from llama_cpp.llama_tokenizer import LlamaHFTokenizer


class InstanceStoreSingleton(object):
  _shared_instance_state = {
      "assistants": {},
      "messages": {},
      "runs": {},
      "file_objects": {},
      "fine_tuning_jobs": {},
      "fine_tuning_job_events": {},
      "models": {},
      "threads": {},
  }
   
  def __new__(cls, *args, **kwargs):
    obj = super(InstanceStoreSingleton, cls).__new__(cls, *args, **kwargs)
    obj.__dict__ = cls._shared_instance_state

    return obj
   
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
# model_alias = "Polaris-Small" # https://ollama.com/starfleetai/polaris-small
# model_alias = "Phi-3-Mini-4K-Instruct"
# model_alias = "Replit-Code-V-1.5-3B"
# model_alias = "SmolLM-?" # https://huggingface.co/collections/HuggingFaceTB/smollm-6695016cad7167254ce15966
# model_alias = "TinyLlama-1.1B"
model_alias = "TinySolar-248m-4k-py"
# n_ctx = 2048
n_ctx = 4096
# n_ctx = 16192
n_gpu_layers = -1
num_pred_tokens = 2 if n_gpu_layers == 0 else 10 # num_pred_tokens is the number of tokens to predict 10 is the default and generally good for gpu, 2 performs better for cpu-only machines.
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
