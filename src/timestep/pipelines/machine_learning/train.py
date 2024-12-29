import argparse
import json
import os
from pprint import pprint
from typing import Dict, List, Union

import mlflow
import PIL
import torch
from datasets import interleave_datasets, load_dataset
from datasets.features import Features, Image, Sequence, Value
from mlflow import MlflowClient
from trl import SFTConfig, SFTTrainer, apply_chat_template
from unsloth import FastVisionModel, is_bfloat16_supported

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
# dataset = load_dataset("unsloth/LaTeX_OCR", split="train[:1%]")
# dataset = load_dataset("unsloth/LaTeX_OCR", split="train", streaming=True)
# dataset = load_dataset("HuggingFaceH4/llava-instruct-mix-vsft", split="train[:1%]")
# lmms-lab/LLaVA-OneVision-Data

# dataset = load_dataset("HuggingFaceH4/llava-instruct-mix-vsft", split="train[:1%]")
# dataset = load_dataset("HuggingFaceH4/llava-instruct-mix-vsft", split="train", streaming=True)

# system_message = """You are a Vision Language Model specialized in interpreting visual data from chart images.
# Your task is to analyze the provided chart image and respond to queries with concise answers, usually a single word, number, or short phrase.
# The charts include a variety of types (e.g., line charts, bar charts) and contain colors, labels, and text.
# Focus on delivering accurate, succinct answers based on the visual information. Avoid additional explanation unless absolutely necessary."""

# def format_data(sample):
#     messages = [
#         {
#             "role": "system",
#             "content": [{"type": "text", "text": system_message}],
#         },
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "image",
#                     "image": sample["image"],
#                 },
#                 {
#                     "type": "text",
#                     "text": sample["query"],
#                 },
#             ],
#         },
#         {
#             "role": "assistant",
#             "content": [{"type": "text", "text": sample["label"][0]}],
#         },
#     ]

#     return {"messages": messages}

# dataset_id = "HuggingFaceM4/ChartQA"
# train_dataset, eval_dataset, test_dataset = load_dataset(dataset_id, split=["train[:1%]", "val[:1%]", "test[:1%]"])
# # train_dataset, eval_dataset, test_dataset = load_dataset(dataset_id, split=["train", "val", "test"], streaming=True)


def create_conversation_feature():
    """
    Creates a Feature object representing a conversation with multi-modal content.
    Format:
    - Each message has a role (user/assistant) and a list of content items
    - Content items can be text or images

    Returns:
        datasets.Features: A Feature object for conversations
    """
    content_list_feature = {
        "type": Value("string"),  # 'text' or 'image'
        "text": Value("string", id=None),  # Used when type is 'text'
        "image": Value(
            "string", id=None
        ),  # Used when type is 'image' - stores image path/url/bytes
    }

    content_string_feature = Value("string")

    tool_call_feature = {
        "function": {
            "arguments": Value("string"),
            "description": Value("string"),
            "name": Value("string"),
        },
        "id": Value("string"),
        "type": Value("string"),
    }

    message_feature = {
        "content": Union[Sequence(content_list_feature), content_string_feature],
        "role": Value("string"),
        "tool_calls": Sequence(tool_call_feature),
    }

    parameters_feature = {
        "properties": Dict,
        "required": Sequence(Value("string")),
        "type": Value("string"),
    }

    tool_feature = {
        "function": {
            "description": Value("string"),
            "name": Value("string"),
            "parameters": parameters_feature,
        },
        "type": Value("string"),
    }

    conversation_feature = Features(
        {
            "completion": Sequence(message_feature),
            "images": Sequence(Image()),
            "messages": Sequence(message_feature),
            "prompt": Sequence(message_feature),
            "tools": Sequence(tool_feature),
        }
    )

    return conversation_feature


expected_column_names = [
    "completion",
    "images",
    "messages",
    "prompt",
    "tools",
]

features = create_conversation_feature()

latex_ocr_dataset = load_dataset("unsloth/LaTeX_OCR", split="train", streaming=True)


def convert_to_conversation(
    sample,
    indices,
    image_key="image",
    text_key="text",
):
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Write the LaTeX representation for this image.",
                },
                {"type": "image"},
            ],
        },
        {"role": "assistant", "content": [{"type": "text", "text": sample[text_key]}]},
    ]

    return {
        "completion": messages[1:],
        "images": [sample[image_key]],
        "prompt": messages[:1],
    }


latex_ocr_dataset = latex_ocr_dataset.map(
    convert_to_conversation,
    batched=False,
    features=features,
    remove_columns=latex_ocr_dataset.column_names,
    with_indices=True,
    batch_size=4,
)

assert (
    latex_ocr_dataset.column_names == expected_column_names
), f"{latex_ocr_dataset.column_names} != {expected_column_names}"

chat_threads_dataset = load_dataset(
    "mjschock/chat_threads", split="train", streaming=True
)


def chat_threads_dataset_function(
    sample,
    indices,
):
    messages = json.loads(sample["messages"])
    tools = json.loads(sample["tools"])

    # TODO: adjust call_id to call_0, call_1, etc.

    return {
        "messages": messages,
        "tools": tools,
    }


chat_threads_dataset = chat_threads_dataset.map(
    chat_threads_dataset_function,
    batched=False,
    features=features,
    # remove_columns=chat_threads_dataset.column_names,
    with_indices=True,
    batch_size=4,
)

assert (
    chat_threads_dataset.column_names == expected_column_names
), f"{chat_threads_dataset.column_names} != {expected_column_names}"

dataset = interleave_datasets(
    [chat_threads_dataset, latex_ocr_dataset],
    probabilities=[0.5, 0.5],
    seed=42,
    stopping_strategy="first_exhausted",
)

assert (
    dataset.column_names == expected_column_names
), f"{dataset.column_names} != {expected_column_names}"

model, processor = FastVisionModel.from_pretrained(
    "HuggingFaceTB/SmolVLM-Instruct",
    load_in_4bit=True,  # Use 4bit to reduce memory use. False for 16bit LoRA.
    max_seq_length=2048,  # Supports RoPE Scaling internally, so choose any!
    use_gradient_checkpointing="unsloth",  # True or "unsloth" for long context
)


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

# start_header_id = "<|"
# start_header_id = "<|start_header_id|>"
start_header_id = ""

# end_header_id = "|>"
# end_header_id = "<|end_header_id|>"
end_header_id = ":"

role_header_template = (
    start_header_id
    + "{{ message.role | capitalize }}"
    + end_header_id
)

assistant_generation_role_header_template = (
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
    "{%- set config.has_tools = tools is not none and tools | length > 0 -%}"
    # Ensure system message exists
    "{%- if not config.has_system_message -%}"
    f'{{%- set messages = [{{ "content": "{DEFAULT_SYSTEM_MESSAGE["content"]}", "role": "{DEFAULT_SYSTEM_MESSAGE["role"]}" }}] + messages -%}}'
    "{%- endif -%}"
    # Process messages
    "{%- for message in messages -%}"
    "{% if loop.first %}{{ bos_token }}{% endif %}"
    "{% if message.content is defined and message.content is not string and message.content[0]['type'] in ['image'] %}"
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
    "{{ eos_token }}{{ '\n' }}"
    "{%- endif -%}"
    # User message handling
    "{%- if message.role == 'user' -%}"
    f"{content_template}" + "{{ eos_token }}{{ '\n' }}"
    "{%- endif -%}"
    # Assistant message handling
    "{%- if message.role == 'assistant' -%}"
    "{% generation %}"
    "{%- if message.tool_calls is defined and message.tool_calls | length > 0 -%}"
    f"{tool_calls_template}"
    "{%- else -%}"
    f"{content_template}"
    "{%- endif -%}"
    "{% endgeneration %}"
    "{{ eos_token }}{{ '\n' }}"
    "{%- endif -%}"
    # Tool message handling
    "{%- if message.role == 'tool' -%}"
    f"{tool_response_template}"
    "{{ eos_token }}{{ '\n' }}"
    "{%- endif -%}"
    "{%- endfor -%}"
    # Generation prompt
    "{%- if add_generation_prompt -%}"
    f"{assistant_generation_role_header_template}"
    "{%- endif -%}"
)

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

print("=========================================")
print()

assert (
    processor.chat_template == processor.tokenizer.chat_template
), f"{processor.chat_template} != {processor.tokenizer.chat_template}"

# Save the chat_template to file
with open("chat_template.txt", "w") as f:
    f.write(processor.chat_template)

# model.save_pretrained_merged(
#     "models/pretrained_merged_model",
#     # processing_class,
#     # tokenizer,
#     processor,
#     save_method="merged_16bit",
# )

# model.push_to_hub("mjschock/SmolVLM-Instruct", token=os.getenv("HF_TOKEN"))
# processor.push_to_hub("mjschock/SmolVLM-Instruct", token=os.getenv("HF_TOKEN"))
# model.push_to_hub_merged("mjschock/SmolVLM-Instruct", processor, save_method="merged_16bit", token=os.getenv("HF_TOKEN"))

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

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=str, default="outputs")
args = parser.parse_args()

FastVisionModel.for_training(model)  # Enable for training!

image_token_id = processor.tokenizer.additional_special_tokens_ids[
    processor.tokenizer.additional_special_tokens.index("<image>")
]


def collate_fn(examples):
    conversations = []

    for example in examples:
        completion = extract_messages(example, messages_key="completion")
        messages = extract_messages(example, messages_key="messages")
        prompt = extract_messages(example, messages_key="prompt")
        tools = extract_tools(example)

        conversations.append(
            {
                "completion": completion,
                "images": example["images"],
                "prompt": prompt,
                "messages": prompt + completion if not messages else messages,
                "tools": tools,
            }
        )

    text_batch = [
        processor.apply_chat_template(
            add_generation_prompt=False,
            conversation=conversation["messages"],
            documents=None,
            tokenize=False,
            tools=conversation["tools"],
        )
        for conversation in conversations
    ]

    for text in text_batch:
        print("text:")
        print(text)

    tokenized_text_batch = [
        processor.apply_chat_template(
            add_generation_prompt=False,
            conversation=conversation["messages"],
            documents=None,
            return_assistant_tokens_mask=True,
            return_dict=True,
            return_tensors="pt",
            tokenize=True,
            tools=conversation["tools"],
        )
        for conversation in conversations
    ]

    images_batch = [conversation["images"] for conversation in conversations]

    for images in images_batch:
        if images is not None:
            for image in images:
                assert (
                    type(image) == PIL.PngImagePlugin.PngImageFile
                ), f"{type(image)} != PIL.PngImagePlugin.PngImageFile"
                assert image.mode == "RGB", f"{image.mode} != RGB"

    # if any images are None in the batch, we need to process them separately
    if any(images is None for images in images_batch):
        batch = {
            "attention_mask": [],
            "input_ids": [],
            "pixel_attention_mask": [],
            "pixel_values": [],
        }

        for text, images in zip(text_batch, images_batch):
            processed = processor(
                text=text, images=images, return_tensors="pt", padding=True
            )

            batch["attention_mask"].append(processed["attention_mask"])
            batch["input_ids"].append(processed["input_ids"])

            if "pixel_attention_mask" in processed:
                batch["pixel_attention_mask"].append(processed["pixel_attention_mask"])

            else:
                batch["pixel_attention_mask"].append(torch.tensor([]))

            if "pixel_values" in processed:
                batch["pixel_values"].append(processed["pixel_values"])

            else:
                batch["pixel_values"].append(torch.tensor([]))

        for key, value in batch.items():
            batch[key] = torch.cat(value, dim=0)

    else:
        batch = processor(
            text=text_batch, images=images_batch, return_tensors="pt", padding=True
        )

    assistant_masks = []

    for i in range(len(batch["input_ids"])):
        assistant_mask = torch.zeros_like(batch["input_ids"][i])
        offset = 0

        for j in range(len(tokenized_text_batch[i]["input_ids"][0])):
            if tokenized_text_batch[i]["input_ids"][0][j] == image_token_id:
                while (
                    batch["input_ids"][i][j + offset]
                    != tokenized_text_batch[i]["input_ids"][0][j + 1]
                ):
                    offset += 1

                offset -= 1

            else:
                assert (
                    tokenized_text_batch[i]["input_ids"][0][j]
                    == batch["input_ids"][i][j + offset]
                ), f"{tokenized_text_batch[i]['input_ids'][0][j]} != {batch["input_ids"][i][j+offset]}"

                if tokenized_text_batch[i]["assistant_masks"][j] == 1:
                    assistant_mask[j + offset] = 1

        decoded_assistant_input_ids = processor.tokenizer.decode(
            batch["input_ids"][i][assistant_mask == 1]
        )
        decoded_assistant_tokenized_text_batch_input_ids = processor.tokenizer.decode(
            tokenized_text_batch[i]["input_ids"][0][
                torch.tensor(tokenized_text_batch[i]["assistant_masks"]) == 1
            ]
        )

        assert (
            decoded_assistant_input_ids
            == decoded_assistant_tokenized_text_batch_input_ids
        ), f"{decoded_assistant_input_ids} != {decoded_assistant_tokenized_text_batch_input_ids}"

        assistant_masks.append(assistant_mask)

    assistant_masks = torch.stack(assistant_masks)
    labels = torch.where(assistant_masks == 1, batch["input_ids"], torch.tensor(-100))

    batch["labels"] = labels

    if len(batch["pixel_attention_mask"]) == 0:
        del batch["pixel_attention_mask"]

    if len(batch["pixel_values"]) == 0:
        del batch["pixel_values"]

    return batch


def extract_messages(example, messages_key="messages"):
    messages = []

    if example[messages_key] is None:
        return messages

    for role_idx in range(len(example[messages_key]["role"])):
        message = {"role": example[messages_key]["role"][role_idx]}

        contents = example[messages_key]["content"][role_idx]

        if type(contents) == str:
            message["content"] = contents

        elif type(contents) == list:
            message["content"] = contents

        tool_calls = example[messages_key]["tool_calls"][role_idx]

        if tool_calls is not None:
            message["tool_calls"] = []

            for tool_call_idx in range(len(tool_calls["id"])):

                tool_call = {
                    "function": {
                        "arguments": tool_calls["function"][tool_call_idx]["arguments"],
                        "description": tool_calls["function"][tool_call_idx][
                            "description"
                        ],
                        "name": tool_calls["function"][tool_call_idx]["name"],
                    },
                    "id": tool_calls["id"][tool_call_idx],
                    "type": tool_calls["type"][tool_call_idx],
                }

                message["tool_calls"].append(tool_call)

        messages.append(message)

    return messages


def extract_tools(example):
    tools = []

    if example["tools"] is None:
        return tools

    for function_idx in range(len(example["tools"]["function"])):
        tool = {
            "function": {
                "description": example["tools"]["function"][function_idx][
                    "description"
                ],
                "name": example["tools"]["function"][function_idx]["name"],
                "parameters": example["tools"]["function"][function_idx]["parameters"],
            },
            "type": example["tools"]["type"][function_idx],
        }

        tools.append(tool)

    return tools


trainer = SFTTrainer(
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
        # optim="adamw_torch_fused",
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
        # dataset_num_proc=1, # https://github.com/unslothai/unsloth?tab=readme-ov-file#windows-installation
        max_seq_length=2048,
        # max_seq_length=max_seq_length,
    ),
    data_collator=collate_fn,
    model=model,
    processing_class=processor.tokenizer,
    train_dataset=dataset,
)

gpu_stats = torch.cuda.get_device_properties(0)
start_gpu_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
max_memory = round(gpu_stats.total_memory / 1024 / 1024 / 1024, 3)
print(f"\nGPU = {gpu_stats.name}. Max memory = {max_memory} GB.")
print(f"{start_gpu_memory} GB of memory reserved.\n")

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

run_id = mlflow.last_active_run().info.run_id
print(f"run_id: {run_id}")

model.save_pretrained("lora_model")
processor.save_pretrained("lora_model")
