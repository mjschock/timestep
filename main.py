"""
Unified Model Server using Unsloth
"""

import asyncio
import json
import logging
from enum import Enum
from typing import Any, Dict, List, Optional

# isort: off
from unsloth import FastModel

# isort: on

import torch
from datasets import Dataset
from pydantic import BaseModel, ConfigDict
from transformers import PreTrainedModel, PreTrainedTokenizer

from utils import process_conversation

# Configure logging
logging.basicConfig(level=logging.INFO)
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

    model_config = ConfigDict(arbitrary_types_allowed=True)

    batch_size: int = 2
    do_sample: bool = True
    max_new_tokens: int = 128
    min_p: float = 0.1
    mode: Mode = Mode.INFERENCE
    temperature: float = 0.7
    top_p: float = 0.9
    use_cache: bool = True


class ModelServer:
    """Server for handling model inference tasks."""

    def __init__(
        self,
        model_args: Optional[FastModelArguments] = None,
    ):
        # Use provided args or default
        self.model_args = model_args or FastModelArguments()
        self.model: Optional[PreTrainedModel] = None
        self.tokenizer: Optional[PreTrainedTokenizer] = None

        # Initialize model and tokenizer
        try:
            logger.info(f"Loading model: {self.model_args.model_name}")

            # Load model using unified FastModel
            self.model, self.tokenizer = FastModel.from_pretrained(
                **self.model_args.model_dump(exclude_none=True)
            )

            # Enable native 2x faster inference
            FastModel.for_inference(self.model)

            if (
                self.model.device.type == "cuda"
                and (
                    device_props := torch.cuda.get_device_properties(self.model.device)
                ).major
                < 7
            ):
                logger.warning(
                    f"Disabling torch.dynamo since GPU is too old: {device_props}"
                )
                torch._dynamo.config.disable = True

            logger.info("Model loaded successfully")

        except Exception as e:
            logger.error(f"Failed to initialize model: {e}")
            raise RuntimeError(f"Model initialization failed: {str(e)}")

    async def step(
        self,
        dataset: Dataset,
        step_args: Optional[StepArguments] = None,
    ) -> List[str]:
        """
        Main step function for inference.

        Args:
            dataset: Dataset containing conversational data
            step_args: Arguments for the step method. If None, default values will be used.

        Returns:
            List of predictions
        """
        # Use provided args or default
        step_args = step_args or StepArguments()

        # Validate mode
        if step_args.mode != StepArguments.Mode.INFERENCE:
            raise ValueError("Currently only 'inference' mode is supported")

        logger.info(
            f"Starting inference with parameters: max_new_tokens={step_args.max_new_tokens}, "
            f"temperature={step_args.temperature}, batch_size={step_args.batch_size}"
        )

        # Ensure model is in inference mode
        FastModel.for_inference(self.model)

        example = dataset[3]

        print("example:")
        print(example)

        def format_conversation(messages):
            for message in messages:
                try:
                    message["content"] = json.loads(message["content"])
                except json.decoder.JSONDecodeError:
                    pass

            return messages

        conversation = format_conversation(example["messages"])

        print("conversation:")
        print(conversation)

        images, text, videos = process_conversation(conversation, self.tokenizer)

        inputs = self.tokenizer(
            images=images,
            text=text,
            videos=videos,
            return_tensors="pt",
        ).to(self.model.device, dtype=torch.bfloat16)

        with torch.no_grad():
            generated_ids = self.model.generate(
                **inputs,
                do_sample=step_args.do_sample,
                max_new_tokens=step_args.max_new_tokens,
                min_p=step_args.min_p,
                pad_token_id=self.tokenizer.eos_token_id,
                temperature=step_args.temperature,
                top_p=step_args.top_p,
                use_cache=step_args.use_cache,
            )

        generated_texts = self.tokenizer.batch_decode(
            generated_ids,
            skip_special_tokens=True,
        )

        print("response:")
        print(generated_texts[0])


# Example usage and testing
async def main():
    """Example usage of the ModelServer."""

    # Initialize server with default arguments
    server = ModelServer()

    try:
        # Create test dataset with three examples
        conversations = []
        with open("conversations.jsonl", "r") as f:
            for line in f:
                conversations.append(json.loads(line.strip()))

        # Normalize content in conversations before creating dataset
        normalized_conversations = []

        for conv in conversations:
            normalized_conv = {"messages": []}

            for msg in conv["messages"]:
                normalized_msg = msg.copy()

                if "content" in normalized_msg and not isinstance(
                    normalized_msg["content"], str
                ):
                    normalized_msg["content"] = json.dumps(normalized_msg["content"])

                normalized_conv["messages"].append(normalized_msg)

            normalized_conversations.append(normalized_conv)

        # Create dataset from test data
        test_dataset = Dataset.from_list(normalized_conversations)

        # Log dataset structure
        logger.info(f"Dataset structure: {test_dataset}")

        for example_i, example in enumerate(test_dataset):
            logger.info(f"Example {example_i}: {example['messages']}")

            for msg_i, msg in enumerate(example["messages"]):
                try:
                    assert (
                        json.loads(msg["content"])
                        == conversations[example_i]["messages"][msg_i]["content"]
                    ), f"{json.loads(msg['content'])} != {conversations[example_i]['messages'][msg_i]['content']}"
                except json.decoder.JSONDecodeError:
                    assert (
                        msg["content"]
                        == conversations[example_i]["messages"][msg_i]["content"]
                    ), f"{msg['content']} != {conversations[example_i]['messages'][msg_i]['content']}"

        # Test inference with minimal parameters
        logger.info("\nTesting inference...")

        step_args = StepArguments(
            batch_size=1,
            do_sample=False,  # Disable sampling for faster generation
            max_new_tokens=32,  # Reduced for faster testing
            temperature=0.7,
        )

        inference_results = await server.step(
            dataset=test_dataset,
            step_args=step_args,
        )

        logger.info(f"Inference results: {inference_results}")

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
