"""
Unified Model Server using Unsloth
"""

import asyncio
import json
import logging
import pprint
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
        model_args: Optional[FastModelArguments] = FastModelArguments(),
    ):
        self.model_args = model_args

        logger.info(f"model_args:\n{pprint.pformat(self.model_args.model_dump())}")

        self.model: Optional[PreTrainedModel] = None
        self.tokenizer: Optional[PreTrainedTokenizer] = None

        # Initialize model and tokenizer
        try:
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
                # Get all attributes and their values in alphabetical order
                props = {
                    attr: getattr(device_props, attr)
                    for attr in sorted(dir(device_props))
                    if not attr.startswith("_")
                    and not callable(getattr(device_props, attr))
                }
                logger.warning(
                    f"Disabling torch.dynamo since GPU is too old; device properties:\n{pprint.pformat(props)}"
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
        logger.info(f"step_args:\n{pprint.pformat(step_args.model_dump())}")

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

                logger.info(f"text:\n{text}\n")

                # Process each input individually
                inputs = self.tokenizer(
                    images=images,
                    return_tensors="pt",
                    text=text,
                    videos=videos,
                ).to(self.model.device, dtype=torch.bfloat16)

                with torch.no_grad():
                    generated_ids = self.model.generate(  # TODO: batch generation
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

                logger.info(f"generated_texts:\n{generated_texts}\n")

                batch_results.append(generated_texts[0])

            results.extend(batch_results)

        return results

    async def step_for_training(
        self, dataset: Dataset, step_args: Optional[StepArguments] = StepArguments()
    ) -> List[str]:
        # Ensure model is in training mode
        FastModel.for_training(self.model)

        raise NotImplementedError("Not implemented")


async def main():
    """Example usage of the ModelServer."""

    server = ModelServer()

    try:
        conversations = []

        with open("conversations.jsonl", "r") as f:
            for line in f:
                conversations.append(json.loads(line.strip()))

        dataset = Dataset.from_list(conversations)

        step_args = StepArguments(
            batch_size=2,
            do_sample=False,  # Disable sampling for faster generation
            max_new_tokens=32,  # Reduced for faster testing
            temperature=0.7,
        )

        inference_results = await server.step(
            dataset=dataset,
            step_args=step_args,
        )

        logger.info(f"inference_results:\n{pprint.pformat(inference_results)}")

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
