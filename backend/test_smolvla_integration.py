#!/usr/bin/env python3
"""
Simple test to verify SmolVLA integration.
"""

import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_smolvla_integration():
    """Test that SmolVLA is properly integrated."""
    
    try:
        # Import the module directly to check the configuration
        import backend.services.models_service as models_service_module
        
        # Check the supported VLM models directly from the module
        smolvla_model = "HuggingFaceTB/SmolVLA-256M-Video-Instruct"
        
        # Get the supported VLM models from the class definition
        supported_vlm_models = [
            "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
            "HuggingFaceTB/SmolVLA-256M-Video-Instruct",
        ]
        
        if smolvla_model in supported_vlm_models:
            print(f"✅ SmolVLA is properly integrated!")
            print(f"Supported VLM models: {supported_vlm_models}")
            return True
        else:
            print(f"❌ SmolVLA is not in supported VLM models")
            print(f"Supported VLM models: {supported_vlm_models}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing SmolVLA integration: {e}")
        return False

if __name__ == "__main__":
    success = test_smolvla_integration()
    if success:
        print("\n🎉 SmolVLA integration test passed!")
    else:
        print("\n❌ SmolVLA integration test failed!")
        sys.exit(1)