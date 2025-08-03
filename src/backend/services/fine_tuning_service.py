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
            n_epochs=hyperparameters.get("n_epochs", 3)
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

            # Process training data
            model_inputs = prepare_model_inputs(
                dataset=dataset,
                model=model,
                processor=processor,
            )

            # Get collate function and run training
            model_outputs = process_model_inputs(
                data_collator=model_inputs["data_collator"],
                model=model,
                processor=processor,
                train_dataset=model_inputs["train_dataset"],
            )

            # Run training
            _ = process_model_outputs(
                model_outputs=model_outputs,
                processor=processor,
            )

            self.logger.info("Fine-tuning completed successfully")

            # Update job status to "succeeded"
            if job:
                job.status = "succeeded"
                job.finished_at = int(time.time())
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
        return {
            "object": "list",
            "data": [job.model_dump() for job in jobs],
            "has_more": False,
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
    ) -> dict[str, Any]:
        """List checkpoints for a fine-tuning job."""
        return {"status": "not_implemented"}

    def list_fine_tuning_events(
        self, job_id: str, limit: str = None, after: str = None
    ) -> dict[str, Any] | None:
        """List events for a fine-tuning job."""
        return {"status": "not_implemented"}

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
