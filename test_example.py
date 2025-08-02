#!/usr/bin/env python3
"""
Test script for Timestep-OAI-Compatible-App
This demonstrates how to use the unified API with different providers.
"""

import json
import requests
from typing import Dict, Any

# Base URL for the application
BASE_URL = "http://localhost:8000"

def test_root_endpoint():
    """Test the root endpoint"""
    print("🔍 Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_health_endpoint():
    """Test the health endpoint"""
    print("🔍 Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_providers_endpoint():
    """Test the providers endpoint"""
    print("🔍 Testing providers endpoint...")
    response = requests.get(f"{BASE_URL}/providers")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_local_models():
    """Test local models endpoint"""
    print("🔍 Testing local models...")
    response = requests.get(f"{BASE_URL}/local/v1/models")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_local_chat():
    """Test local chat completion"""
    print("🔍 Testing local chat completion...")
    payload = {
        "model": "SmolVLM2-1.7B-Instruct",
        "messages": [
            {"role": "user", "content": "Hello, how are you?"}
        ],
        "max_tokens": 100
    }
    response = requests.post(
        f"{BASE_URL}/local/v1/chat/completions",
        json=payload
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_external_provider_proxy():
    """Test external provider proxy (will fail without real API key)"""
    print("🔍 Testing external provider proxy...")
    headers = {"Authorization": "Bearer sk-test-key"}
    response = requests.get(f"{BASE_URL}/openai/v1/models", headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    print()

def test_file_upload():
    """Test file upload endpoint"""
    print("🔍 Testing file upload...")
    files = {"file": ("test.txt", "This is a test file", "text/plain")}
    data = {"purpose": "fine-tune"}
    response = requests.post(f"{BASE_URL}/local/v1/files", files=files, data=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_fine_tuning():
    """Test fine-tuning job creation"""
    print("🔍 Testing fine-tuning job creation...")
    data = {
        "model": "SmolVLM2-1.7B-Instruct",
        "training_file": "file-abc123",
        "suffix": "test-finetune"
    }
    response = requests.post(f"{BASE_URL}/local/v1/fine_tuning/jobs", data=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def main():
    """Run all tests"""
    print("🚀 Testing Timestep-OAI-Compatible-App")
    print("=" * 50)
    
    try:
        test_root_endpoint()
        test_health_endpoint()
        test_providers_endpoint()
        test_local_models()
        test_local_chat()
        test_file_upload()
        test_fine_tuning()
        test_external_provider_proxy()
        
        print("✅ All tests completed!")
        print("\n📝 Usage Examples:")
        print("1. Start the server: python main.py")
        print("2. Use with OpenAI client:")
        print("   import openai")
        print("   client = openai.OpenAI(base_url='http://localhost:8000/local/v1')")
        print("   response = client.chat.completions.create(...)")
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure to run 'python main.py' first.")
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    main()