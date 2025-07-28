#!/usr/bin/env python3
import csv
import glob
import logging
import os
import time
import uuid
from typing import Any, get_args

import torch
from datasets import load_dataset
from openai.types.fine_tuning.dpo_hyperparameters import DpoHyperparameters
from openai.types.fine_tuning.dpo_method import DpoMethod
from openai.types.fine_tuning.fine_tuning_job import (
    FineTuningJob,
    Hyperparameters,
    Method,
)
from openai.types.fine_tuning.supervised_hyperparameters import (
    SupervisedHyperparameters,
)
from openai.types.fine_tuning.supervised_method import SupervisedMethod
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from torch.nn.utils.rnn import pad_sequence
from transformers import (
    AutoModelForImageTextToText,
    AutoProcessor,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
)
from trl import DPOConfig, DPOTrainer

# Extract method type values from OpenAI API type definition

METHOD_TYPES = get_args(Method.model_fields["type"].annotation)
METHOD_TYPE_SUPERVISED, METHOD_TYPE_DPO, METHOD_TYPE_REINFORCEMENT = METHOD_TYPES

# Constants
MODEL_ID = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
OUTPUT_BASE_DIR = "data/models"
FILES_DIR = "data/files"
SMOLVLM_TARGET_MODULES = [
    "down_proj",
    "gate_proj",
    "k_proj",
    "o_proj",
    "q_proj",
    "up_proj",
    "v_proj",
]
MEMORY_CONVERSION_FACTOR = 1024**3
DEFAULT_TRAINING_FILE_ID = "file-tiger-lab-video-feedback-default"

# PEFT method constants
PEFT_METHOD_NONE = "none"
PEFT_METHOD_LORA = "lora"
PEFT_METHOD_QLORA = "qlora"


class FineTuningJobDB:
    """In-memory database for storing and managing FineTuningJob objects."""

    def __init__(self):
        self._jobs: dict[str, FineTuningJob] = {}
        self._counter = 0

    def create_job(self, fine_tuning_job: FineTuningJob) -> FineTuningJob:
        """Create and store a new fine-tuning job."""
        # Generate a unique ID if not provided or if it's a temporary ID
        if not fine_tuning_job.id or fine_tuning_job.id == "temp-id":
            self._counter += 1
            fine_tuning_job.id = f"ftjob-{int(time.time())}-{self._counter}"

        # Store the job
        self._jobs[fine_tuning_job.id] = fine_tuning_job
        logging.info(f"📝 Created job {fine_tuning_job.id} in database")
        return fine_tuning_job

    def get_job(self, job_id: str) -> FineTuningJob | None:
        """Retrieve a fine-tuning job by ID."""
        job = self._jobs.get(job_id)
        if job:
            logging.info(f"📖 Retrieved job {job_id} from database")
        else:
            logging.warning(f"⚠️  Job {job_id} not found in database")
        return job

    def update_job(
        self, job_id: str, fine_tuning_job: FineTuningJob
    ) -> FineTuningJob | None:
        """Update an existing fine-tuning job."""
        if job_id in self._jobs:
            self._jobs[job_id] = fine_tuning_job
            logging.info(f"📝 Updated job {job_id} in database")
            return fine_tuning_job
        else:
            logging.error(f"❌ Cannot update job {job_id}: not found in database")
            return None

    def list_jobs(self) -> dict[str, FineTuningJob]:
        """List all fine-tuning jobs."""
        logging.info(f"📋 Listed {len(self._jobs)} jobs from database")
        return self._jobs.copy()

    def delete_job(self, job_id: str) -> bool:
        """Delete a fine-tuning job by ID."""
        if job_id in self._jobs:
            del self._jobs[job_id]
            logging.info(f"🗑️  Deleted job {job_id} from database")
            return True
        else:
            logging.warning(f"⚠️  Cannot delete job {job_id}: not found in database")
            return False

    def clear(self):
        """Clear all jobs from the database."""
        count = len(self._jobs)
        self._jobs.clear()
        logging.info(f"🧹 Cleared {count} jobs from database")


# Global database instance
fine_tuning_db = FineTuningJobDB()


class UnifiedFineTuner:
    """Unified fine-tuning class supporting both SFT and DPO with various PEFT configurations."""

    def __init__(
        self,
        train_dataset: Any,
        fine_tuning_job: FineTuningJob,
        peft_method: str = PEFT_METHOD_QLORA,
        max_steps: int = 10,
        eval_steps: int = 5,
    ):
        """Initialize the unified fine-tuner.

        Args:
            train_dataset: Pre-prepared training dataset
            fine_tuning_job: OpenAI FineTuningJob object containing all configuration
            peft_method: PEFT configuration string (none, lora, qlora)
            max_steps: Maximum training steps
            eval_steps: Steps between evaluations
        """
        self.train_dataset = train_dataset
        self.fine_tuning_job = fine_tuning_job
        self.peft_method = peft_method
        self.max_steps = max_steps
        self.eval_steps = eval_steps

        # Extract configuration from FineTuningJob
        self.method = (
            fine_tuning_job.method.type
            if fine_tuning_job.method
            else METHOD_TYPE_SUPERVISED
        )
        self.model_id = fine_tuning_job.model
        self.training_file = fine_tuning_job.training_file
        self.validation_file = fine_tuning_job.validation_file
        self.seed = fine_tuning_job.seed
        self.metadata = fine_tuning_job.metadata

        # Detect if this is a vision dataset by checking the dataset structure
        self.has_vision = self._detect_vision_from_dataset()

        # Initialize state
        self.processor = None
        self.tokenizer = None
        self.model = None
        self.trainer = None

    def _detect_vision_from_dataset(self) -> bool:
        """Detect if the dataset contains vision data by examining its structure."""
        if not self.train_dataset or len(self.train_dataset) == 0:
            return False

        # Check the first example for vision indicators
        example = self.train_dataset[0]

        # Check for common vision indicators in the processed dataset
        vision_indicators = [
            "video link" in example,
            "videos" in example,
            "image" in example,
            "video" in example,
            "pixel_values" in example,
            "image_path" in example,
            "video_path" in example,
        ]

        # Also check if messages contain video/image content
        if "messages" in example:
            for message in example["messages"]:
                if isinstance(message.get("content"), list):
                    for content_item in message["content"]:
                        if isinstance(content_item, dict) and content_item.get(
                            "type"
                        ) in ["video", "image"]:
                            return True

        return any(vision_indicators)

    def _get_batch_size(self) -> int:
        """Get batch size from FineTuningJob method configuration."""
        method = self.fine_tuning_job.method

        if not method:
            return 1

        # Extract based on method type
        if method.type == METHOD_TYPE_SUPERVISED and method.supervised:
            batch_size = getattr(method.supervised.hyperparameters, "batch_size", 1)
            # Handle string values like "auto" or None
            if isinstance(batch_size, str) or batch_size is None:
                batch_size = 1
            return int(batch_size)
        elif method.type == METHOD_TYPE_DPO and method.dpo:
            batch_size = getattr(method.dpo.hyperparameters, "batch_size", 1)
            # Handle string values like "auto" or None
            if isinstance(batch_size, str) or batch_size is None:
                batch_size = 1
            return int(batch_size)
        else:
            return 1

    def _get_learning_rate(self) -> float:
        """Get learning rate from FineTuningJob method configuration."""
        method = self.fine_tuning_job.method

        if not method:
            return 5e-5

        # Extract based on method type
        if method.type == METHOD_TYPE_SUPERVISED and method.supervised:
            multiplier = getattr(
                method.supervised.hyperparameters, "learning_rate_multiplier", 1.0
            )
            # Handle string values like "auto" or None
            if isinstance(multiplier, str) or multiplier is None:
                multiplier = 1.0
            return float(multiplier) * 5e-5
        elif method.type == METHOD_TYPE_DPO and method.dpo:
            multiplier = getattr(
                method.dpo.hyperparameters, "learning_rate_multiplier", 1.0
            )
            # Handle string values like "auto" or None
            if isinstance(multiplier, str) or multiplier is None:
                multiplier = 1.0
            return float(multiplier) * 5e-5
        else:
            return 5e-5

    def _get_num_epochs(self) -> int:
        """Get number of epochs from FineTuningJob method configuration."""
        method = self.fine_tuning_job.method

        if not method:
            return 3  # Default to 3 epochs

        # Extract based on method type
        if method.type == METHOD_TYPE_SUPERVISED and method.supervised:
            n_epochs = getattr(method.supervised.hyperparameters, "n_epochs", 3)
            # Handle string values like "auto" or None
            if isinstance(n_epochs, str) or n_epochs is None:
                n_epochs = 3  # Map "auto" to 3 epochs
            return int(n_epochs)
        elif method.type == METHOD_TYPE_DPO and method.dpo:
            n_epochs = getattr(method.dpo.hyperparameters, "n_epochs", 3)
            # Handle string values like "auto" or None
            if isinstance(n_epochs, str) or n_epochs is None:
                n_epochs = 3  # Map "auto" to 3 epochs
            return int(n_epochs)
        else:
            return 3  # Default to 3 epochs

    def run_training(self) -> dict[str, Any]:
        """Run the complete training workflow."""
        logging.info("🚀 STARTING UNIFIED FINE-TUNING WORKFLOW")
        logging.info("=" * 80)

        try:
            self._load_processor_and_model()
            self._setup_training()

            # Run the actual training
            logging.info("🔧 STEP 3: Running training...")

            # Check for checkpoints
            model_name = self.model_id.split("/")[-1]
            suffix = (
                f"_{getattr(self.fine_tuning_job, 'suffix', '')}"
                if getattr(self.fine_tuning_job, "suffix", None)
                else ""
            )
            vision_indicator = "vision" if self.has_vision else "text"
            output_dir = f"{OUTPUT_BASE_DIR}/{model_name}-{vision_indicator}-{self.method}-{self.peft_method}{suffix}"

            checkpoints = glob.glob(f"{output_dir}/checkpoint-*")
            resume_checkpoint = None
            if checkpoints:
                checkpoints = sorted(checkpoints, key=lambda x: int(x.split("-")[-1]))
                resume_checkpoint = checkpoints[-1]
                logging.info(f"    🔄 Resuming from checkpoint: {resume_checkpoint}")
            else:
                logging.info("    🚀 Starting fresh training...")

            # Run training
            logging.info(f"    📊 Training with {self.method.upper()} method...")
            train_result = self.trainer.train(resume_from_checkpoint=resume_checkpoint)
            logging.info("    ✅ Training completed!")

            training_results = {
                "train_result": train_result,
                "output_dir": output_dir,
                "trainer": self.trainer,  # Include trainer to access log_history
            }

            # Evaluate the trained model
            logging.info("🔧 STEP 4: Evaluating model...")

            # Simple evaluation - can be enhanced
            final_mem = torch.cuda.max_memory_allocated()

            # Disable gradient checkpointing for inference
            if hasattr(self.model, "gradient_checkpointing_disable"):
                self.model.gradient_checkpointing_disable()

            evaluation_results = {
                "peak_memory_gb": final_mem / MEMORY_CONVERSION_FACTOR,
                "method": self.method,
                "peft_method": self.peft_method,
            }

            # Add method-specific metrics
            if self.method == METHOD_TYPE_SUPERVISED and hasattr(
                self.model, "get_nb_trainable_parameters"
            ):
                trainable_params = self.model.get_nb_trainable_parameters()
                evaluation_results["trainable_parameters"] = trainable_params

            logging.info("    ✅ Evaluation completed")

            # Generate training summary
            logging.info("🔧 STEP 5: Generating summary...")

            summary = {
                "model_id": self.model_id,
                "method": self.method,
                "peft_method": self.peft_method,
                "max_steps": self.max_steps,
                "batch_size": self._get_batch_size(),
                "learning_rate": self._get_learning_rate(),
                "has_vision": self.has_vision,
                "dataset_size": len(self.train_dataset),
                "output_dir": training_results["output_dir"],
                "train_result": training_results[
                    "train_result"
                ],  # Include train_result for metrics extraction
                **evaluation_results,
            }

            logging.info("📊 FINAL SUMMARY:")
            for key, value in summary.items():
                logging.info(f"    - {key}: {value}")

            return summary

        except Exception as e:
            logging.error(f"❌ Training failed: {e}")
            raise

    def _load_processor_and_model(self) -> None:
        """Load processor and model with unified configuration."""
        logging.info("🔧 STEP 1: Loading processor and model...")

        # Load SmolVLM2 processor
        logging.info(f"    📥 Loading processor from {self.model_id}")
        do_image_splitting = (
            False  # Disable image splitting for SFT to avoid string indexing issues
        )
        self.processor = AutoProcessor.from_pretrained(
            self.model_id, do_image_splitting=do_image_splitting
        )
        self.tokenizer = self.processor.tokenizer
        logging.info(
            f"    ✅ Processor loaded. Tokenizer vocab size: {len(self.tokenizer)}"
        )
        logging.info(f"        do_image_splitting: {do_image_splitting}")
        logging.info(f"        has_vision: {self.has_vision}")

        # Load model based on PEFT configuration
        self._load_model()

        # Log memory usage
        initial_mem = torch.cuda.max_memory_allocated()
        logging.info(
            f"    📊 Initial GPU memory usage: {initial_mem / MEMORY_CONVERSION_FACTOR:.2f} GB"
        )

    def _setup_training(self) -> None:
        """Setup training configuration and trainer."""
        logging.info("🔧 STEP 2: Setting up training configuration...")

        if self.method == METHOD_TYPE_SUPERVISED:
            # Setup SFT training
            logging.info("    ⚙️  Setting up SFT training...")

            # Create training arguments
            model_name = self.model_id.split("/")[-1]
            suffix = (
                f"_{getattr(self.fine_tuning_job, 'suffix', '')}"
                if getattr(self.fine_tuning_job, "suffix", None)
                else ""
            )
            vision_indicator = "vision" if self.has_vision else "text"
            output_dir = f"{OUTPUT_BASE_DIR}/{model_name}-{vision_indicator}-{self.method}-{self.peft_method}{suffix}"

            training_args = TrainingArguments(
                output_dir=output_dir,
                num_train_epochs=self._get_num_epochs(),
                per_device_train_batch_size=self._get_batch_size(),
                gradient_accumulation_steps=1,
                warmup_steps=2,
                learning_rate=self._get_learning_rate(),
                weight_decay=0.01,
                logging_steps=1,
                save_strategy="steps",
                save_steps=self.eval_steps,
                save_total_limit=1,
                max_steps=self.max_steps,
                optim="paged_adamw_8bit"
                if self.peft_method != PEFT_METHOD_NONE
                else "adamw_torch",
                bf16=True,
                remove_unused_columns=False,
                report_to="tensorboard",
                label_names=["labels"],
                dataloader_pin_memory=False,
                gradient_checkpointing=True,
                gradient_checkpointing_kwargs={"use_reentrant": False},
            )

            # Create trainer
            self.trainer = Trainer(
                model=self.model,
                args=training_args,
                data_collator=self._create_sft_collate_fn(),
                train_dataset=self.train_dataset,
            )

            logging.info("    ✅ SFT trainer configured")
        else:
            # Setup DPO training
            logging.info("    ⚙️  Setting up DPO training...")

            # Create DPO config
            model_name = self.model_id.split("/")[-1]
            suffix = (
                f"_{getattr(self.fine_tuning_job, 'suffix', '')}"
                if getattr(self.fine_tuning_job, "suffix", None)
                else ""
            )
            vision_indicator = "vision" if self.has_vision else "text"
            output_dir = f"{OUTPUT_BASE_DIR}/{model_name}-{vision_indicator}-{self.method}-{self.peft_method}{suffix}"

            training_args = DPOConfig(
                output_dir=output_dir,
                bf16=True,
                gradient_checkpointing=True,
                per_device_train_batch_size=self._get_batch_size(),
                gradient_accumulation_steps=32,
                num_train_epochs=self._get_num_epochs(),
                dataset_num_proc=8,
                dataloader_num_workers=8,
                logging_steps=1,
                max_steps=self.max_steps,
                label_names=["labels"],
                save_steps=self.eval_steps,
                save_total_limit=1,
            )

            # Create DPO trainer
            peft_config = (
                getattr(self, "lora_config", None)
                if self.peft_method != PEFT_METHOD_NONE
                else None
            )

            self.trainer = DPOTrainer(
                model=self.model,
                ref_model=None,
                args=training_args,
                train_dataset=self.train_dataset,
                peft_config=peft_config,
            )

            logging.info("    ✅ DPO trainer configured")

    def _load_model(self) -> None:
        """Load model with appropriate PEFT configuration."""
        logging.info(f"    📥 Loading model with {self.peft_method} configuration...")

        if self.peft_method == PEFT_METHOD_NONE:
            # Load model for full fine-tuning
            logging.info("        Using full fine-tuning (no PEFT)")
            self.model = self._load_base_model()

            # Freeze vision model when training on text-only datasets
            if (
                not self.has_vision
                and hasattr(self.model, "model")
                and hasattr(self.model.model, "vision_model")
            ):
                frozen_params = sum(
                    param.numel()
                    for param in self.model.model.vision_model.parameters()
                )
                for param in self.model.model.vision_model.parameters():
                    param.requires_grad = False
                logging.info(
                    f"        🧊 Frozen {frozen_params} vision model parameters (text-only dataset)"
                )
            elif self.has_vision:
                logging.info("        🔓 Vision model kept trainable (vision dataset)")

            logging.info("        ✅ Model loaded for full fine-tuning")
        else:
            # Load model with PEFT configuration
            logging.info(f"        Using {self.peft_method.upper()}")

            # Create LoRA configuration
            lora_config = LoraConfig(
                task_type=TaskType.CAUSAL_LM,
                target_modules=SMOLVLM_TARGET_MODULES,
            )
            lora_config.inference_mode = False
            logging.info(
                f"        ✅ LoRA config created: {set(SMOLVLM_TARGET_MODULES)}"
            )

            # Create quantization config if QLoRA
            bnb_config = None
            if self.peft_method == PEFT_METHOD_QLORA:
                bnb_config = BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_use_double_quant=True,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_compute_dtype=torch.bfloat16,
                )
                logging.info(
                    "        ✅ Quantization config created: 4-bit NF4 with double quant"
                )

            # Load base model
            self.model = self._load_base_model(bnb_config)
            logging.info("        ✅ Base model loaded")

            # Store LoRA config for trainer
            self.lora_config = lora_config

            # Apply PEFT for SFT (DPO handles PEFT through trainer)
            if self.method == METHOD_TYPE_SUPERVISED:
                # Apply PEFT configuration for SFT training
                logging.info("        🔗 Applying PEFT for SFT training...")

                # Verify target modules exist in the model
                linear_modules = {
                    name.split(".")[-1]
                    for name, module in self.model.named_modules()
                    if isinstance(module, torch.nn.Linear)
                }
                expected_modules = set(SMOLVLM_TARGET_MODULES)
                found_modules = expected_modules.intersection(linear_modules)
                missing_modules = expected_modules - linear_modules

                logging.info(
                    f"        ✅ Target modules found: {sorted(found_modules)}"
                )
                if missing_modules:
                    logging.warning(
                        f"        ⚠️  Target modules missing: {sorted(missing_modules)}"
                    )

                if len(missing_modules) != 0:
                    raise RuntimeError(
                        f"Expected SmolVLM2 modules missing: {missing_modules}"
                    )
                logging.info(
                    "        🎯 All expected SmolVLM2 target modules confirmed present!"
                )

                # Apply PEFT in the correct order for SFT
                self.model.add_adapter(lora_config)
                self.model.enable_adapters()
                self.model = prepare_model_for_kbit_training(self.model)
                self.model = get_peft_model(self.model, lora_config)

                # Log trainable parameters
                trainable_params = self.model.get_nb_trainable_parameters()
                logging.info(f"        📊 Trainable parameters: {trainable_params}")
                logging.info("        ✅ PEFT applied for SFT training")
            else:
                logging.info("        ✅ LoRA config prepared for DPO trainer")

    def _load_base_model(self, quantization_config=None) -> AutoModelForImageTextToText:
        """Load base model with unified loading logic."""
        kwargs = {
            "pretrained_model_name_or_path": self.model_id,
            "torch_dtype": torch.bfloat16,
            "device_map": "auto",
        }
        if quantization_config:
            kwargs["quantization_config"] = quantization_config
        return AutoModelForImageTextToText.from_pretrained(**kwargs)

    def _create_sft_collate_fn(self):
        """Create collate function for SFT training."""
        # Get special token IDs for masking
        image_token_id = None
        if hasattr(self.tokenizer, "additional_special_tokens_ids"):
            try:
                image_token_id = self.tokenizer.additional_special_tokens_ids[
                    self.tokenizer.additional_special_tokens.index("<image>")
                ]
            except (ValueError, AttributeError):
                image_token_id = None

        def collate_fn(examples):
            """SFT collate function with direct tokenization."""
            instances = []

            # Process each example directly
            for example in examples:
                # The dataset now only contains the messages field
                messages = example["messages"]

                # Create a simple conversation string instead of using apply_chat_template
                conversation = ""
                for msg in messages:
                    role = msg["role"]
                    content = msg["content"]
                    if role == "user":
                        conversation += f"User: {content}\n"
                    elif role == "assistant":
                        conversation += f"Assistant: {content}\n"
                    elif role == "system":
                        conversation += f"System: {content}\n"

                # Tokenize the conversation directly
                tokenized = self.tokenizer(
                    conversation,
                    truncation=True,
                    padding=False,
                    return_tensors="pt",
                    add_special_tokens=True,
                )

                # Move to GPU and correct dtype
                instance = {
                    "input_ids": tokenized["input_ids"].to("cuda").long(),
                    "attention_mask": tokenized["attention_mask"].to("cuda").long(),
                }
                instances.append(instance)

            # Pad sequences
            input_ids = pad_sequence(
                [inst["input_ids"].squeeze(0) for inst in instances],
                batch_first=True,
                padding_value=self.tokenizer.pad_token_id,
            )
            attention_mask = pad_sequence(
                [inst["attention_mask"].squeeze(0) for inst in instances],
                batch_first=True,
                padding_value=0,
            )
            labels = pad_sequence(
                [inst["input_ids"].squeeze(0).clone() for inst in instances],
                batch_first=True,
                padding_value=-100,
            )

            # Mask special tokens
            if image_token_id is not None:
                labels[labels == image_token_id] = -100

            result = {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "labels": labels,
            }

            # Handle pixel_values when present (for vision data)
            pvs = [
                inst.get("pixel_values")
                for inst in instances
                if inst.get("pixel_values") is not None
            ]
            if pvs:
                try:
                    result["pixel_values"] = torch.stack([pv.squeeze(0) for pv in pvs])
                except Exception as e:
                    logging.warning(f"Failed to stack pixel values: {e}")

            return result

        return collate_fn


def _create_training_metrics_file(training_results: dict[str, Any]) -> str:
    """Create a training metrics CSV file from actual training data and register it in the files service.

    Args:
        training_results: Training results containing train_result from trainer

    Returns:
        File ID of the created metrics file

    Raises:
        ValueError: If no valid training metrics are found
    """
    # Import here to avoid circular imports
    from backend.services.files_service import DATA_DIR, FILES_METADATA

    # Extract real training metrics from the trainer's log history
    train_result = training_results.get("train_result")
    trainer = training_results.get("trainer")

    if not train_result:
        raise ValueError("No train_result found in training_results")

    # Check if train_result has the expected structure
    logging.info(f"train_result type: {type(train_result)}")
    logging.info(f"train_result attributes: {dir(train_result)}")

    # Also check trainer log_history
    if trainer:
        logging.info(f"trainer type: {type(trainer)}")
        logging.info(f"trainer has log_history: {hasattr(trainer, 'log_history')}")
        if hasattr(trainer, "log_history"):
            logging.info(
                f"trainer log_history length: {len(trainer.log_history) if trainer.log_history else 0}"
            )
            logging.info(
                f"trainer log_history sample: {trainer.log_history[:2] if trainer.log_history else 'empty'}"
            )

    # Extract metrics from the trainer's log history first (preferred)
    metrics_data = []

    if trainer and hasattr(trainer, "log_history") and trainer.log_history:
        logging.info("✅ Using trainer.log_history for metrics extraction")
        for i, entry in enumerate(trainer.log_history):
            logging.info(f"Log entry {i}: {entry}")
            if "train_loss" in entry:
                metrics_row = {
                    "step": entry.get("step", i + 1),
                    "train_loss": entry.get("train_loss", 0.0),
                }
                # Add epoch if available
                if "epoch" in entry:
                    metrics_row["epoch"] = entry["epoch"]
                # Add learning rate if available
                if "learning_rate" in entry:
                    metrics_row["learning_rate"] = entry["learning_rate"]
                # Add gradient norm if available
                if "grad_norm" in entry:
                    metrics_row["grad_norm"] = entry["grad_norm"]

                metrics_data.append(metrics_row)
                logging.info(f"Added metrics row: {metrics_row}")
    elif hasattr(train_result, "log_history") and train_result.log_history:
        logging.info("✅ Using train_result.log_history for metrics extraction")
        for i, entry in enumerate(train_result.log_history):
            logging.info(f"Log entry {i}: {entry}")
            if "train_loss" in entry:
                metrics_row = {
                    "step": entry.get("step", i + 1),
                    "train_loss": entry.get("train_loss", 0.0),
                }
                # Add epoch if available
                if "epoch" in entry:
                    metrics_row["epoch"] = entry["epoch"]
                # Add learning rate if available
                if "learning_rate" in entry:
                    metrics_row["learning_rate"] = entry["learning_rate"]
                # Add gradient norm if available
                if "grad_norm" in entry:
                    metrics_row["grad_norm"] = entry["grad_norm"]

                metrics_data.append(metrics_row)
                logging.info(f"Added metrics row: {metrics_row}")
    elif hasattr(train_result, "metrics") and hasattr(train_result, "training_loss"):
        logging.info(
            "⚠️ Using train_result direct fields (fallback - only final metrics)"
        )
        logging.info(f"train_result.metrics: {train_result.metrics}")
        logging.info(f"train_result.training_loss: {train_result.training_loss}")
        logging.info(f"train_result.global_step: {train_result.global_step}")

        # Create a single metrics entry from available data
        metrics_row = {
            "step": train_result.global_step,
            "train_loss": train_result.training_loss,
        }
        # Add any additional metrics from the metrics dict
        if train_result.metrics:
            for key, value in train_result.metrics.items():
                if key not in metrics_row:  # Don't override existing keys
                    metrics_row[key] = value

        metrics_data.append(metrics_row)
        logging.info(f"Added single metrics row: {metrics_row}")
    else:
        raise ValueError(
            f"train_result does not have expected metrics structure. Available attributes: {dir(train_result)}"
        )

    if not metrics_data:
        # Log what we actually found for debugging
        logging.error(
            f"No training metrics could be extracted. train_result: {train_result}"
        )
        if trainer:
            logging.error(
                f"trainer.log_history: {getattr(trainer, 'log_history', 'not available')}"
            )
        raise ValueError(
            "No training metrics could be extracted from train_result or trainer"
        )

    logging.info(
        f"📊 Successfully extracted {len(metrics_data)} training metrics entries"
    )

    # Generate a unique file ID
    file_id = f"file-{uuid.uuid4().hex[:8]}"
    filename = "training_metrics.csv"
    file_path = os.path.join(DATA_DIR, f"{file_id}-{filename}")

    # Determine CSV fieldnames from the data
    fieldnames = set()
    for row in metrics_data:
        fieldnames.update(row.keys())
    fieldnames = sorted(fieldnames)  # Consistent ordering

    # Write CSV file
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in metrics_data:
            writer.writerow(row)

    # Calculate file size
    file_size = os.path.getsize(file_path)

    # Register file in FILES_METADATA
    file_obj = {
        "id": file_id,
        "object": "file",
        "bytes": file_size,
        "created_at": int(time.time()),
        "filename": filename,
        "purpose": "fine-tune-results",
        "status": "uploaded",
        "status_details": None,
    }
    FILES_METADATA[file_id] = file_obj

    logging.info(
        f"✅ Created training metrics file: {file_id} -> {filename} ({len(metrics_data)} entries)"
    )
    return file_id


def validate_and_load_dataset(training_file_id: str):
    """Validate and load a dataset from JSONL file.

    Args:
        training_file_id: The training file ID

    Returns:
        The loaded and validated dataset
    """
    # Import here to avoid circular imports
    from backend.services.files_service import DATA_DIR, FILES_METADATA

    # Get file metadata
    file_metadata = FILES_METADATA.get(training_file_id)
    if not file_metadata:
        raise FileNotFoundError(
            f"Training file {training_file_id} not found in metadata"
        )

    # Determine the correct file path
    if "file_path" in file_metadata:
        jsonl_file_path = file_metadata["file_path"]
    else:
        # Construct path using files service pattern
        jsonl_file_path = os.path.join(
            DATA_DIR, f"{training_file_id}-{file_metadata['filename']}"
        )

    # Check if file exists
    if not os.path.exists(jsonl_file_path):
        raise FileNotFoundError(f"Dataset file not found: {jsonl_file_path}")

    # Load dataset from JSONL

    dataset = load_dataset("json", data_files=jsonl_file_path)
    train_dataset = dataset["train"]

    # Validate the dataset format
    if len(train_dataset) == 0:
        raise ValueError(f"Dataset is empty: {jsonl_file_path}")

    # Check that all examples have the messages field
    for i, example in enumerate(train_dataset):
        if "messages" not in example:
            raise ValueError(f"Example {i} missing 'messages' field: {example}")

        messages = example["messages"]
        if not isinstance(messages, list):
            raise ValueError(
                f"Example {i} 'messages' field is not a list: {type(messages)}"
            )

        # Validate each message
        for j, message in enumerate(messages):
            if not isinstance(message, dict):
                raise ValueError(
                    f"Example {i}, message {j} is not a dict: {type(message)}"
                )

            if "role" not in message:
                raise ValueError(f"Example {i}, message {j} missing 'role' field")

            role = message["role"]
            content = message.get("content")

            if role not in ["user", "assistant", "system"]:
                raise ValueError(f"Example {i}, message {j} has invalid role: {role}")

            # Assistant messages can have tool_calls instead of content
            if role == "assistant" and content is None and "tool_calls" in message:
                # This is valid - assistant message with only tool calls
                continue

            # All other messages must have content
            if content is None:
                raise ValueError(f"Example {i}, message {j} missing 'content' field")

            # For vision data, content can be a list or string
            # For text data, content should be a string
            if not isinstance(content, str | list):
                raise ValueError(
                    f"Example {i}, message {j} content is not string or list: {type(content)}"
                )

    logging.info(
        f"✅ Loaded and validated {len(train_dataset)} examples from {jsonl_file_path}"
    )
    return train_dataset


def create_fine_tuning_job(
    method_type: str = METHOD_TYPE_SUPERVISED,
    training_file_id: str = DEFAULT_TRAINING_FILE_ID,
    model: str = MODEL_ID,
) -> str:
    """Create a fine-tuning job with the specified method type and store it in the database."""

    if method_type == METHOD_TYPE_SUPERVISED:
        method = Method(
            type="supervised",
            supervised=SupervisedMethod(
                hyperparameters=SupervisedHyperparameters(
                    batch_size="auto", learning_rate_multiplier="auto", n_epochs="auto"
                )
            ),
        )
    elif method_type == METHOD_TYPE_DPO:
        method = Method(
            type="dpo",
            dpo=DpoMethod(
                hyperparameters=DpoHyperparameters(
                    batch_size=None,
                    beta=None,
                    learning_rate_multiplier=None,
                    n_epochs=None,
                )
            ),
        )
    else:
        raise ValueError(f"Unsupported method type: {method_type}")

    # Create the job object
    fine_tuning_job = FineTuningJob(
        id="temp-id",  # Temporary ID, will be replaced by database
        created_at=int(time.time()),
        model=model,
        object="fine_tuning.job",
        organization_id="org-demo",
        result_files=[],
        seed=42,
        status="queued",  # Start with queued status since dataset is prepared
        training_file=training_file_id,
        hyperparameters=Hyperparameters(),
        method=method,
    )

    # Store in database and get the generated ID
    stored_job = fine_tuning_db.create_job(fine_tuning_job)

    return stored_job.id


def run_fine_tuning_job(job_id: str, **kwargs) -> FineTuningJob:
    """Run a fine-tuning job with OpenAI API-compatible interface."""
    import time

    logging.info(f"🔧 run_fine_tuning_job called for job {job_id}")

    # Retrieve the job from the database
    fine_tuning_job = fine_tuning_db.get_job(job_id)
    if not fine_tuning_job:
        logging.error(f"❌ Job {job_id} not found in database")
        raise ValueError(f"Job {job_id} not found in database")

    logging.info(f"📊 Found job {job_id} with status: {fine_tuning_job.status}")

    # Check job status
    if fine_tuning_job.status == "running":
        logging.error(f"❌ Job {job_id} is already running")
        raise ValueError("Resuming a fine-tuning job is not yet supported")
    elif fine_tuning_job.status not in ["queued"]:
        logging.error(
            f"❌ Job {job_id} cannot be run in status '{fine_tuning_job.status}' - expected 'queued'"
        )
        raise ValueError(
            f"Job {job_id} cannot be run in status '{fine_tuning_job.status}'"
        )

    # Update status to validating_files
    fine_tuning_job.status = "validating_files"
    fine_tuning_db.update_job(job_id, fine_tuning_job)
    logging.info(f"🔍 Job {job_id} status updated to 'validating_files'")

    # Validate dataset file and load it
    logging.info(f"📁 Starting dataset validation for job {job_id}")
    method_type = (
        fine_tuning_job.method.type
        if fine_tuning_job.method
        else METHOD_TYPE_SUPERVISED
    )
    logging.info(f"⚙️  Method type for job {job_id}: {method_type}")

    try:
        train_dataset = validate_and_load_dataset(fine_tuning_job.training_file)
        logging.info(f"✅ Dataset validation completed for job {job_id}")
    except Exception as e:
        logging.error(f"❌ Dataset validation failed for job {job_id}: {str(e)}")
        fine_tuning_job.status = "failed"
        fine_tuning_job.finished_at = int(time.time())
        fine_tuning_job.error = {
            "code": "dataset_validation_failed",
            "message": str(e),
            "param": None,
            "type": "server_error",
        }
        fine_tuning_db.update_job(job_id, fine_tuning_job)
        return fine_tuning_job

    # Update status to running
    fine_tuning_job.status = "running"
    fine_tuning_db.update_job(job_id, fine_tuning_job)
    logging.info(f"🔄 Job {job_id} status updated to 'running'")

    # Set random seed if provided
    if fine_tuning_job.seed is not None:
        torch.manual_seed(fine_tuning_job.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed(fine_tuning_job.seed)

    # Determine PEFT method based on method type
    if method_type == METHOD_TYPE_SUPERVISED:
        peft_method = PEFT_METHOD_QLORA  # Default to QLoRA for supervised
    elif method_type == METHOD_TYPE_DPO:
        peft_method = PEFT_METHOD_LORA  # Default to LoRA for DPO
    else:
        peft_method = PEFT_METHOD_QLORA  # Default fallback

    # Extract training parameters from kwargs
    max_steps = kwargs.get("max_steps", 10)
    eval_steps = kwargs.get("eval_steps", max_steps // 2 if max_steps > 1 else 1)

    # Create fine-tuner instance with pre-prepared dataset
    fine_tuner = UnifiedFineTuner(
        train_dataset=train_dataset,
        fine_tuning_job=fine_tuning_job,
        peft_method=peft_method,
        max_steps=max_steps,
        eval_steps=eval_steps,
    )

    try:
        # Run training
        training_results = fine_tuner.run_training()

        # Create a training metrics CSV file for the result
        result_file_id = _create_training_metrics_file(training_results)

        # Update the original FineTuningJob object with results
        fine_tuning_job.status = "succeeded"
        fine_tuning_job.finished_at = int(time.time())
        fine_tuning_job.result_files = [result_file_id]
        fine_tuning_job.trained_tokens = training_results.get("total_flos", 0)

        # Update the job in the database
        fine_tuning_db.update_job(job_id, fine_tuning_job)
        logging.info(f"✅ Job {job_id} completed successfully")

        return fine_tuning_job

    except Exception as e:
        # Handle training failure

        # Update the original FineTuningJob object with error information
        fine_tuning_job.status = "failed"
        fine_tuning_job.finished_at = int(time.time())
        fine_tuning_job.result_files = []
        fine_tuning_job.trained_tokens = 0

        # Add error information to the job
        fine_tuning_job.error = {
            "code": "training_failed",
            "message": str(e),
            "param": None,
            "type": "server_error",
        }

        # Update the job in the database
        fine_tuning_db.update_job(job_id, fine_tuning_job)
        logging.error(f"❌ Job {job_id} failed: {str(e)}")

        return fine_tuning_job


def cancel_job(job_id: str) -> FineTuningJob:
    """Cancel a fine-tuning job."""
    fine_tuning_job = fine_tuning_db.get_job(job_id)
    if not fine_tuning_job:
        raise ValueError(f"Job {job_id} not found in database")

    # Check if job can be cancelled
    if fine_tuning_job.status not in ["queued", "running"]:
        raise ValueError(
            f"Job {job_id} cannot be cancelled in status '{fine_tuning_job.status}'"
        )

    # Update status to cancelled
    fine_tuning_job.status = "cancelled"
    fine_tuning_job.finished_at = int(time.time())
    fine_tuning_db.update_job(job_id, fine_tuning_job)
    logging.info(f"🚫 Job {job_id} cancelled")

    return fine_tuning_job


def main():
    """Main function using OpenAI API spec types."""
    # Build OpenAI API compatible job configuration
    training_file_id = DEFAULT_TRAINING_FILE_ID
    method_type = METHOD_TYPE_SUPERVISED  # Switch back to SFT

    job_id = create_fine_tuning_job(method_type, training_file_id)

    print("🚀 Starting fine-tuning job with OpenAI API spec...")
    print(f"📋 Job ID: {job_id}")

    # Get initial job state
    initial_job = fine_tuning_db.get_job(job_id)
    print(f"🎯 Training file: {initial_job.training_file}")
    print(f"⚙️  Method: {initial_job.method.type}")
    print(f"📊 Status: {initial_job.status}")
    print(f"📅 Created at: {initial_job.created_at}")
    print(f"🔧 Model: {initial_job.model}")
    print(f"📁 Result files: {initial_job.result_files}")
    print(f"🎲 Seed: {initial_job.seed}")
    print(f"📝 Metadata: {initial_job.metadata}")
    print(f"🔗 Integrations: {initial_job.integrations}")
    print(f"📊 Hyperparameters: {initial_job.hyperparameters}")
    print(f"⚙️  Method details: {initial_job.method}")
    print(f"⏰ Finished at: {getattr(initial_job, 'finished_at', 'Not started')}")
    print(f"❌ Error: {getattr(initial_job, 'error', 'None')}")
    print(f"🔢 Trained tokens: {getattr(initial_job, 'trained_tokens', 'Not started')}")
    print(f"📈 Estimated finish: {getattr(initial_job, 'estimated_finish', 'Not set')}")
    print(f"🏷️  Suffix: {getattr(initial_job, 'suffix', 'None')}")
    print(f"🏢 Organization ID: {initial_job.organization_id}")
    print(f"📄 Validation file: {initial_job.validation_file}")
    print(f"📄 Object type: {initial_job.object}")
    print("=" * 80)

    # Run fine-tuning job using the new API
    fine_tuning_job = run_fine_tuning_job(job_id)

    # Print summary
    print("\n🎉 Fine-tuning job completed!")
    print(f"📋 Job ID: {fine_tuning_job.id}")
    print(f"📊 Status: {fine_tuning_job.status}")
    print(f"📅 Created at: {fine_tuning_job.created_at}")
    print(f"🔧 Model: {fine_tuning_job.model}")
    print(f"📁 Result files: {fine_tuning_job.result_files}")
    print(f"🎲 Seed: {fine_tuning_job.seed}")
    print(f"📝 Metadata: {fine_tuning_job.metadata}")
    print(f"🔗 Integrations: {fine_tuning_job.integrations}")
    print(f"📊 Hyperparameters: {fine_tuning_job.hyperparameters}")
    print(f"⚙️  Method details: {fine_tuning_job.method}")
    print(f"⏰ Finished at: {getattr(fine_tuning_job, 'finished_at', 'Not finished')}")
    print(f"❌ Error: {getattr(fine_tuning_job, 'error', 'None')}")
    print(
        f"🔢 Trained tokens: {getattr(fine_tuning_job, 'trained_tokens', 'Not trained')}"
    )
    print(
        f"📈 Estimated finish: {getattr(fine_tuning_job, 'estimated_finish', 'Not set')}"
    )
    print(f"🏷️  Suffix: {getattr(fine_tuning_job, 'suffix', 'None')}")
    print(f"🏢 Organization ID: {fine_tuning_job.organization_id}")
    print(f"📄 Validation file: {fine_tuning_job.validation_file}")
    print(f"📄 Object type: {fine_tuning_job.object}")

    # Demonstrate database functionality
    print("\n" + "=" * 80)
    print("🗄️  DATABASE DEMONSTRATION")
    print("=" * 80)

    # List all jobs in the database
    all_jobs = fine_tuning_db.list_jobs()
    print(f"📋 Total jobs in database: {len(all_jobs)}")
    for job_id, job in all_jobs.items():
        print(f"  - {job_id}: {job.status} ({job.method.type})")

    # Retrieve the job by ID
    retrieved_job = fine_tuning_db.get_job(fine_tuning_job.id)
    if retrieved_job:
        print(f"✅ Successfully retrieved job {retrieved_job.id} from database")
        print(f"   Status: {retrieved_job.status}")
        print(f"   Result files: {retrieved_job.result_files}")
    else:
        print(f"❌ Failed to retrieve job {fine_tuning_job.id} from database")

    # Try to retrieve a non-existent job
    non_existent_job = fine_tuning_db.get_job("ftjob-nonexistent")
    if non_existent_job is None:
        print("✅ Correctly returned None for non-existent job")

    # Demonstrate status transitions and validation
    print("\n" + "=" * 80)
    print("🔄 STATUS TRANSITIONS & VALIDATION DEMONSTRATION")
    print("=" * 80)

    # Create a new job to demonstrate cancellation
    cancel_job_id = create_fine_tuning_job(METHOD_TYPE_DPO)
    job_to_cancel = fine_tuning_db.get_job(cancel_job_id)
    print(f"📋 Created job {cancel_job_id} with status: {job_to_cancel.status}")

    # Cancel the job
    cancelled_job = cancel_job(cancel_job_id)
    print(f"🚫 Cancelled job {cancel_job_id}, new status: {cancelled_job.status}")

    # Try to run a cancelled job (should fail)
    try:
        run_fine_tuning_job(cancel_job_id)
    except ValueError as e:
        print(f"✅ Correctly prevented running cancelled job: {e}")

    # Try to run a running job (should fail)
    try:
        # First start the job
        run_fine_tuning_job(job_id)
        # Try to run it again (should fail)
        run_fine_tuning_job(job_id)
    except ValueError as e:
        print(f"✅ Correctly prevented running already running job: {e}")

    return fine_tuning_job


if __name__ == "__main__":
    results = main()
