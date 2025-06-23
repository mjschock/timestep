"""
Unified Model Server using Unsloth
"""

import asyncio
import json
import logging
import pprint
import sys
from enum import Enum
from typing import Any, Dict, List, Optional

# isort: off
import requests
from unsloth import FastModel, is_bf16_supported
from unsloth.trainer import UnslothVisionDataCollator

# isort: on

import torch
from datasets import Dataset
from pydantic import BaseModel, ConfigDict
from transformers import (
    PreTrainedModel,
    PreTrainedTokenizer,
    StoppingCriteria,
    StoppingCriteriaList,
)
from trl import SFTConfig, SFTTrainer
from utils import process_conversation

# Configure logging
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Remove any existing handlers to avoid duplication
if root_logger.hasHandlers():
    root_logger.handlers.clear()

# Handler for stdout (INFO and WARNING levels)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.addFilter(lambda record: record.levelno <= logging.WARNING)
stdout_handler.setFormatter(logging.Formatter("%(message)s"))


# Handler for stderr (ERROR and above)
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.ERROR)
stderr_handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s: %(message)s"))

root_logger.addHandler(stdout_handler)
root_logger.addHandler(stderr_handler)

logger = logging.getLogger(__name__)


class FastModelArguments(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    auto_model: Optional[str] = None
    device_map: str = "sequential"
    dtype: Optional[torch.dtype] = None
    fix_tokenizer: bool = True  # [TODO] No effect
    full_finetuning: bool = False
    fullgraph: bool = True  # No graph breaks
    load_in_4bit: bool = True
    load_in_8bit: bool = False
    max_seq_length: int = 2048
    model_name: str = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
    resize_model_vocab: Optional[int] = None  # [TODO] No effect
    return_logits: bool = False  # Return logits
    revision: Optional[str] = None
    rope_scaling: Optional[Dict[str, Any]] = None  # [TODO] No effect
    token: Optional[str] = None
    trust_remote_code: bool = False
    unsloth_force_compile: bool = False
    use_exact_model_name: bool = False
    use_gradient_checkpointing: str = "unsloth"
    whisper_language: Optional[str] = None
    whisper_task: Optional[str] = None


class StepArguments(BaseModel):
    """Arguments for the step method."""

    class Mode(str, Enum):
        """Available modes for the step method."""

        INFERENCE = "inference"
        TRAINING = "training"

    model_config = ConfigDict(arbitrary_types_allowed=True)

    batch_size: int = 1  # Reduced from 2 to 1
    do_sample: bool = True
    max_new_tokens: int = 128
    min_p: float | None = 0.1
    mode: Mode = Mode.INFERENCE
    temperature: float | None = 0.7
    top_p: float | None = 0.9
    use_cache: bool = True


class CodeActStoppingCriteria(StoppingCriteria):
    def __init__(self, processor: PreTrainedTokenizer):
        self.processor = processor
        # Get the token IDs for "</execute>"
        self.stop_sequence = self.processor.tokenizer.encode(
            "</execute>", add_special_tokens=False
        )

    def __call__(
        self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs
    ) -> bool:
        # Get the last few tokens, looking at enough tokens to match our stop sequence
        last_tokens = input_ids[0, -len(self.stop_sequence) :].tolist()

        # If we don't have enough tokens yet, continue generating
        if len(last_tokens) < len(self.stop_sequence):
            return False

        # Check if the last tokens match our stop sequence
        return last_tokens == self.stop_sequence


class UserTokenStoppingCriteria(StoppingCriteria):
    def __init__(self, processor: PreTrainedTokenizer):
        self.processor = processor
        # Get the token IDs for "\nUser:"
        self.stop_sequence = self.processor.tokenizer.encode(
            "\nUser:", add_special_tokens=False
        )

    def __call__(
        self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs
    ) -> bool:
        # Get the last few tokens, looking at enough tokens to match our stop sequence
        last_tokens = input_ids[0, -len(self.stop_sequence) :].tolist()

        # If we don't have enough tokens yet, continue generating
        if len(last_tokens) < len(self.stop_sequence):
            return False

        # Check if the last tokens match our stop sequence
        return last_tokens == self.stop_sequence


class ModelServer:
    """Server for handling model inference tasks."""

    def __init__(
        self,
        model_args: Optional[FastModelArguments] = FastModelArguments(),
    ):
        self.model_args = model_args

        # Set memory optimization settings
        torch.cuda.empty_cache()
        torch.backends.cudnn.benchmark = True
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True

        logger.info(f"model_args:\n{pprint.pformat(self.model_args.model_dump())}\n")

        self.model: Optional[PreTrainedModel] = None
        self.tokenizer: Optional[PreTrainedTokenizer] = None

        # Initialize model and tokenizer
        try:
            # Load model using unified FastModel
            self.model, self.tokenizer = FastModel.from_pretrained(
                **self.model_args.model_dump(exclude_none=True)
            )

            # Override preprocessor parameters
            if hasattr(self.tokenizer, "image_processor"):
                # Set image size parameters to match preprocessor_config.json
                self.tokenizer.image_processor.size = {"longest_edge": 2048}
                self.tokenizer.image_processor.max_image_size = {"longest_edge": 512}

                # Set video parameters if available
                if hasattr(self.tokenizer.image_processor, "video_sampling"):
                    self.tokenizer.image_processor.video_sampling["video_size"] = {
                        "longest_edge": 512
                    }
                    self.tokenizer.image_processor.video_sampling["max_frames"] = 64
                    self.tokenizer.image_processor.video_sampling["fps"] = 1

            # Enable native 2x faster inference
            FastModel.for_inference(self.model)

            if (
                self.model.device.type == "cuda"
                and (
                    device_props := torch.cuda.get_device_properties(self.model.device)
                ).major
                < 7
            ):
                # Get all attributes and their values in alphabetical order
                props = {
                    attr: getattr(device_props, attr)
                    for attr in sorted(dir(device_props))
                    if not attr.startswith("_")
                    and not callable(getattr(device_props, attr))
                }
                logger.warning(
                    f"Disabling torch.dynamo since GPU is too old; device properties:\n{pprint.pformat(props)}\n"
                )
                torch._dynamo.config.disable = True

        except Exception as e:
            logger.error(f"Failed to initialize model: {e}")
            raise RuntimeError(f"Model initialization failed: {str(e)}")

    async def step(
        self,
        dataset: Dataset,
        step_args: Optional[StepArguments] = StepArguments(),
    ) -> List[str]:
        """
        Main step function for inference.

        Args:
            dataset: Dataset containing conversational data
            step_args: Arguments for the step method. If None, default values will be used.

        Returns:
            List of predictions
        """
        logger.info(f"step_args:\n{pprint.pformat(step_args.model_dump())}\n")

        # Validate mode
        if step_args.mode == StepArguments.Mode.INFERENCE:
            return await self.step_for_inference(dataset, step_args)

        elif step_args.mode == StepArguments.Mode.TRAINING:
            return await self.step_for_training(dataset, step_args)

        else:
            raise ValueError(f"Invalid mode: {step_args.mode}")

    async def step_for_inference(
        self, dataset: Dataset, step_args: Optional[StepArguments] = StepArguments()
    ) -> List[str]:
        # Ensure model is in inference mode
        FastModel.for_inference(self.model)

        results = []

        for batch in dataset.iter(batch_size=step_args.batch_size):
            batch_results = []

            for conversation in batch["messages"]:
                images, text, videos = process_conversation(
                    conversation, self.tokenizer
                )

                # logger.info(f"text:\n{text}\n")

                if images is not None or videos is not None:
                    if images is not None:
                        assert images[0].size == (
                            224,
                            224,
                        ), f"{images[0].size} != (224, 224)"
                    if videos is not None:
                        assert videos[0][0].size == (
                            224,
                            224,
                        ), f"{videos[0][0].size} != (224, 224)"

                # Process each input individually
                inputs = self.tokenizer(
                    images=images,
                    return_tensors="pt",
                    text=text,
                    videos=videos,
                ).to(self.model.device, dtype=torch.bfloat16)

                with torch.no_grad():
                    # Create stopping criteria
                    stopping_criteria = StoppingCriteriaList(
                        [
                            UserTokenStoppingCriteria(self.tokenizer),
                            CodeActStoppingCriteria(self.tokenizer),
                        ]
                    )

                    generation_kwargs = {
                        "max_new_tokens": step_args.max_new_tokens,
                        "use_cache": step_args.use_cache,
                        "pad_token_id": self.tokenizer.eos_token_id,
                        "stopping_criteria": stopping_criteria,
                        "do_sample": step_args.do_sample,
                    }
                    if step_args.do_sample:
                        if step_args.temperature is not None:
                            generation_kwargs["temperature"] = step_args.temperature
                        if step_args.top_p is not None:
                            generation_kwargs["top_p"] = step_args.top_p
                        if step_args.min_p is not None:
                            generation_kwargs["min_p"] = step_args.min_p

                    generated_ids = self.model.generate(  # TODO: batch generation
                        **inputs, **generation_kwargs
                    )

                generated_texts = self.tokenizer.batch_decode(
                    generated_ids,
                    skip_special_tokens=True,
                )

                # Extract only the Assistant's response and clean it up
                response = generated_texts[0].split("Assistant:")[-1].strip()

                # Remove any "User:" that might have been generated
                if "User:" in response:
                    response = response.split("User:")[0].strip()

                # If response contains <execute> tag, extract the code and result
                if "<execute>" in response and "</execute>" in response:
                    code_start = response.find("<execute>") + len("<execute>")
                    code_end = response.find("</execute>")
                    code = response[code_start:code_end].strip()

                    # Extract the result after </execute>
                    result_start = response.find("</execute>") + len("</execute>")
                    result = response[result_start:].strip()

                    # If there's an "Env:" line, use that as the result
                    if "Env:" in result:
                        response = result.split("Env:")[-1].strip()
                    else:
                        response = result

                # Remove any trailing newlines
                response = response.rstrip()

                logger.info("========================================================")
                logger.info(f"prompt:\n{text}\n")
                logger.info(f"response:\n{response}")
                logger.info("========================================================")

                batch_results.append(response)

            results.extend(batch_results)

        return results

    async def step_for_training(
        self, dataset: Dataset, step_args: Optional[StepArguments] = StepArguments()
    ) -> List[str]:
        # Ensure model is in training mode
        FastModel.for_training(self.model)

        # Print first example
        print("First example:")
        print(dataset[0])

        # Standalone preprocess function for training dataset
        # Pass the tokenizer as an argument

        def preprocess_function(example, tokenizer):
            conversation = example["messages"]
            images, text, videos = process_conversation(conversation, tokenizer)
            tokenized = tokenizer(
                images=images,
                text=text,
                videos=videos,
                return_tensors=None,  # Let Datasets handle batching
                padding="max_length",
                truncation=True,
                max_length=2048,
            )
            # Convert tensors to lists for compatibility with Datasets
            for k, v in tokenized.items():
                if hasattr(v, "tolist"):
                    tokenized[k] = v.tolist()
            return tokenized

        # Preprocess the dataset using the standalone function
        print("Tokenizing dataset...")
        tokenized_dataset = dataset.map(
            lambda ex: preprocess_function(ex, self.tokenizer), batched=False
        )
        print("First tokenized example:")
        print(tokenized_dataset[0])

        # Ensure model is in training mode
        FastModel.for_training(self.model)

        # Apply LoRA/PEFT adapters before training (do not replace self.model)
        model = FastModel.get_peft_model(
            self.model,
            finetune_vision_layers=True,
            finetune_language_layers=True,
            finetune_attention_modules=False,
            finetune_mlp_modules=True,
            r=8,
            lora_alpha=8,
            lora_dropout=0,
            bias="none",
            random_state=3407,
            use_rslora=False,
            loftq_config=None,
            # target_modules="all-linear", # Optional
        )

        trainer = SFTTrainer(
            model=model,
            tokenizer=self.tokenizer,
            data_collator=UnslothVisionDataCollator(self.tokenizer),  # Must use!
            train_dataset=tokenized_dataset,
            args=SFTConfig(
                per_device_train_batch_size=1,  # Reduce to 1 to make Pixtral fit!
                gradient_accumulation_steps=4,
                warmup_steps=5,
                max_steps=30,
                # num_train_epochs = 1, # Set this instead of max_steps for full training runs
                learning_rate=2e-4,
                fp16=not is_bf16_supported(),
                bf16=is_bf16_supported(),
                logging_steps=1,
                optim="paged_adamw_8bit",
                weight_decay=0.01,
                lr_scheduler_type="linear",
                seed=3407,
                output_dir="outputs",
                report_to="none",  # For Weights and Biases
                # You MUST put the below items for vision finetuning:
                remove_unused_columns=False,
                dataset_text_field="",
                dataset_kwargs={"skip_prepare_dataset": True},
                dataset_num_proc=4,
                max_seq_length=2048,
            ),
        )

        trainer_stats = trainer.train()

        print("trainer_stats:")
        print(trainer_stats)

        return []


def get_gaia_conversations():
    DEFAULT_API_URL = "https://agents-course-unit4-scoring.hf.space"
    api_url = DEFAULT_API_URL
    questions_url = f"{api_url}/questions"
    response = requests.get(questions_url, timeout=15)
    response.raise_for_status()
    questions_data = response.json()

    conversations = []

    # for item in questions_data[0:3]:
    #     task_id = item.get("task_id")
    #     question_text = item.get("question")

    #     if not task_id or question_text is None:
    #         print(f"Skipping item with missing task_id or question: {item}")
    #         continue

    #     # logger.info(f"question_text:\n{question_text}\n")
    #     conversation = {"messages": [{"role": "user", "content": question_text}]}

    #     logger.info(f"conversation:\n{pprint.pformat(conversation)}\n")

    #     # submitted_answer = agent(question_text)

    #     conversations.append(conversation)

    conversations.append(
        {
            "messages": [
                {
                    "content": """You are an AI agent acting as a human assistant.
You have access to the following tools:
- web_search(query: str) -> str: Search the web for the given query.

If you would like to suggest the use of one or more tools, use Python code to do so and wrap the code in <execute> tags.

User: How many r's are in the word "strawberry"?
Assistant: <execute>
web_search_query = 'How many r's are in the word "strawberry"?'
web_search_results = web_search(web_search_query)
print(web_search_results)
</execute>
Tool: There are 3 r's in the word "strawberry".
Assistant: 3

User: What is the answer to the Ultimate Question of Life, the Universe, and Everything?
Assistant: <execute>
web_search_query = 'What is the answer to the Ultimate Question of Life, the Universe, and Everything?'
web_search_results = web_search(web_search_query)
print(web_search_results)
</execute>
Tool: The answer to the Ultimate Question of Life, the Universe, and Everything is 42.
Assistant: 42
""",
                    "role": "system",
                },
                {
                    "content": "How many studio albums were published by Mercedes Sosa between 2000 and 2009 (included)? You can use the latest 2022 version of english wikipedia.",
                    "role": "user",
                },
                {
                    "content": "<execute>\nweb_search_query = 'How many studio albums were published by Mercedes Sosa between 2000 and 2009 (included)? You can use the latest 2022 version of english wikipedia.'\nweb_search_results = web_search(web_search_query)\nprint(web_search_results)\n</execute>",
                    "role": "assistant",
                },
                {
                    "content": "Mercedes Sosa has published 3 studio albums between 2000 and 2009 (included).",
                    "role": "tool",
                },
                # {
                #     "content": "3",
                #     "role": "assistant",
                # },
            ]
        }
    )

    conversations.append(
        {
            "messages": [
                {
                    "content": "In the video https://www.youtube.com/watch?v=L1vXCYZAYYM, what is the highest number of bird species to be on camera simultaneously?",
                    "role": "user",
                },
                {
                    "content": "```python\ncontent=[{'type': 'text', 'text': 'In the video https://www.youtube.com/watch?v=L1vXCYZAYYM, what is the highest number of bird species to be on camera simultaneously?'}, {'type': 'video', 'path': 'https://www.youtube.com/watch?v=L1vXCYZAYYM'}]\nprint(content)```",
                    "role": "assistant",
                },
                {
                    "content": [
                        {
                            "type": "text",
                            "text": "In the video https://www.youtube.com/watch?v=L1vXCYZAYYM, what is the highest number of bird species to be on camera simultaneously?",
                        },
                        {
                            "type": "video",
                            "path": "https://www.youtube.com/watch?v=L1vXCYZAYYM",
                        },
                    ],
                    "role": "tool",
                },
                # {
                #     "content": "10",
                #     "role": "assistant",
                # },
            ]
        }
    )

    conversations.append(
        {
            "messages": [
                {
                    "content": '.rewsna eht sa "tfel" drow eht fo etisoppo eht etirw ,ecnetnes siht dnatsrednu uoy fI',
                    "role": "user",
                },
                {
                    "content": '```python\ntext=".rewsna eht sa "tfel" drow eht fo etisoppo eht etirw ,ecnetnes siht dnatsrednu uoy fI"\nreversed_text = "".join(list(reversed(text)))\nprint(reversed_text)```',
                    "role": "assistant",
                },
                {
                    "content": 'If you understand this sentence, write the opposite of the word "left" as the answer.',
                    "role": "tool",
                },
                # {
                #     "content": "right",
                #     "role": "assistant",
                # },
            ]
        }
    )

    for conversation in conversations:
        for message in conversation["messages"]:
            if type(message["content"]) == list:
                message["content"] = json.dumps(message["content"])

    return conversations


async def main():
    """Example usage of the ModelServer."""

    server = ModelServer()

    try:
        conversations = get_gaia_conversations()

        with open("conversations.jsonl", "r") as f:
            for line in f:
                conversations.append(json.loads(line.strip()))

        conversations = conversations[0:1]

        dataset = Dataset.from_list(conversations)

        step_args = StepArguments(
            batch_size=2,
            do_sample=False,
            max_new_tokens=64,
        )

        inference_results = await server.step(
            dataset=dataset,
            step_args=step_args,
        )

        logger.info(f"inference_results:\n{pprint.pformat(inference_results)}")

        # # Load a dataset for training
        # training_dataset = load_dataset("unsloth/llava-instruct-mix-vsft-mini", split="train")

        # # Define training arguments
        # training_step_args = StepArguments(
        #     batch_size=1,
        #     mode=StepArguments.Mode.TRAINING,
        # )

        # # Start the training process
        # training_results = await server.step(
        #     dataset=training_dataset,
        #     step_args=training_step_args,
        # )

        # logger.info(f"training_results:\n{pprint.pformat(training_results)}")

    except Exception as e:
        logger.error(f"Error in main: {e}")
        raise


if __name__ == "__main__":
    # Create and set the event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        # Run the async main function
        loop.run_until_complete(main())
    finally:
        loop.close()
