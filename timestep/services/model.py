from llama_cpp import Llama
from llama_cpp.llama_chat_format import MoondreamChatHandler

chat_handler = MoondreamChatHandler.from_pretrained(
  repo_id="vikhyatk/moondream2",
  filename="*mmproj*",
)

llm = Llama.from_pretrained(
  repo_id="vikhyatk/moondream2",
  filename="*text-model*",
  chat_handler=chat_handler,
  n_ctx=2048, # n_ctx should be increased to accommodate the image embedding
)
