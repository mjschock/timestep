import os

from llama_cpp import Llama
from llama_cpp.llama_chat_format import MoondreamChatHandler, NanoLlavaChatHandler, ObsidianChatHandler
from llama_cpp.llama_tokenizer import LlamaHFTokenizer

# chat_handler = MoondreamChatHandler.from_pretrained(
#   repo_id="vikhyatk/moondream2",
#   filename="*mmproj*",
# )

# llm = Llama.from_pretrained(
#   repo_id="vikhyatk/moondream2",
#   filename="*text-model*",
#   chat_handler=chat_handler,
#   n_ctx=2048, # n_ctx should be increased to accommodate the image embedding
# )

# chat_handler = NanoLlavaChatHandler.from_pretrained(
#   repo_id="abetlen/nanollava-gguf",
#   filename="*mmproj*",
# )

# llm = Llama.from_pretrained(
#   repo_id="abetlen/nanollava-gguf",
#   filename="*text-model*",
#   chat_handler=chat_handler,
#   n_ctx=2048, # n_ctx should be increased to accommodate the image embedding
# )

# llm = Llama(
#     chat_format="oasst_llama",
#     model_path=f"{os.getcwd()}/3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf",
#     n_ctx=16192,
# )

# llm = Llama.from_pretrained(
#   repo_id="abetlen/replit-code-v1_5-3b-GGUF",
#   filename="replit-code-v1_5-3b.Q4_0.gguf",
#   n_ctx=16192,
# )

# tokenizer = LlamaHFTokenizer.from_pretrained("meetkai/functionary-small-v2.5-GGUF")

# llm = Llama.from_pretrained(
#   repo_id="meetkai/functionary-small-v2.5-GGUF",
#   filename="functionary-small-v2.5.Q4_0.gguf",
#   chat_format="functionary-v2",
#   tokenizer=tokenizer,
# )

# llm = Llama(
#     chat_format="functionary-v2",
#     # lora_path=f"{os.getcwd()}/notebooks/lora-TinyLLama-v0.1-5M-F16-Recipe_NER-LATEST.bin",
#     model_path=f"{os.getcwd()}/3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf",
#     n_ctx=16192,
#     tokenizer=tokenizer,
# )

# llm = Llama.from_pretrained(
#   repo_id="gorilla-llm/gorilla-openfunctions-v2-gguf",
#   filename="gorilla-openfunctions-v2-q2_K.gguf",
#   n_ctx=2048, # n_ctx should be increased to accommodate the image embedding
# )

# llm = Llama(
#     # chat_format="functionary-v2",
#     # lora_path=f"{os.getcwd()}/notebooks/lora-TinyLLama-v0.1-5M-F16-Recipe_NER-LATEST.bin",
#     model_path=f"{os.getcwd()}/3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf",
#     n_ctx=16192,
#     # tokenizer=tokenizer,
# )

# chat_handler = ObsidianChatHandler.from_pretrained(
#   repo_id="NousResearch/Obsidian-3B-V0.5-GGUF",
#   filename="mmproj-obsidian-f16.gguf",
# )

# llm = Llama.from_pretrained(
#   repo_id="NousResearch/Obsidian-3B-V0.5-GGUF",
#   filename="obsidian-q6.gguf",
#   chat_handler=chat_handler,
#   n_ctx=2048, # n_ctx should be increased to accommodate the image embedding
# )

llm = Llama(
    chat_format="chatml",
    model_path=f"{os.getcwd()}/3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf",
    n_ctx=16192,
)

# TODO:
# https://github.com/microsoft/Samba
# https://github.com/facebookresearch/MobileLLM
