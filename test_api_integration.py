#!/usr/bin/env python3
"""Test script for API integration with VLM-based image generation"""

import sys
import os
import json
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend', 'src'))

async def test_api_integration():
    """Test VLM-based image generation through the API"""
    print("🧪 Testing API integration with VLM-based image generation...")
    
    try:
        # Import the images service directly
        from backend.services.images_service import ImagesService
        from fastapi import Request
        from unittest.mock import Mock
        
        # Create a mock request
        mock_request = Mock()
        mock_request.json = Mock(return_value={
            "model": "vlm-image-generator",
            "prompt": "Generate a beautiful sunset landscape",
            "n": 1,
            "size": "512x512",
            "response_format": "b64_json"
        })
        
        # Create the service
        service = ImagesService()
        
        # Test the create_image method
        print("🎨 Testing image generation through API...")
        result = await service.create_image(mock_request)
        
        print("✅ API integration test successful!")
        print(f"   Result keys: {list(result.keys())}")
        print(f"   Data length: {len(result['data'])}")
        
        if result['data']:
            image_data = result['data'][0]
            print(f"   Image keys: {list(image_data.keys())}")
            if 'b64_json' in image_data:
                print(f"   Base64 image length: {len(image_data['b64_json'])}")
        
        return True
        
    except Exception as e:
        print(f"❌ API integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import asyncio
    success = asyncio.run(test_api_integration())
    if success:
        print("\n🎉 API integration test completed successfully!")
    else:
        print("\n❌ API integration test failed!")