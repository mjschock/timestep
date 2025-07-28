#!/usr/bin/env python3
"""Test script for VLM-based image generation"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend', 'src'))

def test_vlm_image_generation():
    """Test VLM-based image generation"""
    print("🧪 Testing VLM-based image generation...")
    
    try:
        # Import the VLM image service
        from backend.services.vlm_image_service import VLMImageService
        
        # Initialize the service
        service = VLMImageService()
        
        # Test prompts
        test_prompts = [
            "Generate a handwritten digit 7",
            "Create a beautiful landscape with mountains",
            "Generate an abstract art piece",
            "Create a simple geometric pattern",
            "Generate a photorealistic portrait"
        ]
        
        for i, prompt in enumerate(test_prompts):
            print(f"\n🎨 Test {i+1}: '{prompt}'")
            
            # Generate image
            img_array, img = service.generate_image(prompt, width=256, height=256)
            
            if img_array is not None and img is not None:
                print(f"✅ Successfully generated image for prompt: '{prompt}'")
                print(f"   Image shape: {img_array.shape}")
                print(f"   Image mode: {img.mode}")
                print(f"   Image size: {img.size}")
                
                # Save the image
                filename = f"test_image_{i+1}.png"
                img.save(filename)
                print(f"   Saved as: {filename}")
            else:
                print(f"❌ Failed to generate image for prompt: '{prompt}'")
        
        print("\n🎉 VLM-based image generation test completed!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_vlm_image_generation()