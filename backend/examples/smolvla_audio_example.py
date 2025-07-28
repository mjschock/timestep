#!/usr/bin/env python3
"""
Example script demonstrating SmolVLA audio processing capabilities.

This script shows how to use SmolVLA to process audio inputs along with text and images.
SmolVLA extends SmolVLM2 with audio processing capabilities.
"""

import torch
from transformers import AutoModelForImageTextToText, AutoProcessor

def main():
    """Demonstrate SmolVLA audio processing."""
    
    # SmolVLA model name
    model_name = "HuggingFaceTB/SmolVLA-256M-Video-Instruct"
    
    print(f"🎵 Loading SmolVLA model: {model_name}")
    
    try:
        # Load model and processor
        processor = AutoProcessor.from_pretrained(model_name)
        model = AutoModelForImageTextToText.from_pretrained(
            model_name, torch_dtype=torch.bfloat16
        ).to("cuda")
        
        print("✅ Model loaded successfully!")
        
        # Example 1: Audio-only input
        print("\n🎵 Example 1: Audio-only processing")
        audio_messages = [
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
        
        print("Processing audio input...")
        inputs = processor.apply_chat_template(
            audio_messages,
            add_generation_prompt=True,
            tokenize=False,
            return_dict=False,
        )
        print(f"✅ Audio processing successful")
        
        # Example 2: Mixed content (text + image + audio)
        print("\n🎵 Example 2: Mixed content processing")
        mixed_messages = [
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
        
        print("Processing mixed content input...")
        inputs = processor.apply_chat_template(
            mixed_messages,
            add_generation_prompt=True,
            tokenize=False,
            return_dict=False,
        )
        print(f"✅ Mixed content processing successful")
        
        # Example 3: Video + audio
        print("\n🎵 Example 3: Video + audio processing")
        video_audio_messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "video",
                        "path": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p110924.mp4",
                    },
                    {
                        "type": "audio",
                        "path": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/audio_sample.wav",
                    },
                    {"type": "text", "text": "Describe the video and audio content."},
                ],
            },
        ]
        
        print("Processing video + audio input...")
        inputs = processor.apply_chat_template(
            video_audio_messages,
            add_generation_prompt=True,
            tokenize=False,
            return_dict=False,
        )
        print(f"✅ Video + audio processing successful")
        
        print("\n🎉 All SmolVLA examples completed successfully!")
        print("\nSupported content types:")
        print("- text: {\"type\": \"text\", \"text\": \"...\"}")
        print("- image: {\"type\": \"image\", \"url\": \"...\"}")
        print("- audio: {\"type\": \"audio\", \"path\": \"...\"}")
        print("- video: {\"type\": \"video\", \"path\": \"...\"}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("This might be due to:")
        print("- Model not available")
        print("- CUDA not available")
        print("- Missing dependencies")


if __name__ == "__main__":
    main()