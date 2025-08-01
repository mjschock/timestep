# ruff: noqa: S101

import json
import tempfile

import pytest

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

        model_inputs, inference_messages, inference_prompt = prepare_model_inputs(
            messages=messages,
            processor=processor,
            tools=tools,
        )

        print("Testing inputs...")
        assert inference_messages == expected["messages"]
        assert inference_prompt == expected["prompt"]

        ### PROCESS INPUTS
        print("Processing inputs...")

        model_outputs = process_model_inputs(model_inputs, model, processor)

        ### PROCESS OUTPUTS
        print("Processing outputs...")

        response = process_model_outputs(model_inputs, model_outputs, processor)

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

        processed_dataset, processed_messages, _ = prepare_model_inputs(
            messages=messages,
            processor=processor,
            tools=tools,
            train=True,
        )

        # TODO: Re-enable input validation for training
        # print("Testing inputs...")
        # assert processed_messages == expected["messages"]
        # assert processed_dataset == expected["prompt"]

        ### PROCESS INPUTS
        print("Processing inputs...")

        collate_fn = process_model_inputs(
            processed_dataset, model, processor, train=True
        )

        ### PROCESS OUTPUTS
        print("Processing outputs...")

        training_result = process_model_outputs(
            processed_dataset,
            collate_fn,
            model,
            train=processor,
            conversation_idx=conversation_idx,
        )

        # Store the model path for use in inference test
        model_path = training_result["model_path"]
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

        model_inputs, inference_messages, inference_prompt = prepare_model_inputs(
            messages=messages,
            processor=processor,
            tools=tools,
        )

        print("Testing inputs...")
        assert inference_messages == expected["messages"]
        assert inference_prompt == expected["prompt"]

        ### PROCESS INPUTS
        print("Processing inputs...")

        model_outputs = process_model_inputs(model_inputs, model, processor)

        ### PROCESS OUTPUTS
        print("Processing outputs...")

        response = process_model_outputs(model_inputs, model_outputs, processor)

        print("✅ Fine-tuned model inference completed!")
        print(f"🤖 Fine-tuned model response: {response}")

        assert response == expected["response"]
