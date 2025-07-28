#!/usr/bin/env python3
"""Test script for VLM-based image generation"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend', 'src'))

from backend.services.vlm_image_service import VLMImageService

def test_vlm_image_generation():
    """Test VLM-based image generation"""
    print("Testing VLM-based image generation...")
    
    try:
        # Initialize the service
        service = VLMImageService()
        
        # Test prompts
        test_prompts = [
            "Generate a handwritten digit 7",
            "Create a beautiful landscape with mountains",
            "Generate an abstract art piece",
            "Create a simple geometric pattern"
        ]
        
        for i, prompt in enumerate(test_prompts):
            print(f"\nTesting prompt {i+1}: {prompt}")
            
            # Generate image
            img_array, img = service.generate_image(prompt, width=256, height=256)
            
            # Save the image
            filename = f"test_image_{i+1}.png"
            img.save(filename)
            print(f"✓ Generated and saved: {filename}")
        
        print("\n✓ All tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_vlm_image_generation()