#!/usr/bin/env python3
"""Simple test for VLM-based image generation"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend', 'src'))

def test_simple_vlm_image():
    """Test VLM-based image generation without loading all models"""
    print("🧪 Testing simple VLM-based image generation...")
    
    try:
        # Import the VLM image service directly
        from backend.services.vlm_image_service import VLMImageService
        
        # Create a simple mock models service
        class MockModelsService:
            def get_model_instance(self, model_name):
                print(f"Mock: Loading model {model_name}")
                return None, None  # Return None for now to avoid loading heavy models
        
        # Initialize the service with mock
        service = VLMImageService(MockModelsService())
        
        # Test prompts
        test_prompts = [
            "Generate a handwritten digit 7",
            "Create a beautiful landscape with mountains",
            "Generate an abstract art piece"
        ]
        
        for i, prompt in enumerate(test_prompts):
            print(f"\n🎨 Test {i+1}: '{prompt}'")
            
            # Generate image
            img_array, img = service.generate_image(prompt, width=128, height=128)
            
            if img_array is not None and img is not None:
                print(f"✅ Successfully generated image for prompt: '{prompt}'")
                print(f"   Image shape: {img_array.shape}")
                print(f"   Image mode: {img.mode}")
                print(f"   Image size: {img.size}")
                
                # Save the image
                filename = f"simple_test_image_{i+1}.png"
                img.save(filename)
                print(f"   Saved as: {filename}")
            else:
                print(f"❌ Failed to generate image for prompt: '{prompt}'")
        
        print("\n🎉 Simple VLM-based image generation test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_simple_vlm_image()
    if success:
        print("\n🎉 Simple test completed successfully!")
    else:
        print("\n❌ Simple test failed!")