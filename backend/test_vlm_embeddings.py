#!/usr/bin/env python3
"""
Test script for VLM-based embeddings.

This script demonstrates how to use the new VLM-based embedding service
that extracts latent representations from vision language models.
"""

import requests
import json
import base64
from PIL import Image
import io

# Configuration
BASE_URL = "http://localhost:8000/v1"
EMBEDDING_MODEL = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"

def test_text_embeddings():
    """Test text-only embeddings using VLM."""
    print("Testing text embeddings with VLM...")
    
    # Test data
    texts = [
        "A cat sitting on a windowsill",
        "A beautiful sunset over the ocean",
        "A person reading a book in a library"
    ]
    
    for i, text in enumerate(texts):
        payload = {
            "input": text,
            "model": EMBEDDING_MODEL,
            "embedding_type": "cls"  # Use CLS token embedding
        }
        
        try:
            response = requests.post(f"{BASE_URL}/embeddings", json=payload)
            if response.status_code == 200:
                result = response.json()
                embedding = result["data"][0]["embedding"]
                print(f"✅ Text {i+1}: Generated embedding of dimension {len(embedding)}")
                print(f"   Text: {text}")
                print(f"   First 5 values: {embedding[:5]}")
                print()
            else:
                print(f"❌ Text {i+1}: Failed with status {response.status_code}")
                print(f"   Error: {response.text}")
                print()
        except Exception as e:
            print(f"❌ Text {i+1}: Exception - {e}")
            print()

def test_multimodal_embeddings():
    """Test multimodal embeddings with text and image."""
    print("Testing multimodal embeddings with VLM...")
    
    # Create a simple test image (you can replace this with a real image)
    test_image = Image.new('RGB', (224, 224), color='red')
    
    # Convert image to base64
    buffer = io.BytesIO()
    test_image.save(buffer, format='PNG')
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    # Test multimodal embedding
    payload = {
        "text": "A red square image",
        "image": image_base64,
        "model": EMBEDDING_MODEL,
        "embedding_type": "cls"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/embeddings/multimodal", json=payload)
        if response.status_code == 200:
            result = response.json()
            embedding = result["data"][0]["embedding"]
            print(f"✅ Multimodal: Generated embedding of dimension {len(embedding)}")
            print(f"   Text: A red square image")
            print(f"   First 5 values: {embedding[:5]}")
            print()
        else:
            print(f"❌ Multimodal: Failed with status {response.status_code}")
            print(f"   Error: {response.text}")
            print()
    except Exception as e:
        print(f"❌ Multimodal: Exception - {e}")
        print()

def test_different_embedding_types():
    """Test different embedding extraction strategies."""
    print("Testing different embedding extraction types...")
    
    text = "A cat sitting on a windowsill"
    embedding_types = ["cls", "mean", "last_layer", "multi_layer"]
    
    for embedding_type in embedding_types:
        payload = {
            "input": text,
            "model": EMBEDDING_MODEL,
            "embedding_type": embedding_type
        }
        
        try:
            response = requests.post(f"{BASE_URL}/embeddings", json=payload)
            if response.status_code == 200:
                result = response.json()
                embedding = result["data"][0]["embedding"]
                print(f"✅ {embedding_type}: Generated embedding of dimension {len(embedding)}")
                print(f"   First 5 values: {embedding[:5]}")
                print()
            else:
                print(f"❌ {embedding_type}: Failed with status {response.status_code}")
                print(f"   Error: {response.text}")
                print()
        except Exception as e:
            print(f"❌ {embedding_type}: Exception - {e}")
            print()

def compare_with_traditional_embeddings():
    """Compare VLM embeddings with traditional sentence transformers."""
    print("Comparing VLM embeddings with traditional embeddings...")
    
    text = "A cat sitting on a windowsill"
    
    # Test VLM embedding
    vlm_payload = {
        "input": text,
        "model": EMBEDDING_MODEL,
        "embedding_type": "cls"
    }
    
    # Test traditional embedding
    traditional_payload = {
        "input": text,
        "model": "sentence-transformers/paraphrase-MiniLM-L3-v2"
    }
    
    try:
        # Get VLM embedding
        vlm_response = requests.post(f"{BASE_URL}/embeddings", json=vlm_payload)
        if vlm_response.status_code == 200:
            vlm_result = vlm_response.json()
            vlm_embedding = vlm_result["data"][0]["embedding"]
            print(f"✅ VLM embedding dimension: {len(vlm_embedding)}")
            print(f"   First 5 values: {vlm_embedding[:5]}")
        else:
            print(f"❌ VLM embedding failed: {vlm_response.status_code}")
            print(f"   Error: {vlm_response.text}")
        
        # Get traditional embedding
        traditional_response = requests.post(f"{BASE_URL}/embeddings", json=traditional_payload)
        if traditional_response.status_code == 200:
            traditional_result = traditional_response.json()
            traditional_embedding = traditional_result["data"][0]["embedding"]
            print(f"✅ Traditional embedding dimension: {len(traditional_embedding)}")
            print(f"   First 5 values: {traditional_embedding[:5]}")
        else:
            print(f"❌ Traditional embedding failed: {traditional_response.status_code}")
            print(f"   Error: {traditional_response.text}")
            
        print()
        
    except Exception as e:
        print(f"❌ Comparison failed: {e}")
        print()

if __name__ == "__main__":
    print("🚀 Testing VLM-based Embeddings")
    print("=" * 50)
    print()
    
    # Test text embeddings
    test_text_embeddings()
    
    # Test multimodal embeddings
    test_multimodal_embeddings()
    
    # Test different embedding types
    test_different_embedding_types()
    
    # Compare with traditional embeddings
    compare_with_traditional_embeddings()
    
    print("✅ Testing completed!")