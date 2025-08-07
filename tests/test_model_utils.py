# ruff: noqa: S101

import json
import tempfile

import pytest
from datasets import Dataset, DatasetDict

from backend._shared.config.constants import (
    BASE_MODEL_INFERENCE_CONVERSATIONS,
    BASE_MODEL_TRAINING_CONVERSATIONS,
    FINE_TUNED_MODEL_INFERENCE_CONVERSATIONS,
)
from backend._shared.utils.model_utils import (
    get_model,
    get_processor,
    prepare_model_inputs,
    process_model_inputs,
    process_model_outputs,
)


class TestMultimodalMessageProcessor:
    @pytest.fixture(scope="class")
    def processor(self):
        """Load the SmolVLM2 processor for testing."""
        return get_processor()

    @pytest.fixture(scope="class")
    def model_paths_file(self):
        """Create a temporary file to store model paths between tests."""
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
            json.dump({}, f)
            return f.name

    def _get_model_path(self, conversation_idx, model_paths_file):
        """Get the model path for a conversation from the shared file."""
        try:
            with open(model_paths_file) as f:
                paths = json.load(f)
            return paths.get(str(conversation_idx))
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def _set_model_path(self, conversation_idx, model_path, model_paths_file):
        """Set the model path for a conversation in the shared file."""
        try:
            with open(model_paths_file) as f:
                paths = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            paths = {}

        paths[str(conversation_idx)] = model_path

        with open(model_paths_file, "w") as f:
            json.dump(paths, f)

    @pytest.mark.parametrize(
        "conversation_idx", range(len(BASE_MODEL_INFERENCE_CONVERSATIONS))
    )
    @pytest.mark.slow
    def test_base_model_inference(self, processor, conversation_idx):
        """Test example conversations with actual model inference (requires GPU)."""
        try:
            model = get_model()
        except Exception as e:
            pytest.skip(f"Model loading failed (GPU required): {e}")

        conversation_dict = BASE_MODEL_INFERENCE_CONVERSATIONS[conversation_idx]

        print(f"\n🤖 RUNNING INFERENCE FOR CONVERSATION {conversation_idx + 1}...")

        expected = conversation_dict["expected"]
        messages = conversation_dict["messages"]
        tools = conversation_dict["tools"]

        ### PREPARE INPUTS
        print("Preparing inputs...")

        # Create DatasetDict with Dataset for inference
        test_data = [
            {
                "messages": messages,
                "tools": tools,
                "parallel_tool_calls": None,  # Add this field as mentioned in comment
            }
        ]

        dataset = DatasetDict({"test": Dataset.from_list(test_data)})

        # Verify the dataset structure matches expected format
        assert "test" in dataset
        assert len(dataset["test"]) == 1
        test_example = dataset["test"][0]
        assert "messages" in test_example
        assert "tools" in test_example
        assert "parallel_tool_calls" in test_example
        print(
            f"✅ Dataset structure verified: {list(dataset.keys())} with features {dataset['test'].features}"
        )

        model_inputs = prepare_model_inputs(
            dataset=dataset,
            model=model,
            processor=processor,
        )

        print("Testing inputs...")
        # TODO: Re-enable testing expected messages/prompt for inference data
        # assert inference_messages == expected["messages"]
        # assert inference_prompt == expected["prompt"]

        ### PROCESS INPUTS
        print("Processing inputs...")

        model_outputs = process_model_inputs(
            data_collator=model_inputs["data_collator"],
            eval_dataset=model_inputs["eval_dataset"],
            model=model,
            processor=processor,
            test_dataset=model_inputs["test_dataset"],
            train_dataset=model_inputs["train_dataset"],
        )

        ### PROCESS OUTPUTS
        print("Processing outputs...")

        results = process_model_outputs(
            model_outputs=model_outputs,
            processor=processor,
            tools=tools,
            tool_choice="required" if tools else None,
        )

        response = results["response"]

        print("✅ Inference completed!")
        print(f"🤖 Model response: {response}")

        assert response == expected["response"]

    @pytest.mark.parametrize(
        "conversation_idx", range(len(BASE_MODEL_TRAINING_CONVERSATIONS))
    )
    @pytest.mark.slow
    def test_base_model_training(  # noqa: C901
        self, processor, conversation_idx, model_paths_file
    ):
        """Test example conversations with actual model training using Trainer (single epoch, requires GPU)."""
        try:
            # Load model with QLoRA (4-bit quantized LoRA) for parameter-efficient training
            model = get_model(train=True)
        except Exception as e:
            pytest.skip(f"Model loading failed (GPU required): {e}")

        conversation_dict = BASE_MODEL_TRAINING_CONVERSATIONS[conversation_idx]

        print(f"\n🤖 RUNNING TRAINING FOR CONVERSATION {conversation_idx + 1}...")

        # TODO: Re-enable testing expected messages/prompt for training data
        # expected = conversation_dict["expected"]
        messages = conversation_dict["messages"]
        tools = conversation_dict["tools"]

        ### PREPARE INPUTS
        print("Preparing inputs...")

        # Create DatasetDict with Dataset for training
        train_data = [
            {
                "messages": messages,
                "tools": tools,
                "parallel_tool_calls": None,  # Add this field as mentioned in comment
            }
        ]

        dataset = DatasetDict({"train": Dataset.from_list(train_data)})

        # Verify the dataset structure matches expected format
        assert "train" in dataset
        assert len(dataset["train"]) == 1
        train_example = dataset["train"][0]
        assert "messages" in train_example
        assert "tools" in train_example
        assert "parallel_tool_calls" in train_example
        print(
            f"✅ Dataset structure verified: {list(dataset.keys())} with features {dataset['train'].features}"
        )

        model_inputs = prepare_model_inputs(
            dataset=dataset,
            model=model,
            processor=processor,
        )

        # TODO: Re-enable input validation for training
        # print("Testing inputs...")
        # assert processed_messages == expected["messages"]
        # assert processed_dataset == expected["prompt"]

        ### PROCESS INPUTS
        print("Processing inputs...")

        model_outputs = process_model_inputs(
            data_collator=model_inputs["data_collator"],
            eval_dataset=model_inputs["eval_dataset"],
            model=model,
            processor=processor,
            test_dataset=model_inputs["test_dataset"],
            train_dataset=model_inputs["train_dataset"],
        )

        ### PROCESS OUTPUTS
        print("Processing outputs...")

        output = process_model_outputs(model_outputs=model_outputs, processor=processor)

        # Store the model path for use in inference test
        model_path = output["model_path"]
        checkpoint_path = f"{model_path}/checkpoint-1"
        print(f"✅ Training completed! Model saved to: {checkpoint_path}")

        # Store the model path in the shared file for use in inference test
        self._set_model_path(conversation_idx, checkpoint_path, model_paths_file)

    @pytest.mark.parametrize(
        "conversation_idx", range(len(FINE_TUNED_MODEL_INFERENCE_CONVERSATIONS))
    )
    @pytest.mark.slow
    def test_fine_tuned_model_inference(
        self, processor, conversation_idx, model_paths_file
    ):
        """Test fine-tuned model inference using the same conversations as training (requires GPU)."""
        try:
            # Get the model path from the shared file
            model_path = self._get_model_path(conversation_idx, model_paths_file)

            if model_path is None:
                pytest.skip(
                    f"No fine-tuned model path found for conversation {conversation_idx}. Run training test first."
                )

            # Load the fine-tuned model for inference
            model = get_model(pretrained_model_name_or_path=model_path)
        except Exception as e:
            pytest.skip(f"Fine-tuned model loading failed (GPU required): {e}")

        conversation_dict = FINE_TUNED_MODEL_INFERENCE_CONVERSATIONS[conversation_idx]

        print(
            f"\n🎯 RUNNING FINE-TUNED MODEL INFERENCE FOR CONVERSATION {conversation_idx + 1}..."
        )

        expected = conversation_dict["expected"]
        messages = conversation_dict["messages"]
        tools = conversation_dict["tools"]

        ### PREPARE INPUTS
        print("Preparing inputs...")

        # Create DatasetDict with Dataset for fine-tuned inference
        test_data = [
            {
                "messages": messages,
                "tools": tools,
                "parallel_tool_calls": None,  # Add this field as mentioned in comment
            }
        ]

        dataset = DatasetDict({"test": Dataset.from_list(test_data)})

        # Verify the dataset structure matches expected format
        assert "test" in dataset
        assert len(dataset["test"]) == 1
        test_example = dataset["test"][0]
        assert "messages" in test_example
        assert "tools" in test_example
        assert "parallel_tool_calls" in test_example
        print(
            f"✅ Dataset structure verified: {list(dataset.keys())} with features {dataset['test'].features}"
        )

        model_inputs = prepare_model_inputs(
            dataset=dataset,
            model=model,
            processor=processor,
        )

        print("Testing inputs...")
        # TODO: Re-enable testing expected messages/prompt for fine-tuned inference data
        # assert inference_messages == expected["messages"]
        # assert inference_prompt == expected["prompt"]

        ### PROCESS INPUTS
        print("Processing inputs...")

        model_outputs = process_model_inputs(
            data_collator=model_inputs["data_collator"],
            eval_dataset=model_inputs["eval_dataset"],
            model=model,
            processor=processor,
            test_dataset=model_inputs["test_dataset"],
            train_dataset=model_inputs["train_dataset"],
        )

        ### PROCESS OUTPUTS
        print("Processing outputs...")

        output = process_model_outputs(model_outputs=model_outputs, processor=processor)
        response = output["response"]

        print("✅ Fine-tuned model inference completed!")
        print(f"🤖 Fine-tuned model response: {response}")

        assert response == expected["response"]
