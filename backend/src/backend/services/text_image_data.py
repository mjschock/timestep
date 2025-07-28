import json
import numpy as np
from datasets import load_dataset
from .text_image_converter import ImageTextConverter

def create_training_data():
    """Generate training pairs from MNIST"""
    dataset = load_dataset("mnist", split="train[:1000]")  # Small subset
    converter = ImageTextConverter()
    
    training_data = []
    for i, sample in enumerate(dataset):
        # Convert PIL to numpy
        img_array = np.array(sample['image'])
        label = sample['label']
        
        # Convert to text
        text_repr = converter.image_to_text(img_array)
        
        # Create training pair
        training_data.append({
            "prompt": f"Generate a handwritten digit {label}",
            "completion": text_repr
        })
        
        if i % 100 == 0:
            print(f"Processed {i}/1000 images")
    
    # Save training data
    with open('training_data.json', 'w') as f:
        json.dump(training_data, f)
    
    print(f"✓ Created {len(training_data)} training pairs")
    return training_data

def load_training_data():
    """Load existing training data"""
    try:
        with open('training_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("No existing training data found. Creating new data...")
        return create_training_data()