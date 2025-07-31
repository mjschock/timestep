# ruff: noqa: S101

import os

import pytest
import torch
from torch.nn.utils.rnn import pad_sequence
from transformers import Trainer, TrainingArguments

from constants import EXAMPLE_CONVERSATIONS, FINE_TUNED_EXAMPLE_CONVERSATIONS
from model_utils import (
    MODEL_PATH,
    get_model,
    get_processor,
    prepare_model_inputs,
    process_model_inputs,
    process_model_outputs,
)


class TestMultimodalMessageProcessor:
    """
    Test suite for multimodal message processing functionality.

    Tests cover text-only and multimodal conversations, training example preparation,
    inference processing, validation functions, and edge cases for robust functionality.
    Includes comprehensive testing of tool call conversion, message building, and
    training example validation.
    """

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

        # Preprocess the dataset with the desired instruction
        # instruction = "Caption the video."
        # processed_dataset = [
        #     preprocess_video_caption_example(train_dataset[0], instruction)
        # ]
        processed_dataset = [
            {
                "messages": messages,
            }
        ]

        print("processed_dataset:")
        print(processed_dataset)

        print("type(processed_dataset):")
        print(type(processed_dataset))

        # raise ValueError("stop here")

        image_token_id = processor.tokenizer.additional_special_tokens_ids[
            processor.tokenizer.additional_special_tokens.index("<image>")
        ]

        def collate_fn(examples):
            instances = []
            for example in examples:
                messages = example["messages"]
                instance = (
                    processor.apply_chat_template(
                        messages,
                        add_generation_prompt=False,
                        tokenize=True,
                        return_dict=True,
                        return_tensors="pt",
                    )
                    .to("cuda")
                    .to(model.dtype)
                )
                instances.append(instance)

            input_ids = pad_sequence(
                [inst["input_ids"].squeeze(0) for inst in instances],
                batch_first=True,
                padding_value=processor.tokenizer.pad_token_id,
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

            labels[labels == image_token_id] = -100

            out = {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "labels": labels,
            }

            # Step 1: figure out maximum frames, height, width across the batch
            pvs = [
                inst["pixel_values"].squeeze(0)
                for inst in instances
                if "pixel_values" in inst
            ]
            if pvs:  # there is at least one non-None pixel_values
                max_frames = max(pv.shape[0] for pv in pvs)
                max_h = max(pv.shape[-2] for pv in pvs)
                max_w = max(pv.shape[-1] for pv in pvs)
            else:
                max_h = max_w = processor.video_size["longest_edge"]
                max_frames = 1

            padded_pixel_values_list = []
            for ex in instances:
                pv = ex.get("pixel_values", None).squeeze(0)

                if pv is None:
                    # text-only => fill pixel data + mask with zeros
                    shape_pv = (max_frames, 3, max_h, max_w)
                    padded_pv = torch.zeros(shape_pv, dtype=torch.float32)
                else:
                    f, c, h, w = pv.shape
                    # Prepare final storage
                    padded_pv = torch.zeros(
                        (max_frames, c, max_h, max_w), dtype=pv.dtype, device=pv.device
                    )
                    padded_pv[:f, :, :h, :w] = pv
                padded_pixel_values_list.append(padded_pv)

            out["pixel_values"] = torch.stack(padded_pixel_values_list, dim=0)
            return out

        # Print model info
        model.print_trainable_parameters()
        print(f"  Model dtype: {model.dtype}")

        # Create training arguments exactly like the working example
        training_args = TrainingArguments(
            num_train_epochs=1,
            per_device_train_batch_size=2,
            gradient_accumulation_steps=1,
            warmup_steps=50,
            learning_rate=1e-4,
            weight_decay=0.01,
            logging_steps=25,
            save_strategy="steps",
            save_steps=250,
            save_total_limit=1,
            optim="paged_adamw_8bit",  # appropriate optimizer for QLoRA
            bf16=True,
            # output_dir=f"./test-training-{conversation_idx}",
            output_dir=f"data/models/{MODEL_PATH.split('/')[-1]}-{conversation_idx}",
            hub_model_id=f"{os.getenv('HF_USERNAME', os.getenv('USER'))}/{MODEL_PATH.split('/')[-1]}-{conversation_idx}",
            remove_unused_columns=False,
            report_to="tensorboard",
            label_names=["labels"],
            dataloader_pin_memory=False,
            gradient_checkpointing=True,
            gradient_checkpointing_kwargs={"use_reentrant": False},
        )

        # Create trainer
        trainer = Trainer(
            model=model,
            args=training_args,
            data_collator=collate_fn,
            train_dataset=processed_dataset,
        )

        # Record initial loss for comparison
        model.eval()
        with torch.no_grad():
            # Get a sample batch to compute initial loss
            sample_batch = collate_fn([processed_dataset[0]])
            device = next(model.parameters()).device
            sample_batch = {
                k: v.to(device) if hasattr(v, "to") else v
                for k, v in sample_batch.items()
            }

            initial_outputs = model(**sample_batch)
            initial_loss = initial_outputs.loss.item()

        print(f"  Initial loss: {initial_loss:.4f}")

        # Train for one epoch
        model.train()
        train_result = trainer.train()

        print("  Training completed!")
        print(f"  Final loss: {train_result.training_loss:.4f}")
        print(f"  Loss improvement: {initial_loss - train_result.training_loss:.4f}")

        # Verify that training actually improved the model
        assert train_result.training_loss < initial_loss, (
            "Training should improve the model"
        )
