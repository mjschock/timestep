import argparse
import json
import logging
import os
from datetime import datetime
from typing import Dict

import evaluate
import mlflow
import numpy as np
import torch
from data import MultiModalConversationalDataCollator, train_dataset, validation_dataset
from transformers.image_utils import load_image
from transformers.trainer_utils import EvalPrediction
from trl import SFTConfig, SFTTrainer
from unsloth import FastVisionModel, is_bfloat16_supported

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=str, default="outputs")
args = parser.parse_args()

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

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

os.environ["TOKENIZERS_PARALLELISM"] = "false"

load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.
max_seq_length = 2048  # Supports RoPE Scaling interally, so choose any!
# max_seq_length = 4096 # Choose any! We auto support RoPE Scaling internally!
seed = 42

model, processor = FastVisionModel.from_pretrained(
    "HuggingFaceTB/SmolVLM-Instruct",
    load_in_4bit=load_in_4bit,  # Use 4bit to reduce memory use. False for 16bit LoRA.
    max_seq_length=max_seq_length,  # Supports RoPE Scaling internally, so choose any!
    use_gradient_checkpointing="unsloth",  # True or "unsloth" for long context
)

logger.debug(f"model: {model}")
logger.debug(f"processor: {processor}")

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

# TODO: Probably use the other format which makes it easier to pass tools to other tools
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
    start_header_id + "{{ message.role | capitalize }}" + end_header_id
)

assistant_generation_role_header_template = (
    start_header_id + "Assistant" + end_header_id
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
    # Ensure system message exists if using tools
    "{%- if config.has_tools and not config.has_system_message -%}"
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
    f"{content_template}"
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

image1 = load_image(
    "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
)
image2 = load_image(
    "https://huggingface.co/spaces/merve/chameleon-7b/resolve/main/bee.jpg"
)

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "image"},
            {"type": "text", "text": "Can you describe the two images?"},
        ],
    },
]

# Show example of prompt generated from chat_template before setting it
prompt_before = processor.apply_chat_template(
    add_generation_prompt=True,
    conversation=messages,
)

# Set the chat_template
processor.chat_template = chat_template
processor.tokenizer.chat_template = chat_template

assert (
    processor.chat_template == processor.tokenizer.chat_template
), f"{processor.chat_template} != {processor.tokenizer.chat_template}"

with open("chat_template.txt", "w") as f:
    f.write(
        processor.chat_template
    )  # TODO: Don't write this out here, update the server to point to lora_model/chat_template.json

# Show the same example of prompt generated from chat_template after setting it
prompt = processor.apply_chat_template(
    add_generation_prompt=True,
    conversation=messages,
)

logger.debug(f"prompt_before: {prompt_before}")
logger.debug(f"prompt: {prompt}")

assert prompt == prompt_before, f"{prompt} != {prompt_before}"

# inputs = processor(text=prompt, images=[image1, image2], return_tensors="pt").to(model.device)
inputs = processor(text=prompt, images=[image2, image1], return_tensors="pt").to(
    model.device
)

try:
    generated_ids = model.generate(**inputs, max_new_tokens=500)

except torch._dynamo.exc.BackendCompilerFailed as e:
    logger.debug(e)
    logger.info("Disabling dynamo...")

    torch._dynamo.config.disable = True

    generated_ids = model.generate(**inputs, max_new_tokens=500)

generated_texts = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True,
)

print(generated_texts[0])

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
    bias="none",
    finetune_attention_modules=True,  # False if not finetuning attention layers
    finetune_language_layers=True,  # False if not finetuning language layers
    finetune_mlp_modules=True,  # False if not finetuning MLP layers
    finetune_vision_layers=True,  # False if not finetuning vision layers
    loftq_config=None,  # And LoftQ
    lora_alpha=16,  # Recommended alpha == r at least
    lora_dropout=0,
    r=16,  # The larger, the higher the accuracy, but might overfit
    random_state=seed,
    # target_modules = "all-linear", # Optional now! Can specify a list if needed
    use_rslora=False,  # We support rank stabilized LoRA
)

model.config.use_cache = False

FastVisionModel.for_training(model)  # Enable for training!


def preprocess_logits_for_metrics(
    logits: torch.Tensor, labels: torch.Tensor
) -> torch.Tensor:
    if isinstance(logits, tuple):
        logits = logits[0]

    return logits.argmax(dim=-1)


def compute_metrics(eval_pred: EvalPrediction) -> Dict:
    # metrics = evaluate.combine(
    #     ["accuracy", "bleu", "bertscore", "chrf", "meteor", "rouge", "sacrebleu", "ter"]
    # )
    # metrics = evaluate.combine(["accuracy", "bleu", "meteor", "rouge"])
    # Use metrics that work well with structured text
    metrics = evaluate.combine(["rouge"])  # Start with just ROUGE

    predictions = eval_pred.predictions
    labels = eval_pred.label_ids

    # Replace padding tokens and clip to vocab size
    predictions[predictions == -100] = processor.tokenizer.pad_token_id
    labels[labels == -100] = processor.tokenizer.pad_token_id
    predictions = np.clip(predictions, 0, processor.tokenizer.vocab_size - 1)
    labels = np.clip(labels, 0, processor.tokenizer.vocab_size - 1)

    try:
        pred_texts = processor.tokenizer.batch_decode(
            predictions, skip_special_tokens=True, clean_up_tokenization_spaces=True
        )

        label_texts = processor.tokenizer.batch_decode(
            labels, skip_special_tokens=True, clean_up_tokenization_spaces=True
        )

        # Add custom exact match metric for JSON structure
        def normalize_json_string(s):
            # Remove whitespace and normalize quotes
            return "".join(s.split())

        exact_matches = sum(
            normalize_json_string(pred) == normalize_json_string(ref)
            for pred, ref in zip(pred_texts, label_texts)
        )
        exact_match_rate = exact_matches / len(pred_texts)

        # Compute ROUGE scores
        rouge_scores = metrics.compute(predictions=pred_texts, references=label_texts)

        # Combine metrics
        results = {
            "exact_match": exact_match_rate,
            **{
                k: float(np.mean(v)) if isinstance(v, (list, np.ndarray)) else float(v)
                for k, v in rouge_scores.items()
            },
        }

        return results

    except Exception as e:
        print(f"Error in compute_metrics: {str(e)}")
        print(f"Sample prediction: {pred_texts[0][:100]}")
        print(f"Sample label: {label_texts[0][:100]}")
        raise


if os.path.exists(f"{args.output_dir}/train_dataset_state_dict.json"):
    with open(f"{args.output_dir}/train_dataset_state_dict.json", "r") as f:
        train_dataset.load_state_dict(json.loads(f.read()))

trainer = SFTTrainer(
    args=SFTConfig(
        bf16=is_bfloat16_supported(),
        dataloader_num_workers=1,
        dataset_kwargs={"skip_prepare_dataset": True},
        dataset_num_proc=1,  # https://github.com/unslothai/unsloth?tab=readme-ov-file#windows-installation
        dataset_text_field="",
        eval_on_start=True,
        fp16=not is_bfloat16_supported(),
        gradient_accumulation_steps=4,
        gradient_checkpointing=True,
        hub_model_id="mjschock/SmolVLM-Instruct-SFT",
        hub_token=os.getenv("HF_TOKEN"),
        # learning_rate=1e-5,
        learning_rate=1e-4,
        logging_steps=1,
        lr_scheduler_type="constant",
        max_seq_length=max_seq_length,
        max_steps=3,
        # num_train_epochs = 1, # Set this instead of max_steps for full training runs
        optim="adamw_bnb_8bit",
        output_dir=args.output_dir,
        per_device_eval_batch_size=1,
        per_device_train_batch_size=1,
        push_to_hub=True,
        remove_unused_columns=False,
        report_to=["mlflow", "tensorboard"],
        run_name=os.getenv(
            "SKYPILOT_TASK_ID",
            f"SmolVLM-Instruct-SFT-{datetime.now().strftime('%Y-%m-%d-%H-%M-%s')}",
        ),
        save_steps=1,
        save_total_limit=1,
        seed=seed,
        warmup_steps=0,
        weight_decay=0.01,
    ),
    compute_metrics=compute_metrics,
    data_collator=MultiModalConversationalDataCollator(model, processor),
    eval_dataset=validation_dataset,
    model=model,
    preprocess_logits_for_metrics=preprocess_logits_for_metrics,
    processing_class=processor.tokenizer,
    train_dataset=train_dataset,
)

try:
    trainer_stats = trainer.train(
        ignore_keys_for_eval=["pixel_attention_mask", "pixel_values"],
        resume_from_checkpoint=True,
        trial=None,
    )

except ValueError as e:
    if "No valid checkpoint found" in str(e):
        logger.info("No valid checkpoint found, starting from scratch...")

        trainer_stats = trainer.train(
            ignore_keys_for_eval=["pixel_attention_mask", "pixel_values"],
            resume_from_checkpoint=False,
            trial=None,
        )

    else:
        raise

with open(f"{args.output_dir}/train_dataset_state_dict.json", "w") as f:
    f.write(json.dumps(train_dataset.state_dict()))

run_id = mlflow.last_active_run().info.run_id
print(f"run_id: {run_id}")

# model.save_pretrained("lora_model")
# processor.save_pretrained("lora_model")

# Save and push to hub
# trainer.save_model(training_args.output_dir)
trainer.save_model(args.output_dir)
# if training_args.push_to_hub:
if trainer.args.push_to_hub:
    # trainer.push_to_hub(dataset_name=script_args.dataset_name)

    kwargs = {
        "dataset": [
            "mjschock/chat_threads",
            "unsloth/LaTeX_OCR",
            "xingyaoww/code-act",
        ],
        "tags": [
            "image-text-to-text",
        ],
    }

    trainer.push_to_hub(
        # language: Optional[str] = None,
        # license: Optional[str] = None,
        # tags: Union[str, List[str], None] = None,
        # model_name: Optional[str] = None,
        # finetuned_from: Optional[str] = None,
        # tasks: Union[str, List[str], None] = None,
        # dataset_tags: Union[str, List[str], None] = None,
        # dataset: Union[str, List[str], None] = None,
        # dataset_args: Union[str, List[str], None] = None,
        # dataset = [
        #     "mjschock/chat_threads",
        #     "unsloth/LaTeX_OCR",
        #     "xingyaoww/code-act",
        # ],
        **kwargs,
    )
    if trainer.accelerator.is_main_process:
        # processor.push_to_hub(training_args.hub_model_id)
        processor.push_to_hub(trainer.args.hub_model_id)
