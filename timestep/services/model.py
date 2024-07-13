import os

from llama_cpp import Llama
from llama_cpp.llama_chat_format import MoondreamChatHandler, NanoLlavaChatHandler

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

llm = Llama(
    chat_format="oasst_llama",
    model_path=f"{os.getcwd()}/3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf",
    n_ctx=16192,
)

# llm = Llama.from_pretrained(
#   repo_id="abetlen/replit-code-v1_5-3b-GGUF",
#   filename="replit-code-v1_5-3b.Q4_0.gguf",
#   n_ctx=16192,
# )
