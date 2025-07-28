import torch
import numpy as np
from PIL import Image
from .text_image_converter import ImageTextConverter
from .text_image_trainer import get_trained_model

def generate_image(prompt, model_path='./image-text-model'):
    """Generate image from text prompt"""
    # Load trained model
    model, tokenizer = get_trained_model(model_path)
    
    if model is None or tokenizer is None:
        print("No trained model available. Please train the model first.")
        return None
    
    # Format prompt
    input_text = f"Prompt: {prompt} Output: Size:"
    
    # Generate
    inputs = tokenizer.encode(input_text, return_tensors='pt')
    
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=1000,  # Adjust based on image size
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    # Decode generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract image text (after "Output: ")
    try:
        image_text = generated_text.split("Output: ")[1]
        
        # Convert text to image
        converter = ImageTextConverter()
        img_array = converter.text_to_image(image_text)
        
        # Convert to PIL Image
        img = Image.fromarray(img_array)
        
        print(f"✓ Generated image from prompt: {prompt}")
        return img_array, img
        
    except Exception as e:
        print(f"Generation failed: {e}")
        return None, None

def generate_image_with_fallback(prompt, model_path='./image-text-model'):
    """Generate image with fallback to random if model fails"""
    result = generate_image(prompt, model_path)
    
    if result[0] is None:
        # Fallback: generate random 28x28 image (MNIST size)
        print("Using fallback: generating random image")
        img_array = np.random.randint(0, 256, (28, 28, 3), dtype=np.uint8)
        img = Image.fromarray(img_array)
        return img_array, img
    
    return result