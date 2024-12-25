import argparse
import os
from pprint import pprint

import mlflow
import torch
from datasets import load_dataset
from mlflow import MlflowClient
from trl import SFTConfig, SFTTrainer
from unsloth import FastVisionModel, is_bfloat16_supported
from unsloth.trainer import UnslothVisionDataCollator

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")

print(f"MLFLOW_TRACKING_URI: {MLFLOW_TRACKING_URI}")

# PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
# mlflow.transformers.autolog()
mlflow.autolog(
    disable=False,
    disable_for_unsupported_versions=False,
    exclude_flavors=None,
    exclusive=False,
    extra_tags=None,
    # log_dataset=True,
    log_input_examples=True,
    log_model_signatures=True,
    log_models=True,
    # log_trace=True,
    silent=False,
)


def print_auto_logged_info(r):
    tags = {k: v for k, v in r.data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in MlflowClient().list_artifacts(r.info.run_id, "model")]
    print(f"run_id: {r.info.run_id}")
    print(f"artifacts: {artifacts}")
    print(f"params: {r.data.params}")
    print(f"metrics: {r.data.metrics}")
    print(f"tags: {tags}")


dtype = (
    None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
)
load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.
max_seq_length = 2048  # Supports RoPE Scaling interally, so choose any!
# max_seq_length = 4096 # Choose any! We auto support RoPE Scaling internally!

# [1] Get LAION dataset
# url = "https://huggingface.co/datasets/laion/OIG/resolve/main/unified_chip2.jsonl"
# dataset = load_dataset("json", data_files={"train": url}, split="train")
# dataset = load_dataset("json", data_files={"train": url}, split="train[:1%]")
# dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2024-10", split="train", streaming=True)
# dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2024-46", split="train[:1%]")
# dataset = DataChain.from_hf("HuggingFaceFW/fineweb", name="CC-MAIN-2024-46", split="train")
# dataset = load_dataset("unsloth/Radiology_mini", split = "train[:1%]")
# dataset = load_dataset("unsloth/llava-instruct-mix-vsft-mini", split = "train[:1%]")
# dataset = load_dataset("unsloth/LaTeX_OCR", split = "train")
dataset = load_dataset("unsloth/LaTeX_OCR", split="train[:1%]")
# lmms-lab/LLaVA-OneVision-Data


def convert_to_conversation(sample, instruction, image_key="image", text_key="text"):
    conversation = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": instruction},
                {"type": "image", "image": sample[image_key]},
            ],
        },
        {"role": "assistant", "content": [{"type": "text", "text": sample[text_key]}]},
    ]

    return {"messages": conversation}


dataset = [
    convert_to_conversation(sample, "Write the LaTeX representation for this image.")
    for sample in dataset
]

# 4bit pre quantized models we support for 4x faster downloading + no OOMs.
# fourbit_models = [
# "unsloth/tinyllama-bnb-4bit",  # "unsloth/tinyllama" for 16bit loading
# ]  # More models at https://huggingface.co/unsloth

# [2] Load Mistral model
# model, tokenizer = FastLanguageModel.from_pretrained(
#     dtype=dtype,
#     load_in_4bit=load_in_4bit,
#     max_seq_length=max_seq_length,
#     # model_name=fourbit_models[0],
#     model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     # model_name="ibm-fms/Bamba-9B",
#     # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
# )

model, processor = FastVisionModel.from_pretrained(
    # "unsloth/Llama-3.2-11B-Vision-Instruct",
    # "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # "llava-hf/llava-onevision-qwen2-0.5b-ov-hf",
    # "HuggingFaceTB/SmolVLM-Instruct",
    # "Qwen/Qwen2-VL-2B-Instruct",
    "HuggingFaceTB/SmolVLM-Instruct",
    load_in_4bit=True,  # Use 4bit to reduce memory use. False for 16bit LoRA.
    max_seq_length=2048,  # Supports RoPE Scaling internally, so choose any!
    use_gradient_checkpointing="unsloth",  # True or "unsloth" for long context
)

# print("model:")
# print(model)


def print_nparams(model):
    """Calculate the total number of model parameters"""
    nparams = sum(p.numel() for p in model.parameters())
    print(f"Number of parameters: {nparams}")


print_nparams(model)

DEFAULT_SYSTEM_MESSAGE = {
    "content": "You are an AI agent acting as a human assistant.",
    "role": "system",
}

tools_template = """
{
  "tools": [
  {% for tool in tools %}
    {
      "function": {
        "description": "{{ tool.function.description }}",
        "name": "{{ tool.function.name }}",
        "parameters": {{ tool.function.parameters | tojson }}
      },
      "type": "{{ tool.type }}"
    }{% if not loop.last %},{% endif %}\n
  {% endfor %}
  ]
}

If you would like to suggest one or more tool calls, please respond in the following format:
{
  "finish_reason": "tool_calls",
  "tool_calls": [
    {
      "arguments": "{\\"parameter_name\\": \\"parameter_value\\"}",
      "id": "call_id",
      "name": "tool_name"
    }
  ]
}
"""

tool_calls_template = """
{
  "finish_reason": "tool_calls",
  "tool_calls": [
  {% for tool_call in message.tool_calls %}
    {
      "arguments": {{ tool_call.function.arguments | tojson }},
      "id": "{{ tool_call.id }}",
      "name": "{{ tool_call.function.name }}"
    }{% if not loop.last %},{% endif %}\n
  {% endfor %}
  ]
}
"""

tool_response_template = """
{
  "content": {{ message.content | tojson }},
  "name": "{{ message.name }}",
  "tool_call_id": "{{ message.tool_call_id }}"
}
"""

content_template = """{% if message['content'] is string %}{{message['content']}}{% else %}{% for line in message['content'] %}{% if line['type'] == 'text' %}{{line['text']}}{% elif line['type'] in ['image'] %}{{ '<image>' }}{% endif %}{% endfor %}{% endif %}"""

# if pretrained_model_name == "TinyLlama-1.1B-Chat-v1.0":
# start_header_id = "<|"
# end_header_id = "|>"
# start_header_id = "<|im_start|>"  # https://github.com/Mozilla-Ocho/llamafile/blob/a8fd4d28c3d2259c98af7035bcdda1a68af6f62c/llama.cpp/server/server.cpp#L492
start_header_id = ""
# end_header_id = ":" + "' '"
end_header_id = ":"

# else:
#   start_header_id = "<|start_header_id|>"
#   end_header_id = "<|end_header_id|>"

role_header_template = (
    # start_header_id + "{{ message.role }}" + end_header_id + "{{ '\n' }}"
    start_header_id
    + "{{ message.role | capitalize }}"
    + end_header_id
)
assistant_generation_role_header_template = (
    # start_header_id + "assistant" + end_header_id + "{{ '\n' }}"
    start_header_id
    + "Assistant"
    + end_header_id
)

# Influenced by:
# https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models
# https://docs.anthropic.com/en/docs/build-with-claude/tool-use
# https://github.com/abetlen/llama-cpp-python/blob/7c4aead82d349469bbbe7d8c0f4678825873c039/llama_cpp/llama_chat_format.py#L3387
# https://github.com/Mozilla-Ocho/llamafile/blob/66a84d8aea2990895fc4f64786406fea64e79197/llama.cpp/server/server.cpp#L480 (need <|im_start|> b/c Mozilla)
# https://github.com/openai/openai-python/blob/120d225b91a8453e15240a49fb1c6794d8119326/chatml.md
# https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html#prompt
# https://huggingface.co/blog/unified-tool-use
chat_template = (
    # Configuration and defaults
    "{%- set config = namespace(has_system_message=false, has_tools=false) -%}"
    "{%- set system_messages = messages | selectattr('role', 'equalto', 'system') | list -%}"
    "{%- set config.has_system_message = system_messages | length > 0 -%}"
    # "{%- set config.has_tools = tools is defined and tools | length > 0 -%}"
    "{%- set config.has_tools = tools is not none and tools | length > 0 -%}"
    # Ensure system message exists
    # "{%- if not config.has_system_message -%}"
    # f'{{%- set messages = [{{ "content": "{DEFAULT_SYSTEM_MESSAGE["content"]}", "role": "{DEFAULT_SYSTEM_MESSAGE["role"]}" }}] + messages -%}}'
    # "{%- endif -%}"
    # Process messages
    "{%- for message in messages -%}"
    # "<|{{ message.role }}|>{{ '\n' }}" # "<|start_header_id|>{{ message.role }}<|end_header_id|>{{ '\n' }}"
    # f"{start_header_id}{{ message.role }}{end_header_id}{{ '\n' }}"
    # start_header_id + "{{ message.role }}" + end_header_id + "{{ '\n' }}"
    # TODO: add bos_token if first message?
    "{% if loop.first %}{{ bos_token }}{% endif %}"
    # f"{role_header_template}" + "{{ ' ' }}"
    "{% if message.content is not string and message.content[0]['type'] in ['image'] %}"
    # "{% if message.content is list and message.content[0]['type'] in ['image', 'image_url'] %}"
    f"{role_header_template}"
    "{%- else -%}"
    f"{role_header_template}" + "{{ ' ' }}"
    "{%- endif -%}"
    # System message handling
    "{%- if message.role == 'system' -%}"
    "{{ message.content }}"
    "{%- if config.has_tools -%}"
    "{{ '\n\n' }}You are aware of the following tools in your environment:"
    f"{tools_template}"
    "{%- endif -%}"
    # "{{ eos_token }}{{ '\n' }}" # <|eot_id|>
    # "<|im_end|>{{ '\n' }}"
    "<end_of_utterance>{{ '\n' }}"
    "{%- endif -%}"
    # User message handling
    "{%- if message.role == 'user' -%}"
    # "{{ message.content }}{{ eos_token }}{{ '\n' }}"
    # "{{ message.content }}<|im_end|>{{ '\n' }}"
    # "{{ message.content }}<end_of_utterance>{{ '\n' }}"
    # f"{content_template}<end_of_utterance>{{ '\n' }}"
    f"{content_template}" + "<end_of_utterance>{{ '\n' }}"
    "{%- endif -%}"
    # Assistant message handling
    "{%- if message.role == 'assistant' -%}"
    "{% generation %}"
    "{%- if message.tool_calls | default(false) -%}"
    f"{tool_calls_template}"
    "{%- else -%}"
    "{{ message.content }}"
    "{%- endif -%}"
    "{% endgeneration %}"
    # "{{ eos_token }}{{ '\n' }}"
    # "<|im_end|>{{ '\n' }}"
    "<end_of_utterance>{{ '\n' }}"
    "{%- endif -%}"
    # Tool message handling
    "{%- if message.role == 'tool' -%}"
    f"{tool_response_template}"
    # "{{ eos_token }}{{ '\n' }}"
    # "<|im_end|>{{ '\n' }}"
    "<end_of_utterance>{{ '\n' }}"
    "{%- endif -%}"
    "{%- endfor -%}"
    # Generation prompt
    "{%- if add_generation_prompt -%}"
    # "<|assistant|>{{ '\n' }}" # <|start_header_id|>assistant<|end_header_id|>
    # f"{assistant_generation_role_header_template}" + "{{ ' ' }}"
    f"{assistant_generation_role_header_template}"
    "{%- endif -%}"
)

# chat_template_with_tool_calls = chat_template

# {
#   "chat_template": "<|im_start|>{% for message in messages %}{{message['role'] | capitalize}}{% if message['content'][0]['type'] == 'image' %}{{':'}}{% else %}{{': '}}{% endif %}{% for line in message['content'] %}{% if line['type'] == 'text' %}{{line['text']}}{% elif line['type'] == 'image' %}{{ '<image>' }}{% endif %}{% endfor %}<end_of_utterance>\n{% endfor %}{% if add_generation_prompt %}{{ 'Assistant:' }}{% endif %}"
# }

# chat_template = "{% for message in messages %}{% if loop.first and messages[0]['role'] != 'system' %}{{ '<|im_start|>system\nYou are a helpful AI assistant<|im_end|>\n' }}{% endif %}<|im_start|>{{message['role'] | capitalize}}{% if message['content'] is string %}{{': '}}{{message['content']}}{% else %}{% if message['content'][0]['type'] == 'image' %}{{':'}}{% else %}{{': '}}{% endif %}{% for line in message['content'] %}{% if line['type'] == 'text' %}{{line['text']}}{% elif line['type'] == 'image' %}{{ '<image>' }}{% endif %}{% endfor %}{% endif %}<end_of_utterance>\n{% endfor %}{% if add_generation_prompt %}{{ 'Assistant: ' }}{% endif %}"
# chat_template = "{% for message in messages %}{% if loop.first and messages[0]['role'] != 'system' %}{{ '<|im_start|>System: You are a helpful AI assistant.<end_of_utterance>\n' }}{% endif %}<|im_start|>{{message['role'] | capitalize}}{% if message['content'] is string %}{{': '}}{{message['content']}}{% else %}{% if message['content'][0]['type'] == 'image' %}{{':'}}{% else %}{{': '}}{% endif %}{% for line in message['content'] %}{% if line['type'] == 'text' %}{{line['text']}}{% elif line['type'] == 'image' %}{{ '<image>' }}{% endif %}{% endfor %}{% endif %}<end_of_utterance>\n{% endfor %}{% if add_generation_prompt %}{{ 'Assistant: ' }}{% endif %}"
# chat_template = "<|im_start|>{% for message in messages %}{% if loop.first and messages[0]['role'] != 'system' %}{{ 'System: You are a helpful AI assistant.<end_of_utterance>\n' }}{% endif %}{{message['role'] | capitalize}}{% if message['content'] is string %}{{': '}}{{message['content']}}{% else %}{% if message['content'][0]['type'] in ['image', 'image_url'] %}{{':'}}{% else %}{{': '}}{% endif %}{% for line in message['content'] %}{% if line['type'] == 'text' %}{{line['text']}}{% elif line['type'] in ['image', 'image_url'] %}{{ '<image>' }}{% endif %}{% endfor %}{% endif %}<end_of_utterance>\n{% endfor %}{% if add_generation_prompt %}{{ 'Assistant: ' }}{% endif %}"

messages = []

# messages += [
#     {
#         "role": "user",
#         "content": [
#             {"type": "image"},
#             {"type": "image"},
#             {"type": "text", "text": "Can you describe the two images?"}
#         ]
#     },
# ]

messages += [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            },
        ],
    }
]

# messages += [{'content': 'Welcome to the chat! Please enter your name to join.', 'role': 'system'}, {'content': 'Hello! How can I help you today?', 'role': 'assistant'}, {'content': "What's 2+2?", 'role': 'user'}]


print("messages:")
pprint(messages)

# Show example of prompt generated from chat_template before setting it
prompt_before = processor.apply_chat_template(
    add_generation_prompt=True,
    conversation=messages,
    # documents=documents,
    # tools=tools,
)

print("=========================================")
print("\nprompt (before):\n")
print(prompt_before)

# Set the chat_template
processor.chat_template = chat_template
processor.tokenizer.chat_template = chat_template

# Show the same example of prompt generated from chat_template after setting it

prompt = processor.apply_chat_template(
    add_generation_prompt=True,
    conversation=messages,
    # documents=documents,
    # tools=tools,
)

print("\nprompt (after):\n")
print(prompt)

# processor.chat_template = chat_template_with_tool_calls
# processor.tokenizer.chat_template = chat_template_with_tool_calls

# prompt = processor.apply_chat_template(
#     add_generation_prompt=True,
#     conversation=messages,
#     # documents=documents,
#     # tools=tools,
# )

# print("\nprompt (with tool calls):\n")
# print(prompt)
print("=========================================")
print()

assert prompt == prompt_before, f"{prompt} != {prompt_before}"

# raise SystemExit

# print("type(processor):")
# print(type(processor))

# print("processor.chat_template (before):")
# print(processor.chat_template)

# print("processor.tokenizer.chat_template (before):")
# print(processor.tokenizer.chat_template)

assert (
    processor.chat_template == processor.tokenizer.chat_template
), f"{processor.chat_template} != {processor.tokenizer.chat_template}"

# Save the chat_template to file
with open("chat_template.txt", "w") as f:
    f.write(processor.chat_template)

# processor.chat_template = chat_template

# print('tokenizer.chat_template (after):')
# print(processor.chat_template)

print("model.config:")
print(model.config)

# print('model.text_config:')
# print(model.config.text_config)

print("model.generation_config:")
print(model.generation_config)

# assert model.config.bos_token_id == tokenizer.bos_token_id, f"{model.config.bos_token_id} != {tokenizer.bos_token_id}"

# try:
#     assert model.config.eos_token_id == tokenizer.eos_token_id, f"{model.config.eos_token_id} != {tokenizer.eos_token_id}"

# except AssertionError as e:
#     print(e)
#     model.config.eos_token_id = tokenizer.eos_token_id

# assert model.config.pad_token_id == tokenizer.pad_token_id, f"{model.config.pad_token_id} != {tokenizer.pad_token_id}"

# assert model.generation_config.bos_token_id == tokenizer.bos_token_id, f"{model.generation_config.bos_token_id} != {tokenizer.bos_token_id}"

# try:
#     assert model.generation_config.eos_token_id == tokenizer.eos_token_id, f"{model.generation_config.eos_token_id} != {tokenizer.eos_token_id}"

# except AssertionError as e:
#     print(e)
#     model.generation_config.eos_token_id = tokenizer.eos_token_id

# assert model.generation_config.pad_token_id == tokenizer.pad_token_id, f"{model.generation_config.pad_token_id} != {tokenizer.pad_token_id}"

# model.save_pretrained_merged(
#     "models/pretrained_merged_model",
#     # processing_class,
#     # tokenizer,
#     processor,
#     save_method="merged_16bit",
# )

# [3] Do model patching and add fast LoRA weights
# model = FastLanguageModel.get_peft_model(
#     model,
#     bias="none",  # Supports any, but = "none" is optimized
#     loftq_config=None,  # We support LoftQ
#     lora_alpha=16,
#     # lora_alpha=32,
#     lora_dropout=0,  # Supports any, but = 0 is optimized
#     max_seq_length=max_seq_length,
#     r=16,
#     # r = 32, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
#     random_state=42,
#     target_modules=[
#         # "embed_tokens",
#         "q_proj",
#         "k_proj",
#         "v_proj",
#         "o_proj",
#         "gate_proj",
#         "up_proj",
#         "down_proj",
#         # "lm_head",
#     ],
#     # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
#     use_gradient_checkpointing="unsloth",  # True or "unsloth" for very long context
#     use_rslora=False,  # We support rank stabilized LoRA
# )

# model.push_to_hub("mjschock/SmolVLM-Instruct", token=os.getenv("HF_TOKEN"))
# processor.push_to_hub("mjschock/SmolVLM-Instruct", token=os.getenv("HF_TOKEN"))
# model.push_to_hub_merged("mjschock/SmolVLM-Instruct", processor, save_method="merged_16bit", token=os.getenv("HF_TOKEN"))

raise SystemExit

model = FastVisionModel.get_peft_model(
    model,
    finetune_vision_layers=True,  # False if not finetuning vision layers
    finetune_language_layers=True,  # False if not finetuning language layers
    finetune_attention_modules=True,  # False if not finetuning attention layers
    finetune_mlp_modules=True,  # False if not finetuning MLP layers
    r=16,  # The larger, the higher the accuracy, but might overfit
    lora_alpha=16,  # Recommended alpha == r at least
    lora_dropout=0,
    bias="none",
    random_state=42,
    use_rslora=False,  # We support rank stabilized LoRA
    loftq_config=None,  # And LoftQ
    # target_modules = "all-linear", # Optional now! Can specify a list if needed
)

# [4] Parse output directory of checkpoints
parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=str, default="outputs")
args = parser.parse_args()

# [5] Initialize and train the model using the SFTTrainer
FastVisionModel.for_training(model)  # Enable for training!

trainer = SFTTrainer(
    # args=TrainingArguments(
    args=SFTConfig(
        bf16=is_bfloat16_supported(),
        fp16=not is_bfloat16_supported(),
        gradient_accumulation_steps=4,
        logging_steps=1,
        learning_rate=2e-4,
        # learning_rate=2e-5,
        lr_scheduler_type="linear",
        # max_steps=60,
        # max_steps=30,
        max_steps=3,
        # num_train_epochs = 1, # Set this instead of max_steps for full training runs
        optim="adamw_8bit",
        # optim = "paged_adamw_8bit",
        output_dir=args.output_dir,
        # per_device_train_batch_size=2,
        per_device_train_batch_size=1,
        # report_to="none", # Use this for WandB etc
        report_to=["mlflow"],  # TODO: Add tensorboard and get it to show up on HF
        # run_name="Training Run",
        run_name=os.getenv("SKYPILOT_TASK_ID", "Training Run"),
        # save_steps=10,
        save_steps=1,
        seed=42,
        # warmup_ratio=0.1,
        # warmup_steps=10,
        # warmup_steps=5,
        warmup_steps=1,
        weight_decay=0.01,
        # You MUST put the below items for vision finetuning:
        remove_unused_columns=False,
        dataset_text_field="",
        dataset_kwargs={"skip_prepare_dataset": True},
        dataset_num_proc=4,
        max_seq_length=2048,
    ),
    data_collator=UnslothVisionDataCollator(model, processor),  # Must use!
    # dataset_num_proc=1, # https://github.com/unslothai/unsloth?tab=readme-ov-file#windows-installation
    # dataset_text_field="text",
    # max_seq_length=max_seq_length,
    model=model,
    tokenizer=processor,
    train_dataset=dataset,
)

gpu_stats = torch.cuda.get_device_properties(0)
start_gpu_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
max_memory = round(gpu_stats.total_memory / 1024 / 1024 / 1024, 3)
print(f"\nGPU = {gpu_stats.name}. Max memory = {max_memory} GB.")
print(f"{start_gpu_memory} GB of memory reserved.\n")

# with mlflow.start_run() as run:
# trainer_stats = trainer.train()

# try:
#     trainer_stats = trainer.train()

# except torch._dynamo.exc.BackendCompilerFailed as e:
#     print(e)

torch._dynamo.config.disable = True

print("Dynamic compilation disabled")

trainer_stats = trainer.train()

used_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
used_memory_for_lora = round(used_memory - start_gpu_memory, 3)
used_percentage = round(used_memory / max_memory * 100, 3)
lora_percentage = round(used_memory_for_lora / max_memory * 100, 3)
print(f"\n{trainer_stats.metrics['train_runtime']} seconds used for training.")
print(
    f"{round(trainer_stats.metrics['train_runtime']/60, 2)} minutes used for training."
)
print(f"Peak reserved memory = {used_memory} GB.")
print(f"Peak reserved memory for training = {used_memory_for_lora} GB.")
print(f"Peak reserved memory % of max memory = {used_percentage} %.")
print(f"Peak reserved memory for training % of max memory = {lora_percentage} %.\n")

# last_active_run = mlflow.last_active_run()
run_id = mlflow.last_active_run().info.run_id
print(f"run_id: {run_id}")

model.save_pretrained("lora_model")  # Local saving
# tokenizer.save_pretrained("lora_model")
processor.save_pretrained("lora_model")

# remove the models/merged_model directory if it exists
# if os.path.exists("models/merged_model"):
# os.rmdir("models/merged_model")
# os.system("rm -rf models/merged_model")

# https://docs.unsloth.ai/basics/saving-and-using-models/saving-to-gguf - Manual Saving
# trainer.model.save_pretrained_merged(
#     "models/merged_model",
#     trainer.processing_class,
#     # maximum_memory_usage=0.5,
#     maximum_memory_usage=0.25,
#     save_method="merged_16bit",
# )

# run_id = last_active_run.info.run_id
# print_auto_logged_info(mlflow.get_run(run_id=run_id))

# subprocess.run(
#     [
#         "python",
#         "llama.cpp/convert_hf_to_gguf.py",
#         "models/merged_model/",
#         "--outfile",
#         # "models/merged_model/tinyllama-1.1B-chat-bnb-4bit-F16.gguf",
#         "models/merged_model/model-bnb-4bit-F16.gguf",
#         "--outtype",
#         "f16",
#     ]
# )

# subprocess.run(
#     [
#         "llama.cpp/build/bin/llama-quantize",
#         # "models/merged_model/tinyllama-1.1B-chat-bnb-4bit-F16.gguf",
#         "models/merged_model/model-bnb-4bit-F16.gguf",
#         # "models/merged_model/tinyllama-1.1B-chat-bnb-4bit-Q4_K_M.gguf",
#         "models/merged_model/model-bnb-4bit-Q4_K_M.gguf",
#         "Q4_K_M",
#     ]
# )

# subprocess.run(
#     [
#         "ls",
#         "-al",
#         "models/merged_model"
#     ]
# )
