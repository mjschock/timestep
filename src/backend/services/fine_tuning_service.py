# Basic fine-tuning service stub using new model_utils
import os
import time
from typing import Any

from datasets import load_dataset
from openai.types.fine_tuning.fine_tuning_job import (
    Error,
    FineTuningJob,
    Hyperparameters,
    Method,
)
from openai.types.fine_tuning.supervised_hyperparameters import (
    SupervisedHyperparameters,
)
from openai.types.fine_tuning.supervised_method import SupervisedMethod

from backend._shared.dao.fine_tuning_dao import FineTuningJobDAO
from backend._shared.logging_config import logger
from backend._shared.utils.model_utils import (
    get_model,
    get_processor,
    prepare_model_inputs,
    process_model_inputs,
    process_model_outputs,
)
from backend.services.files_service import DATA_DIR, get_files_service


class FineTuningService:
    def __init__(self) -> None:
        self.logger = logger
        self.dao = FineTuningJobDAO()

    async def create_fine_tuning_job(self, request: Any) -> FineTuningJob:
        """Create a fine-tuning job."""
        self.logger.info("Creating fine-tuning job")

        # Parse request body
        body = await request.json()
        model = body.get("model", "gpt-3.5-turbo")
        training_file = body.get("training_file")
        validation_file = body.get("validation_file")
        hyperparameters = body.get("hyperparameters", {})

        if not training_file:
            raise ValueError("training_file is required")

        # # Validate that training file exists and is valid
        # files_service = get_files_service()
        # training_file_data = files_service.get_file(training_file)
        # if not training_file_data:
        #     raise ValueError(f"Training file {training_file} not found")

        # # Validate training file format (should be JSONL)
        # try:
        #     lines = training_file_data.strip().split("\n")
        #     for i, line in enumerate(lines):
        #         if line.strip():  # Skip empty lines
        #             json.loads(line)
        # except json.JSONDecodeError as e:
        #     raise ValueError(
        #         f"Training file {training_file} is not valid JSONL format: {e}"
        #     ) from e

        # # Validate validation file if specified
        # if validation_file:
        #     validation_file_data = files_service.get_file(validation_file)
        #     if not validation_file_data:
        #         raise ValueError(f"Validation file {validation_file} not found")

        #     # Validate validation file format
        #     try:
        #         lines = validation_file_data.strip().split("\n")
        #         for i, line in enumerate(lines):
        #             if line.strip():  # Skip empty lines
        #                 json.loads(line)
        #     except json.JSONDecodeError as e:
        #         raise ValueError(
        #             f"Validation file {validation_file} is not valid JSONL format: {e}"
        #         ) from e

        # Create hyperparameters
        supervised_hyperparams = SupervisedHyperparameters(
            n_epochs=hyperparameters.get("n_epochs", 3),
            batch_size=hyperparameters.get("batch_size", "auto"),
            learning_rate_multiplier=hyperparameters.get(
                "learning_rate_multiplier", "auto"
            ),
        )

        # Create method
        method = Method(
            type="supervised",
            supervised=SupervisedMethod(hyperparameters=supervised_hyperparams),
        )

        # Create the fine-tuning job
        job = FineTuningJob(
            created_at=int(time.time()),
            error=None,
            estimated_finish=None,
            finished_at=None,
            fine_tuned_model=None,
            hyperparameters=Hyperparameters(),  # Use empty Hyperparameters object
            id="temp-id",  # Will be set by DAO
            method=method,
            model=model,
            object="fine_tuning.job",
            organization_id="org-default",
            result_files=[],
            seed=42,  # Use a default seed value
            status="queued",
            trained_tokens=None,
            training_file=training_file,
            validation_file=validation_file,
        )

        # Save to database
        created_job = self.dao.create(job)

        self.logger.info(
            f"Created fine-tuning job {created_job.id} with status 'queued'"
        )
        return created_job

    def start_fine_tuning_job(self, job_id: str) -> None:
        """Start fine-tuning for a specific job."""
        self.logger.info(f"Starting fine-tuning for job {job_id}")

        try:
            # Update job status to "running"
            job = self.dao.get_by_id(job_id)
            if job:
                job.status = "running"
                self.dao.update(job_id, job)

            # Load model for training
            model = get_model(train=True)
            processor = get_processor()

            # Load training and validation files
            files_service = get_files_service()

            # # Load training file
            # training_file_data = files_service.get_file(job.training_file)
            # if not training_file_data:
            #     raise ValueError(f"Training file {job.training_file} not found")

            # # Load validation file if specified
            # validation_file_data = None
            # if job.validation_file:
            #     validation_file_data = files_service.get_file(job.validation_file)
            #     if not validation_file_data:
            #         raise ValueError(f"Validation file {job.validation_file} not found")

            training_file_info = files_service.retrieve_file(job.training_file)

            print("training_file_info", training_file_info)

            # file_path = os.path.join(DATA_DIR, file_id + "-" + filename)

            data_files = {
                # "training": os.path.join(DATA_DIR, training_file_info.id + "-" + training_file_info.filename)
                "train": os.path.join(
                    DATA_DIR,
                    training_file_info["id"] + "-" + training_file_info["filename"],
                )
            }

            if job.validation_file:
                validation_file_info = files_service.retrieve_file(job.validation_file)
                data_files["eval"] = os.path.join(
                    DATA_DIR,
                    validation_file_info.id + "-" + validation_file_info.filename,
                )

            dataset = load_dataset(
                "json", data_files=data_files
            )  # TODO: Optionally, stream=True

            print("dataset", dataset)
            print(f"Dataset keys: {list(dataset.keys())}")
            print(f"Dataset features: {dataset[list(dataset.keys())[0]].features}")

            # Extract hyperparameters from job and map to TrainingArguments
            training_kwargs = {}
            if (
                job.method
                and job.method.supervised
                and job.method.supervised.hyperparameters
            ):
                hyperparams = job.method.supervised.hyperparameters

                # Map hyperparameters to TrainingArguments parameter names
                if hyperparams.n_epochs and hyperparams.n_epochs != "auto":
                    training_kwargs["num_train_epochs"] = int(hyperparams.n_epochs)

                if hyperparams.batch_size and hyperparams.batch_size != "auto":
                    training_kwargs["per_device_train_batch_size"] = int(
                        hyperparams.batch_size
                    )

                if (
                    hyperparams.learning_rate_multiplier
                    and hyperparams.learning_rate_multiplier != "auto"
                ):
                    # learning_rate_multiplier affects the base learning rate
                    base_learning_rate = 2e-3  # Default from model_utils.py
                    training_kwargs["learning_rate"] = base_learning_rate * float(
                        hyperparams.learning_rate_multiplier
                    )

            self.logger.info(f"Using training kwargs: {training_kwargs}")

            # Process training data
            model_inputs = prepare_model_inputs(
                dataset=dataset,
                model=model,
                processor=processor,
            )

            # Get collate function and run training with hyperparameters
            model_outputs = process_model_inputs(
                data_collator=model_inputs["data_collator"],
                model=model,
                processor=processor,
                train_dataset=model_inputs["train_dataset"],
                training_kwargs=training_kwargs,
            )

            # Run training
            training_results = process_model_outputs(
                model_outputs=model_outputs,
                processor=processor,
            )

            self.logger.info("Fine-tuning completed successfully")

            # Create result file with training metrics
            result_file_id = None
            if training_results and "train_result" in training_results:
                train_result = training_results["train_result"]
                self.logger.info(f"Train result type: {type(train_result)}")
                self.logger.info(f"Train result attributes: {dir(train_result)}")

                # Try to get log_history from trainer_state.json
                import json

                # Get the model path from training results
                model_path = training_results.get("model_path")
                self.logger.info(f"Model path from training results: {model_path}")

                # Look for trainer_state.json in checkpoint subdirectories (like checkpoint-26)
                trainer_state_path = None
                if model_path and os.path.exists(model_path):
                    import glob

                    checkpoint_pattern = os.path.join(
                        model_path, "checkpoint-*", "trainer_state.json"
                    )
                    checkpoint_files = glob.glob(checkpoint_pattern)

                    if checkpoint_files:
                        # Use the most recent checkpoint (highest number)
                        trainer_state_path = max(
                            checkpoint_files,
                            key=lambda x: int(x.split("checkpoint-")[1].split("/")[0]),
                        )
                        self.logger.info(
                            f"Found trainer_state.json at: {trainer_state_path}"
                        )
                    else:
                        # Fallback: look directly in model_path
                        direct_path = os.path.join(model_path, "trainer_state.json")
                        if os.path.exists(direct_path):
                            trainer_state_path = direct_path
                            self.logger.info(
                                f"Found trainer_state.json directly at: {trainer_state_path}"
                            )
                        else:
                            self.logger.info(
                                f"No trainer_state.json found in {model_path} or its checkpoints"
                            )

                # Read trainer_state.json if found
                log_history = []
                if trainer_state_path and os.path.exists(trainer_state_path):
                    with open(trainer_state_path) as f:
                        trainer_state = json.load(f)

                    log_history = trainer_state.get("log_history", [])
                    self.logger.info(
                        f"Found {len(log_history)} log entries in trainer_state.json"
                    )
                else:
                    self.logger.info(
                        "Using TrainOutput data only (no trainer_state.json found)"
                    )

                # Create CSV content in OpenAI fine-tuning results format
                import csv
                import io

                csv_buffer = io.StringIO()
                writer = csv.writer(csv_buffer)

                # Write header matching OpenAI format (as shown in the example)
                writer.writerow(
                    [
                        "step",
                        "train_loss",
                        "train_accuracy",
                        "valid_loss",
                        "valid_mean_token_accuracy",
                    ]
                )

                # Write training steps from log_history if available, otherwise use TrainOutput
                if log_history:
                    # Write all training steps from detailed log history
                    for log_entry in log_history:
                        if "loss" in log_entry:  # Only write training step entries
                            writer.writerow(
                                [
                                    log_entry.get("step", ""),
                                    log_entry.get(
                                        "train_loss", log_entry.get("loss", "")
                                    ),
                                    "",  # train_accuracy not available in our training
                                    "",  # valid_loss not available
                                    "",  # valid_mean_token_accuracy not available
                                ]
                            )
                elif hasattr(train_result, "training_loss") and hasattr(
                    train_result, "global_step"
                ):
                    # Fallback: Use TrainOutput data
                    self.logger.info(
                        f"Using TrainOutput: loss={train_result.training_loss}, steps={train_result.global_step}"
                    )
                    writer.writerow(
                        [
                            train_result.global_step,
                            train_result.training_loss,
                            "",  # train_accuracy not available
                            "",  # valid_loss not available
                            "",  # valid_mean_token_accuracy not available
                        ]
                    )
                else:
                    # Write at least one row with placeholder data
                    writer.writerow([1, 0.0, "", "", ""])

                csv_content = csv_buffer.getvalue()
                self.logger.info(
                    f"Training metrics CSV content length: {len(csv_content)}"
                )
                self.logger.info(f"Training metrics CSV preview: {csv_content[:500]}")

                # Create result file via files API (as shown in the example)
                try:
                    import requests

                    csv_bytes = csv_content.encode("utf-8")
                    csv_file = io.BytesIO(csv_bytes)
                    csv_file.name = f"training_metrics_{job_id}.csv"

                    # Make request to files API to create the results file
                    files_data = {"purpose": "fine-tune-results"}
                    files = {
                        "file": (
                            f"training_metrics_{job_id}.csv",
                            csv_file,
                            "text/csv",
                        )
                    }

                    response = requests.post(
                        "http://localhost:8000/v1/files",
                        data=files_data,
                        files=files,
                        timeout=30,
                    )
                    response.raise_for_status()
                    result_file_data = response.json()
                    result_file_id = result_file_data["id"]
                    self.logger.info(
                        f"Successfully created training result file with ID: {result_file_id}"
                    )
                    # Now it can be retrieved like: client.files.retrieve_content(result_file_id)
                except Exception as e:
                    self.logger.error(
                        f"Failed to create result file via files API: {e}"
                    )
                    import traceback

                    self.logger.error(f"Full traceback: {traceback.format_exc()}")
                    result_file_id = None
            else:
                self.logger.warning("No train_result in training_results")

            # Update job status to "succeeded" and set fine_tuned_model
            if job:
                job.status = "succeeded"
                job.finished_at = int(time.time())

                # Set the fine_tuned_model to the model path from training results
                if training_results and "model_path" in training_results:
                    job.fine_tuned_model = training_results["model_path"]

                # Set result files
                if result_file_id:
                    job.result_files = [result_file_id]

                self.dao.update(job_id, job)

        except Exception as e:
            self.logger.error(f"Fine-tuning failed for job {job_id}: {e}")
            # Update job status to "failed"
            job = self.dao.get_by_id(job_id)
            if job:
                job.status = "failed"
                job.error = Error(
                    code="training_failed",
                    message=str(e),
                    param=None,
                )
                job.finished_at = int(time.time())
                self.dao.update(job_id, job)

    def run_grader(self) -> dict[str, Any]:
        """Run a grader."""
        return {"status": "not_implemented"}

    def validate_grader(self) -> dict[str, Any]:
        """Validate a grader."""
        return {"status": "not_implemented"}

    def list_fine_tuning_checkpoint_permissions(self) -> dict[str, Any]:
        """List fine-tuning checkpoint permissions."""
        return {"status": "not_implemented"}

    def create_fine_tuning_checkpoint_permission(self) -> dict[str, Any]:
        """Create fine-tuning checkpoint permission."""
        return {"status": "not_implemented"}

    def delete_fine_tuning_checkpoint_permission(self) -> dict[str, Any]:
        """Delete fine-tuning checkpoint permission."""
        return {"status": "not_implemented"}

    def list_paginated_fine_tuning_jobs(
        self, after: str = None, limit: str = None, metadata: str = None
    ) -> dict[str, Any]:
        """List paginated fine-tuning jobs."""
        jobs = self.dao.list_all()

        # Apply filtering and pagination
        filtered_jobs = jobs

        # Apply 'after' filtering if specified
        if after:
            # Find the index of the 'after' job and take jobs after it
            after_index = -1
            for i, job in enumerate(jobs):
                if job.id == after:
                    after_index = i
                    break
            if after_index >= 0:
                filtered_jobs = jobs[after_index + 1 :]

        # Apply limit if specified
        if limit:
            try:
                limit_int = int(limit)
                filtered_jobs = filtered_jobs[:limit_int]
            except ValueError:
                # If limit is not a valid integer, ignore it
                pass

        # Determine if there are more jobs beyond the current page
        has_more = False
        if limit:
            try:
                limit_int = int(limit)
                # Check if there are more jobs available
                remaining_jobs = len(jobs) - len(filtered_jobs)
                if after:
                    # If 'after' was used, we need to account for jobs before the 'after' job
                    after_index = -1
                    for i, job in enumerate(jobs):
                        if job.id == after:
                            after_index = i
                            break
                    if after_index >= 0:
                        remaining_jobs = len(jobs) - (
                            after_index + 1 + len(filtered_jobs)
                        )
                has_more = remaining_jobs > 0
            except ValueError:
                pass

        return {
            "object": "list",
            "data": [job.model_dump() for job in filtered_jobs],
            "has_more": has_more,
        }

    def retrieve_fine_tuning_job(self, job_id: str) -> FineTuningJob | None:
        """Retrieve a fine-tuning job by ID."""
        return self.dao.get_by_id(job_id)

    def cancel_fine_tuning_job(self, job_id: str) -> FineTuningJob | None:
        """Cancel a fine-tuning job."""
        job = self.dao.get_by_id(job_id)
        if job:
            job.status = "cancelled"
            job.finished_at = int(time.time())
            self.dao.update(job_id, job)
        return job

    def list_fine_tuning_job_checkpoints(
        self, job_id: str, after: str = None, limit: str = None
    ) -> dict[str, Any] | None:
        """List checkpoints for a fine-tuning job."""
        # Check if the job exists first
        job = self.dao.get_by_id(job_id)
        if job is None:
            return None

        # For now, return empty list with proper pagination structure
        checkpoints = []

        # Apply limit if specified
        if limit:
            try:
                limit_int = int(limit)
                checkpoints = checkpoints[:limit_int]
            except ValueError:
                pass

        return {
            "object": "list",
            "data": checkpoints,
            "has_more": False,
        }

    def list_fine_tuning_events(
        self, job_id: str, limit: str = None, after: str = None
    ) -> dict[str, Any] | None:
        """List events for a fine-tuning job."""
        # Check if the job exists first
        job = self.dao.get_by_id(job_id)
        if job is None:
            return None

        # For now, return empty list with proper pagination structure
        events = []

        # Apply limit if specified
        if limit:
            try:
                limit_int = int(limit)
                events = events[:limit_int]
            except ValueError:
                pass

        return {
            "object": "list",
            "data": events,
            "has_more": False,
        }

    def pause_fine_tuning_job(self) -> dict[str, Any]:
        """Pause a fine-tuning job."""
        return {"status": "not_implemented"}

    def resume_fine_tuning_job(self) -> dict[str, Any]:
        """Resume a fine-tuning job."""
        return {"status": "not_implemented"}

    # def _parse_jsonl_file(self, file_data: str, split_name: str = "train") -> dict[str, Any]:
    #     """Parse JSONL file data into conversations format.

    #     Args:
    #         file_data: The JSONL file content as a string
    #         split_name: The name to use for the split (default: "train")
    #     """
    #     from datasets import load_dataset
    #     import tempfile
    #     import os

    #     # Create a temporary file with the JSONL data
    #     with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
    #         f.write(file_data)
    #         temp_file_path = f.name

    #     try:
    #         # Load the dataset using Hugging Face datasets
    #         dataset = load_dataset('json', data_files=temp_file_path)

    #         # Print all available information about the dataset
    #         print("=== DATASET INFORMATION ===")
    #         print(f"Dataset type: {type(dataset)}")
    #         print(f"Dataset keys: {list(dataset.keys())}")

    #         # Print information for each split
    #         for split_key, split_data in dataset.items():
    #             print(f"\n=== SPLIT: {split_key} ===")
    #             print(f"Split type: {type(split_data)}")
    #             print(f"Number of examples: {len(split_data)}")
    #             print(f"Features: {split_data.features}")
    #             print(f"Column names: {split_data.column_names}")

    #             # Print first few examples
    #             print(f"\nFirst 3 examples:")
    #             for i in range(min(3, len(split_data))):
    #                 print(f"Example {i}: {split_data[i]}")

    #             # Print dataset info
    #             print(f"\nDataset info:")
    #             print(f"  - Dataset size: {split_data.dataset_size}")
    #             print(f"  - Num rows: {split_data.num_rows}")
    #             print(f"  - Split: {split_data.split}")

    #             # Print features in detail
    #             print(f"\nDetailed features:")
    #             for feature_name, feature_type in split_data.features.items():
    #                 print(f"  - {feature_name}: {feature_type}")

    #         # Convert the dataset to the expected conversations format
    #         conversations = {}

    #         # Get the first split (datasets library creates a default split)
    #         # The actual split name from the dataset doesn't matter, we use our specified name
    #         split_data = list(dataset.values())[0]

    #         # Extract all messages and tools from the dataset
    #         all_messages = []
    #         all_tools = []

    #         for example in split_data:
    #             # Add messages from this example
    #             all_messages.extend(example['messages'])

    #             # Add tools from this example (they should be the same for all examples)
    #             if example['tools'] and not all_tools:
    #                 all_tools = example['tools']

    #         # Create the conversations structure with our specified split name
    #         if all_messages:
    #             conversations[split_name] = {
    #                 "messages": all_messages,
    #                 "tools": all_tools,
    #             }

    #         print(f"\n=== CONVERSATIONS FORMAT ===")
    #         print(f"Number of messages: {len(all_messages)}")
    #         print(f"Number of tools: {len(all_tools)}")
    #         print(f"Conversations keys: {list(conversations.keys())}")
    #         print(f"Using split name: {split_name}")

    #         # Return the conversations
    #         return conversations

    #     finally:
    #         # Clean up temporary file
    #         os.unlink(temp_file_path)


# Global service instance
_fine_tuning_service = None
_lock = None


def get_fine_tuning_service() -> FineTuningService:
    """Get the global fine-tuning service instance."""
    global _fine_tuning_service, _lock
    if _fine_tuning_service is None:
        import threading

        if _lock is None:
            _lock = threading.Lock()
        with _lock:
            if _fine_tuning_service is None:
                _fine_tuning_service = FineTuningService()
    return _fine_tuning_service
