# ruff: noqa: S101

import pytest

from constants import EXAMPLE_CONVERSATIONS, FINE_TUNED_EXAMPLE_CONVERSATIONS
from model_utils import (
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

    @pytest.mark.parametrize("conversation_idx", range(len(EXAMPLE_CONVERSATIONS)))
    @pytest.mark.slow
    def test_example_conversations_with_model_inference(
        self, processor, conversation_idx
    ):
        """Test example conversations with actual model inference (requires GPU)."""
        try:
            model = get_model()
        except Exception as e:
            pytest.skip(f"Model loading failed (GPU required): {e}")

        conversation_dict = EXAMPLE_CONVERSATIONS[conversation_idx]

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
        "conversation_idx", range(len(FINE_TUNED_EXAMPLE_CONVERSATIONS))
    )
    @pytest.mark.slow
    def test_example_conversations_with_model_training(  # noqa: C901
        self, processor, conversation_idx
    ):
        """Test example conversations with actual model training using Trainer (single epoch, requires GPU)."""
        try:
            # Load model with QLoRA (4-bit quantized LoRA) for parameter-efficient training
            model = get_model(with_peft=True)
        except Exception as e:
            pytest.skip(f"Model loading failed (GPU required): {e}")

        print(
            f"\n🎓 RUNNING TRAINER-BASED TRAINING FOR CONVERSATION {conversation_idx + 1}..."
        )

        conversation_dict = FINE_TUNED_EXAMPLE_CONVERSATIONS[conversation_idx]

        print(f"\n🤖 RUNNING TRAINING FOR CONVERSATION {conversation_idx + 1}...")

        expected = conversation_dict["expected"]
        messages = conversation_dict["messages"]
        tools = conversation_dict["tools"]

        ### PREPARE INPUTS
        print("Preparing inputs...")

        print("messages:")
        print(messages)

        print("tools:")
        print(tools)

        print("expected:")
        print(expected)

        # raise ValueError("stop here")

        # Create a simple dataset class for training that matches the working example format
        # class SimpleDataset:
        #     def __init__(self):
        #         # Use the exact same data format as the working example
        #         self.data = [
        #             {
        #                 "text prompt": "A bee on a flower",
        #                 "video link": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p000304.mp4",
        #             }
        #         ]

        #     def __len__(self):
        #         return 1

        #     def __getitem__(self, idx):
        #         return self.data[idx]

        # train_dataset = SimpleDataset()

        # Define data collator function exactly like the working example
        # def preprocess_video_caption_example(example, instruction="Caption the video."):
        #     prompt = example["text prompt"]
        #     user_content = [{"type": "text", "text": instruction}]
        #     # user_content.append({"type": "video", "path": example["video link"]})
        #     user_content.append({"type": "video", "url": example["video link"]})
        #     messages = [
        #         {"role": "user", "content": user_content},
        #         {
        #             "role": "assistant",
        #             "content": [{"type": "text", "text": f"{prompt}"}],
        #         },
        #     ]
        #     # Return a new dict with messages and keep other fields if needed
        #     # new_example = dict(example)
        #     new_example = {}
        #     new_example["messages"] = messages
        #     return new_example

        # Use prepare_model_inputs with train=True to get the processed dataset
        processed_dataset, processed_messages, _ = prepare_model_inputs(
            messages=messages,
            processor=processor,
            tools=tools,
            train=True,
        )

        print("processed_dataset:")
        print(processed_dataset)

        print("type(processed_dataset):")
        print(type(processed_dataset))

        # raise ValueError("stop here")

        # Get collate function from process_model_inputs
        collate_fn = process_model_inputs(
            processed_dataset, model, processor, train=True
        )

        # Use process_model_outputs with train=True to handle the training workflow
        process_model_outputs(
            processed_dataset,
            collate_fn,
            model,
            train=processor,
            conversation_idx=conversation_idx,
        )

        # ### PREPARE INPUTS
        # print("Preparing inputs...")

        # model_inputs, inference_messages, inference_prompt = prepare_model_inputs(
        #     messages=messages,
        #     processor=processor,
        #     tools=tools,
        # )

        # print("Testing inputs...")
        # assert inference_messages == expected["messages"]
        # assert inference_prompt == expected["prompt"]

        # ### PROCESS INPUTS
        # print("Processing inputs...")

        # model_outputs = process_model_inputs(model_inputs, model, processor)

        # ### PROCESS OUTPUTS
        # print("Processing outputs...")

        # response = process_model_outputs(model_inputs, model_outputs, processor)

        # print("✅ Inference completed!")
        # print(f"🤖 Model response: {response}")

        # assert response == expected["response"]
