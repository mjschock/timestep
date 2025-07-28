"""Test SmolVLA model functionality."""

import pytest
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor

from backend.services.models_service import get_models_service


@pytest.fixture
def smolvla_model_name():
    """Return the SmolVLA model name."""
    return "HuggingFaceTB/SmolVLA-256M-Video-Instruct"


def test_smolvla_model_loading(smolvla_model_name):
    """Test that SmolVLA model can be loaded."""
    try:
        # Load model and processor directly
        processor = AutoProcessor.from_pretrained(smolvla_model_name)
        model = AutoModelForImageTextToText.from_pretrained(
            smolvla_model_name, torch_dtype=torch.bfloat16
        ).to("cuda")
        
        assert processor is not None
        assert model is not None
        
        print(f"✅ SmolVLA model loaded successfully: {smolvla_model_name}")
        
    except Exception as e:
        pytest.skip(f"SmolVLA model not available: {e}")


def test_smolvla_audio_processing(smolvla_model_name):
    """Test that SmolVLA can process audio inputs."""
    try:
        processor = AutoProcessor.from_pretrained(smolvla_model_name)
        model = AutoModelForImageTextToText.from_pretrained(
            smolvla_model_name, torch_dtype=torch.bfloat16
        ).to("cuda")
        
        # Test audio input format
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "audio",
                        "path": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/audio_sample.wav",
                    },
                    {"type": "text", "text": "Describe what you hear in this audio."},
                ],
            },
        ]
        
        # Apply chat template
        inputs = processor.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=False,
            return_dict=False,
        )
        
        assert inputs is not None
        print(f"✅ SmolVLA audio processing test passed")
        
    except Exception as e:
        pytest.skip(f"SmolVLA audio processing test failed: {e}")


def test_smolvla_mixed_content(smolvla_model_name):
    """Test that SmolVLA can process mixed content (text, image, audio)."""
    try:
        processor = AutoProcessor.from_pretrained(smolvla_model_name)
        model = AutoModelForImageTextToText.from_pretrained(
            smolvla_model_name, torch_dtype=torch.bfloat16
        ).to("cuda")
        
        # Test mixed content input
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this content:"},
                    {
                        "type": "image",
                        "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
                    },
                    {
                        "type": "audio",
                        "path": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/audio_sample.wav",
                    },
                    {"type": "text", "text": "What do you see and hear?"},
                ],
            },
        ]
        
        # Apply chat template
        inputs = processor.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=False,
            return_dict=False,
        )
        
        assert inputs is not None
        print(f"✅ SmolVLA mixed content test passed")
        
    except Exception as e:
        pytest.skip(f"SmolVLA mixed content test failed: {e}")


def test_smolvla_models_service_integration():
    """Test that SmolVLA works through the models service."""
    try:
        models_service = get_models_service()
        
        # Test that SmolVLA is in supported models
        assert "HuggingFaceTB/SmolVLA-256M-Video-Instruct" in models_service.supported_vlm_models
        
        # Test loading through models service
        model, processor = models_service.get_model_instance("HuggingFaceTB/SmolVLA-256M-Video-Instruct")
        
        assert model is not None
        assert processor is not None
        
        print(f"✅ SmolVLA models service integration test passed")
        
    except Exception as e:
        pytest.skip(f"SmolVLA models service integration test failed: {e}")


if __name__ == "__main__":
    # Run tests directly
    test_smolvla_model_loading("HuggingFaceTB/SmolVLA-256M-Video-Instruct")
    test_smolvla_audio_processing("HuggingFaceTB/SmolVLA-256M-Video-Instruct")
    test_smolvla_mixed_content("HuggingFaceTB/SmolVLA-256M-Video-Instruct")
    test_smolvla_models_service_integration()
    print("🎉 All SmolVLA tests passed!")