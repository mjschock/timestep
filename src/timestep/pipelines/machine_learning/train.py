import argparse
import os
from pprint import pprint
from typing import Dict, List

import PIL
import mlflow
import torch
from datasets import interleave_datasets, load_dataset
from datasets.features import Features, Image, Sequence, Value
from mlflow import MlflowClient
from trl import apply_chat_template, SFTConfig, SFTTrainer
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
# dataset = load_dataset("unsloth/LaTeX_OCR", split="train[:1%]")
# dataset = load_dataset("unsloth/LaTeX_OCR", split="train", streaming=True)
# dataset = load_dataset("HuggingFaceH4/llava-instruct-mix-vsft", split="train[:1%]")
# lmms-lab/LLaVA-OneVision-Data

from datasets.features import Features, Image, Sequence, Value

# Load the streaming dataset
dataset = load_dataset("unsloth/LaTeX_OCR", split="train", streaming=True)


# def convert_to_conversation(sample, instruction, image_key="image", text_key="text"):
def convert_to_conversation(
    sample,
    indices,
    # instruction="Write the LaTeX representation for this image.",
    image_key="image",
    text_key="text",
):
    print('============================== convert_to_conversation ==============================')
    print('type(sample):')
    print(type(sample))
    print('sample:')
    print(sample)
    print('indices:')
    print(indices)
    print('image_key:')
    print(image_key)
    print('text_key:')
    print(text_key)

    messages = [
        {
            "role": "user",
            "content": [
                # {"type": "text", "text": instruction},
                {"type": "text", "text": "Write the LaTeX representation for this image."},
                # {"type": "image", "image": sample[image_key]},
                {"type": "image"},
            ],
        },
        {"role": "assistant", "content": [{"type": "text", "text": sample[text_key]}]},
    ]

    # return {"messages": messages}

    return {
        "completion": messages[1:],
        "images": [sample[image_key]],
        "prompt": messages[:1],
    }


print('dataset:')
print(dataset)
print('dataset.column_names:')
print(dataset.column_names)
print('dataset.features:')
print(dataset.features)

def create_conversation_feature():
    """
    Creates a Feature object representing a conversation with multi-modal content.
    Format:
    - Each message has a role (user/assistant) and a list of content items
    - Content items can be text or images
    
    Returns:
        datasets.Features: A Feature object for conversations
    """
    content_feature = {
        'type': Value('string'),  # 'text' or 'image'
        'text': Value('string', id=None),  # Used when type is 'text'
        'image': Value('string', id=None)  # Used when type is 'image' - stores image path/url/bytes
    }
    
    message_feature = {
        'role': Value('string'),  # 'user' or 'assistant'
        'content': Sequence(content_feature)
    }
    
    conversation_feature = Features({
        # 'messages': Sequence(message_feature)
        'completion': Sequence(message_feature),
        'images': Sequence(Image()),
        'prompt': Sequence(message_feature)
    })
    
    return conversation_feature

features = create_conversation_feature()

print('features:')
print(features)

# features = Features({
#     # "image": Image(),
#     # "messages": Sequence({
#     #     "role": Value("string"),
#     #     "content": Sequence({
#     #         "type": Value("string"),
#     #         "text": Value("string"),
#     #     }),
#     # }),
#     "messages": Sequence(feature={
#         "role": Value("string"),
#         "content": Sequence(feature={
#             "type": Value("string"),
#             "text": Value("string"),
#         }),
#     }),
#     # "text": Value("string"),
# })

# Stream the dataset and apply processing
dataset = dataset.map(
    convert_to_conversation,
    batched=False,
    # features=dataset.features,
    features=features,
    remove_columns=dataset.column_names,
    with_indices=True,
    batch_size=4
)

# dataset.column_names = ["conversations", "image", "text"]

example = dataset.take(1)
print('example:')
print(example)

print('dataset:')
print(dataset)
# dataset.column_names.append("messages")
# dataset.column_names = ["messages", "image", "text"]
print('dataset.column_names:')
print(dataset.column_names)
# assert dataset.column_names == ["messages"], f"{dataset.column_names} != ['messages']"
assert dataset.column_names == ["completion", "images", "prompt"], f"{dataset.column_names} != ['completion', 'images', 'prompt']"
# assert dataset.column_names == ["image", "messages", "text"], f"{dataset.column_names} != ['image', 'messages', 'text']"
print('dataset.features:')
print(dataset.features)

# processed_dataset.column_names = ["conversations", "image", "text"]

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

enable_system_message = True

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
    f'{{%- set messages = [{{ "content": "{DEFAULT_SYSTEM_MESSAGE["content"]}", "role": "{DEFAULT_SYSTEM_MESSAGE["role"]}" }}] + messages -%}}'
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
    # "{{ message.content }}"
    f"{content_template}"
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

# [4] Parse output directory of checkpoints
parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=str, default="outputs")
args = parser.parse_args()

# [5] Initialize and train the model using the SFTTrainer
FastVisionModel.for_training(model)  # Enable for training!

################
# Create a data collator to encode text and image pairs
################
# def collate_fn(examples):
#     # Get the texts and images, and apply the chat template
#     texts = [processor.apply_chat_template(example["messages"], tokenize=False) for example in examples]
#     tokenized_texts = [processor.apply_chat_template(example["messages"], return_assistant_tokens_mask=True, return_dict=True, return_tensors="pt", tokenize=True) for example in examples]
#     images = [example["images"] for example in examples]
#     # if isinstance(model, LlavaForConditionalGeneration):
#         # LLava1.5 does not support multiple images
#         # images = [image[0] for image in images]

#     print('tokenized_texts:')
#     print(tokenized_texts)

#     # Tokenize the texts and process the images
#     # print('type(processor):')
#     # print(type(processor))
#     batch = processor(text=texts, images=images, return_tensors="pt", padding=True)

#     # assert tokenized_texts[0]["input_ids"] == batch["input_ids"][0], f"{tokenized_texts[0]['input_ids']} != {batch['input_ids'][0]}"
#     # assert tokenized_texts[0]["attention_mask"] == batch["attention_mask"][0], f"{tokenized_texts[0]['attention_mask']} != {batch['attention_mask'][0]}"

#     # assistant_masks = torch.tensor([tokenized_text["assistant_tokens_mask"] for tokenized_text in tokenized_texts])

#     # The labels are the input_ids, and we mask the padding tokens in the loss computation
#     labels = batch["input_ids"].clone()
#     labels[labels == processor.tokenizer.pad_token_id] = -100  #

#     # Use the assistant mask to creat the labels
#     # labels = torch.where(assistant_masks == 1, labels, -100)

#     # Ignore the image token index in the loss computation (model specific)
#     image_token_id = processor.tokenizer.convert_tokens_to_ids(processor.image_token)
#     labels[labels == image_token_id] = -100  # Mask image token IDs in labels

#     batch["labels"] = labels

#     return batch

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

# train_dataset = [format_data(sample) for sample in train_dataset]
# eval_dataset = [format_data(sample) for sample in eval_dataset]
# test_dataset = [format_data(sample) for sample in test_dataset]

# image_token_id = processor.tokenizer.additional_special_tokens_ids[
#     processor.tokenizer.additional_special_tokens.index("<image>")
# ]


# def collate_fn(examples):
#     texts = [processor.apply_chat_template(example, tokenize=False) for example in examples]

#     image_inputs = []
#     for example in examples:
#         image = example[1]["content"][0]["image"]
#         if image.mode != "RGB":
#             image = image.convert("RGB")
#         image_inputs.append([image])

#     batch = processor(text=texts, images=image_inputs, return_tensors="pt", padding=True)
#     labels = batch["input_ids"].clone()
#     labels[labels == processor.tokenizer.pad_token_id] = -100  # Mask padding tokens in labels
#     labels[labels == image_token_id] = -100  # Mask image token IDs in labels

#     batch["labels"] = labels

#     return batch

from unsloth_zoo.vision_utils import (
    _get_dtype,
    get_padding_tokens_ids,
    process_vision_info,
)


class CustomUnslothVisionDataCollator:
    __slots__ = (
        "padding_token_ids",
        "dtype",
        "ignore_index",
        "processor",
        "formatting_func",
    )

    def __init__(self, model, processor, formatting_func=None, ignore_index=-100):
        self.padding_token_ids = get_padding_tokens_ids(processor)
        self.dtype = _get_dtype(
            model.config.torch_dtype
            if hasattr(model.config, "torch_dtype")
            else model.get_input_embeddings().weight.dtype
        )
        self.ignore_index = ignore_index
        self.processor = processor
        self.formatting_func = formatting_func
        return

    def __call__(self, examples):
        # [TODO] Support non image inputs as well
        # The issue is batch = self.processor( forces tensors to be returned and not None.
        texts = []
        images = []

        print("============================== __call__ ==============================")
        print("type(examples):")
        print(type(examples))

        print("examples:")
        print(examples)

        if self.formatting_func is not None:
            examples = [self.formatting_func(example) for example in examples]

        for example in examples:
            messages = example["messages"]
            message = self.processor.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False,
            )
            # Dataset with 2 columns messages / images
            if "images" in example:
                image = example["images"][0]
            else:
                image, video = process_vision_info(messages)
            texts.append(message)
            images.append(image)

        # Tokenize the texts and process the images
        batch = self.processor(
            text=texts,
            images=images,
            padding=True,
            # [TODO] Truncating to max_seq_length does NOT work for VLMs
            # truncation = True,
            return_tensors="pt",
        )
        batch.pop("token_type_ids", None)

        # Pixtral accepts multiple images, so we have to cast it individually
        pixel_values = batch["pixel_values"]
        if type(pixel_values) is list:
            for j, pixel_value_j in enumerate(pixel_values):
                if type(pixel_value_j) is list:
                    for k, pixel_value_k in enumerate(pixel_value_j):
                        pixel_value_j[k] = pixel_value_k.to(self.dtype)
                else:
                    pixel_values[j] = pixel_value_j.to(self.dtype)
            batch["pixel_values"] = pixel_values
        else:
            batch["pixel_values"] = batch["pixel_values"].to(self.dtype)

        # Mask image tokens and pad tokens
        labels = batch["input_ids"].clone()
        labels[torch.isin(labels, self.padding_token_ids)] = self.ignore_index
        batch["labels"] = labels
        return batch
    

# def collate_fn(features):
#     print('============================== collate_fn ==============================')
#     print('type(features):')
#     print(type(features))
#     print('features:')
#     print(features)
#     # Extract individual conversations
#     batch = []
#     for feature in features:
#         conversation = {
#             'messages': []
#         }
        
#         messages = feature['messages']
#         # Ensure we're working with a single conversation
#         if isinstance(messages['role'], list):
#             # Reconstruct the nested structure
#             for i in range(len(messages['role'])):
#                 message = {
#                     'role': messages['role'][i],
#                     'content': []
#                 }
                
#                 # Reconstruct content items
#         #         content_types = messages['content']['type']
#         #         content_texts = messages['content']['text']
#         #         content_images = messages['content']['image']
                
#         #         # Find the indices for this message's content
#         #         start_idx = 0
#         #         if i > 0:
#         #             start_idx = len([t for t in content_types[:i]])
#         #         end_idx = start_idx + len([t for t in content_types[i:i+1]])
                
#         #         # Add each content item
#         #         for j in range(start_idx, end_idx):
#         #             content_item = {
#         #                 'type': content_types[j],
#         #                 'text': content_texts[j] if content_texts[j] is not None else None,
#         #                 'image': content_images[j] if content_images[j] is not None else None
#         #             }
#         #             message['content'].append(content_item)
                
#         #         conversation['messages'].append(message)
#         # else:
#         #     conversation = messages  # Already in correct format
            
#         batch.append(conversation)
    
#     # Now process the reconstructed batch
#     return {
#         'conversations': batch
#     }

image_token_id = processor.tokenizer.additional_special_tokens_ids[
    processor.tokenizer.additional_special_tokens.index("<image>")
]


def collate_fn(examples):
    print('============================== collate_fn ==============================')
    # print('type(examples):')
    # print(type(examples))
    # # print('examples:')
    # print(examples)

    # e.g. examples = [{'messages': {'role': ['user', 'assistant'], 'content': [{'type': ['text', 'image'], 'text': ['Write the LaTeX representation for this image.', None], 'image': [None, '<PIL.PngImagePlugin.PngImageFile image mode=RGB size=160x40 at 0x726BCC0F63F0>']}, {'type': ['text'], 'text': ['{ \\frac { N } { M } } \\in { \\bf Z } , { \\frac { M } { P } } \\in { \\bf Z } , { \\frac { P } { Q } } \\in { \\bf Z }'], 'image': [None]}]}}]

    conversations = []

    for example in examples:
        # print('example:')
        # print(example)

        prompt = extract_messages(example, messages_key='prompt')
        # print('prompt:')

        # messages = extract_messages(example)
        completion = extract_messages(example, messages_key='completion')
        # print('completion:')
        # print(completion)

        # print('messages:')
        # print(messages)

        conversations.append({
            'completion': completion,
            'images': example['images'],
            'prompt': prompt,
            'messages': prompt + completion,
        })

        # raise ValueError('stop')

    # texts = [processor.apply_chat_template(example, tokenize=False) for example in examples]

    # texts = [processor.apply_chat_template(conversation, tokenize=False) for conversation in conversations]
    # texts = [processor.apply_chat_template(conversation['messages'], tokenize=False) for conversation in conversations]
    # prompt_batch = [processor.apply_chat_template(conversation['prompt'], add_generation_prompt=True, tokenize=False) for conversation in conversations]
    # completion_batch = [processor.apply_chat_template(conversation['completion'], add_generation_prompt=False, tokenize=False) for conversation in conversations]

    text_batch = [processor.apply_chat_template(conversation['messages'], tokenize=False) for conversation in conversations]
    tokenized_text_batch = [processor.apply_chat_template(conversation['messages'], return_assistant_tokens_mask=True, return_dict=True, return_tensors="pt", tokenize=True) for conversation in conversations]
    images_batch = [conversation['images'] for conversation in conversations]

    # print('texts:')
    # print(texts)
    # for text in texts:
        # print('text:')
        # print(text)

    for images in images_batch:
        for image in images:
            assert type(image) == PIL.PngImagePlugin.PngImageFile, f"{type(image)} != PIL.PngImagePlugin.PngImageFile"
            assert image.mode == "RGB", f"{image.mode} != RGB"

    # for (prompt, completion, images) in zip(prompt_batch, completion_batch, images_batch):
    #     print('prompt:')
    #     print(prompt)
    #     print('completion:')
    #     print(completion)
    #     print('images:')
    #     print(images)

    # for (text, images) in zip(text_batch, images_batch):
    for (text, tokenized_text, images) in zip(text_batch, tokenized_text_batch, images_batch):
        print('text:')
        print(text)
        print('tokenized_text:')
        print(tokenized_text)
        print('images:')
        print(images)

    texts = text_batch
    image_inputs = images_batch

    print('len(texts):')
    print(len(texts))

    print('len(image_inputs):')
    print(len(image_inputs))

    batch = processor(text=texts, images=image_inputs, return_tensors="pt", padding=True)
    # batch_without_image_tokens = processor(text=texts, return_tensors="pt", padding=True)
    # fake_texts = [f"<image>" for text in texts]
    # batch_without_text_tokens = processor(texts=fake_texts, images=image_inputs, return_tensors="pt", padding=True)

    # print('batch_without_image_tokens:')
    # print(batch_without_image_tokens)

    # print('batch_without_text_tokens:')
    # print(batch_without_text_tokens)

    # print('batch:')
    # print(batch)

    print('batch.keys():')
    print(batch.keys())

    attention_mask = batch["attention_mask"]
    input_ids = batch["input_ids"]
    pixel_attention_mask = batch["pixel_attention_mask"]
    pixel_values = batch["pixel_values"]

    # assert attention_mask.shape == input_ids.shape, f"{attention_mask.shape} != {input_ids.shape}"
    # assert pixel_attention_mask.shape == pixel_values.shape, f"{pixel_attention_mask.shape} != {pixel_values.shape}"

    print('additional_special_tokens:')
    print(processor.tokenizer.additional_special_tokens)

    end_of_utterance_token_id = processor.tokenizer.additional_special_tokens_ids[
        processor.tokenizer.additional_special_tokens.index("<end_of_utterance>")
    ]

    print('end_of_utterance_token_id:')
    print(end_of_utterance_token_id)

    image_token_id = processor.tokenizer.additional_special_tokens_ids[
        processor.tokenizer.additional_special_tokens.index("<image>")
    ]

    print('image_token_id:')
    print(image_token_id)

    fake_token_around_image_id = processor.tokenizer.additional_special_tokens_ids[
        processor.tokenizer.additional_special_tokens.index("<fake_token_around_image>")
    ]

    print('fake_token_around_image_id:')
    print(fake_token_around_image_id)

    print('tokenized_text_batch[0]["input_ids"]:')
    print(tokenized_text_batch[0]["input_ids"])

    print('input_ids[0]:')
    print(input_ids[0])

    # for 

    # print('input_ids_without_image_tokens[0]:')
    # print(input_ids_without_image_tokens[0])

    print('token 44:')
    print(processor.tokenizer.decode([44]))

    print('token 720:')
    print(processor.tokenizer.decode([720]))

    print('token 79:')
    print(processor.tokenizer.decode([79]))

    print('token 33:')
    print(processor.tokenizer.decode([33]))

    print('token 2283:')
    print(processor.tokenizer.decode([2283]))

    print('token 46:')
    print(processor.tokenizer.decode([46]))

    print('49152 44 720 79 33 79 2283 79 33 46 49153:')
    print(processor.tokenizer.decode([49152, 44, 720, 79, 33, 79, 2283, 79, 33, 46, 49153]))

    assistant_masks = []

    for i in range(len(input_ids)):
        assistant_mask = torch.zeros_like(input_ids[i])
        print('assistant_mask:')
        print(assistant_mask)

        print('tokenized_text_batch[i]["input_ids"][0]:')
        print(tokenized_text_batch[i]["input_ids"][0])

        print('tokenized_text_batch[i]["assistant_tokens_mask"][0]:')
        print(tokenized_text_batch[i]["assistant_masks"][0])

        offset = 0

        for j in range(len(tokenized_text_batch[i]["input_ids"][0])):
            print('tokenized_text_batch[i]["input_ids"][0][j]:')
            print(tokenized_text_batch[i]["input_ids"][0][j])

            print('input_ids[i][j+offset]:')
            print(input_ids[i][j+offset])

            # if tokenized_text_batch[i]["input_ids"][j] == image_token_id:
            if tokenized_text_batch[i]["input_ids"][0][j] == image_token_id:
                # offset += 1
                while input_ids[i][j+offset] != tokenized_text_batch[i]["input_ids"][0][j+1]:
                    offset += 1

                offset -= 1

            else:
                # assert tokenized_text_batch[i]["input_ids"][j] == input_ids[i][j+offset], f"{tokenized_text_batch[i]['input_ids'][j]} != {input_ids[i][j+offset]}"
                assert tokenized_text_batch[i]["input_ids"][0][j] == input_ids[i][j+offset], f"{tokenized_text_batch[i]['input_ids'][0][j]} != {input_ids[i][j+offset]}"

                if tokenized_text_batch[i]["assistant_masks"][j] == 1:
                    assistant_mask[j+offset] = 1

        print('assistant_mask:')
        print(assistant_mask)

        # render input ids where assistant tokens are masked

        print('input_ids[i].shape:')
        print(input_ids[i].shape)

        print('assistant_mask.shape:')
        print(assistant_mask.shape)

        print('input_ids[i][assistant_mask == 1]:')
        print(input_ids[i][assistant_mask == 1])

        print('decoded input_ids[i]:')
        decoded_assistant_input_ids = processor.tokenizer.decode(input_ids[i][assistant_mask == 1])
        print(decoded_assistant_input_ids)

        print('==============================')

        print('tokenized_text_batch[i]["input_ids"][0].shape:')
        print(tokenized_text_batch[i]["input_ids"][0].shape)

        # print('tokenized_text_batch[i]["assistant_masks"].shape:')
        # print(tokenized_text_batch[i]["assistant_masks"].shape)

        # assistant_masks = torch.tensor(tokenized_output["assistant_masks"])
        # assistant_masks = torch.tensor(tokenized_text_batch[i]["assistant_masks"])

        # print('assistant_masks.shape:')
        # print(assistant_masks.shape)

        print("tokenized_text_batch[i]['input_ids'][0]: ")
        print(tokenized_text_batch[i]["input_ids"][0])

        print("decoded tokenized_text_batch[i]['input_ids'][0]: ")
        # decoded_assistant_tokenized_text_batch_input_ids = processor.tokenizer.decode(tokenized_text_batch[i]["input_ids"][0][assistant_masks == 1])
        decoded_assistant_tokenized_text_batch_input_ids = processor.tokenizer.decode(tokenized_text_batch[i]["input_ids"][0][torch.tensor(tokenized_text_batch[i]["assistant_masks"]) == 1])
        print(decoded_assistant_tokenized_text_batch_input_ids)

        assert decoded_assistant_input_ids == decoded_assistant_tokenized_text_batch_input_ids, f"{decoded_assistant_input_ids} != {decoded_assistant_tokenized_text_batch_input_ids}"

        assistant_masks.append(assistant_mask)

    assistant_masks = torch.stack(assistant_masks)

    print('tokenized_text_batch:')
    print(tokenized_text_batch)

    print('batch:')
    print(batch)

    # print('tokenized_text_batch.keys():')
    # print(tokenized_text_batch.keys())

    print(assistant_masks)
    print(assistant_masks)

    print('batch.keys():')
    print(batch.keys())

    # labels = batch["input_ids"].clone()
    # labels = torch.where(assistant_masks == 1, batch["input_ids"], -100)
    labels = torch.where(assistant_masks == 1, input_ids, torch.tensor(-100))
    print('labels:')
    print(labels)

    return {
        "attention_mask": attention_mask,
        "input_ids": input_ids,
        "labels": labels,
        "pixel_attention_mask": pixel_attention_mask,
        "pixel_values": pixel_values,
    }

def extract_messages(example, messages_key='messages'):
    messages = []

    # for role_idx in range(len(example['messages']['role'])):
    for role_idx in range(len(example[messages_key]['role'])):
        message = {
                # 'role': example['messages']['role'][role_idx],
                'role': example[messages_key]['role'][role_idx],
                'content': []
            }

        # contents = example['messages']['content'][role_idx]
        contents = example[messages_key]['content'][role_idx]

        for content_idx in range(len(contents['type'])):
            content = {
                    'type': contents['type'][content_idx],
                    'text': contents['text'][content_idx] if contents['text'][content_idx] is not None else None,
                    'image': contents['image'][content_idx] if contents['image'][content_idx] is not None else None
                }

            message['content'].append(content)

        messages.append(message)

    return messages

    # image_inputs = []
    # for example in examples:
    #     image = example[1]["content"][0]["image"]
    #     if image.mode != "RGB":
    #         image = image.convert("RGB")
    #     image_inputs.append([image])

    # batch = processor(text=texts, images=image_inputs, return_tensors="pt", padding=True)
    # labels = batch["input_ids"].clone()
    # labels[labels == processor.tokenizer.pad_token_id] = -100  # Mask padding tokens in labels
    # labels[labels == image_token_id] = -100  # Mask image token IDs in labels

    # batch["labels"] = labels

    # return batch

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
        max_seq_length=2048,
    ),
    # data_collator=UnslothVisionDataCollator(model, processor),  # Must use! https://github.com/unslothai/unsloth-zoo/blob/main/unsloth_zoo/vision_utils.py#L243
    # data_collator=CustomUnslothVisionDataCollator(model, processor),
    # data_collator=UnslothVisionDataCollator(
    #     model, processor, formatting_func=convert_to_conversation
    # ),
    data_collator=collate_fn,
    # dataset_num_proc=1, # https://github.com/unslothai/unsloth?tab=readme-ov-file#windows-installation
    # dataset_text_field="text",
    # max_seq_length=max_seq_length,
    model=model,
    # processing_class=processor.tokenizer,
    tokenizer=processor,
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
