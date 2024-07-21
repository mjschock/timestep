# import joblib
import os

from huggingface_hub import hf_hub_download
from llama_cpp import Llama
# from llama_cpp.llama_chat_format import MoondreamChatHandler, NanoLlavaChatHandler, ObsidianChatHandler
# from llama_cpp.llama_tokenizer import LlamaHFTokenizer
from langchain_core.language_models.llms import LLM
from langchain_community.llms.llamafile import Llamafile
from prefect import flow
from prefect_shell import ShellOperation

from timestep.database import borg
from timestep.utils import start_shell_script

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

# def serve_llamafile()

@flow
def serve_model(
    # filename="tinyllama-1.1b-chat-v1.0-q4_k_m.gguf",
    filename="TinyLLama-v0.1-5M-F16.gguf",
    local_dir="models",
    local_dir_use_symlinks=False,
    # repo_id="mjschock/TinyLlama-1.1B-Chat-v1.0-Q4_K_M-GGUF",
    repo_id=None,
):
    if repo_id:
        # model = joblib.load(
        hf_hub_download(
            filename=filename,
            local_dir=local_dir,
            local_dir_use_symlinks=local_dir_use_symlinks,
            repo_id=repo_id,
        )
        # )

    # TODO:
    # 1. Switch to LangChain's LLamaCpp and update API's to use LangChain's llm interface
    #    See: https://python.langchain.com/v0.2/docs/integrations/llms/llamacpp/
    # 2. Then add logic to create llamafile from GGUF and then swap LlamaCpp for LangChain's LLamafile
    #    See: https://justine.lol/matmul/
    #    See: https://python.langchain.com/v0.2/docs/integrations/llms/llamafile/
    model = Llama( # TODO: switch to LangChain LL
        chat_format="chatml",
        # model_path=f"{os.getcwd()}/3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf",
        model_path=f"{local_dir}/{filename}",
        n_ctx=16192,
    )

# llamafile -m TinyLlama-1.1B-Chat-v1.0.f16.gguf \
#           --grammar 'root ::= "yes" | "no"' --temp 0 -c 0 \
#           --no-display-prompt --log-disable -p "<|user|>
# Can you say for certain that the following email is spam?

# To: jtunney@gmail.com
# From: Federal-Tax-DebtHelp <ConfirmationEmail.inzk@janents.com>
# Subject: Reduce your payments to what you can afford

# Reduce your payments to what you can afford 
 
#  [IMG] 
#  [IMG] 
 
#  [IMG] 
# </s>
# <|assistant|>"

    # with ShellOperation(
    #     commands=[
    #         # "curl -O https://masie_web.apps.nsidc.org/pub/DATASETS/NOAA/G02135/north/daily/data/N_seaice_extent_daily_v3.0.csv",
    #         # f"""{os.getcwd()}/3rdparty/llama-cpp-python/vendor/llama.cpp/llama-finetune \
    #         # TODO: move llama-finetune to vendored dep and use Python CPP bindings to run llama-cpp
    #         f"""llamafile -m {local_dir}/{filename}"""
    #     ],
    #     # working_dir=working_dir,
    # ) as download_csv_operation:

    #     # trigger runs the process in the background
    #     download_csv_process = download_csv_operation.trigger()

    #     # then do other things here in the meantime, like download another file
    #     ...

    #     # when you're ready, wait for the process to finish
    #     download_csv_process.wait_for_completion()

    #     # if you'd like to get the output lines, you can use the `fetch_result` method
    #     output_lines = download_csv_process.fetch_result()

    #     print('output_lines: ', output_lines)

    # if os.path.basename(llamafile_path) == default_llamafile_filename and not os.path.exists(llamafile_path):
    #     os.makedirs(os.path.dirname(llamafile_path))
    #     download_with_progress_bar(default_llamafile_url, llamafile_path)

    # assert os.path.exists(llamafile_path)

    # process = start_shell_script(
    #     file_path="models/TinyLlama-1.1B-Chat-v1.0.F16.llamafile"
    #     # '--host', host,
    #     "--nobrowser",
    #     # '--path', public_path,
    #     # '--port', f'{port}',
    # )
    # print(f"... loaded model with PID: {process.pid}.")

    # raise Exception

    # model: LLM = Llamafile(base_url="http://localhost:8080")

    borg._shared_borg_state["models"]["gpt-3.5-turbo"] = model
    borg._shared_borg_state["models"]["gpt-4-1106-preview"] = model
    borg._shared_borg_state["models"]["LLaMA_CPP"] = model

    print('borg._shared_borg_state: ', borg._shared_borg_state)

    # TODO:
    # https://github.com/microsoft/Samba
    # https://github.com/facebookresearch/MobileLLM
    # https://github.com/TinyLLaVA/TinyLLaVA_Factory

    return model

if __name__ == "__main__":
    serve_model()
