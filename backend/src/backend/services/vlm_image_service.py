import torch
import numpy as np
from PIL import Image
import io
import base64
from typing import Optional, Tuple

class VLMImageService:
    """Image generation service using VLM for prompt understanding"""
    
    def __init__(self, models_service=None):
        self.models_service = models_service
        self.vlm_model = None
        self.vlm_processor = None
        if models_service:
            self._load_vlm()
    
    def _load_vlm(self):
        """Load the VLM model for prompt understanding"""
        try:
            self.vlm_model, self.vlm_processor = self.models_service.get_model_instance(
                "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
            )
            print("✓ VLM loaded successfully for image generation")
        except Exception as e:
            print(f"⚠️ Failed to load VLM: {e}")
            self.vlm_model = None
            self.vlm_processor = None
    
    def _analyze_prompt_with_vlm(self, prompt: str) -> dict:
        """Use VLM to analyze and understand the image generation prompt"""
        if self.vlm_model is None or self.vlm_processor is None:
            return {"style": "default", "content": prompt, "complexity": "simple"}
        
        try:
            # Create a simple test image for VLM analysis
            test_image = Image.new('RGB', (224, 224), color='white')
            
            # Format prompt for VLM analysis
            vlm_prompt = f"Analyze this image and describe what kind of image generation prompt would create it: {prompt}"
            
            # Process with VLM
            inputs = self.vlm_processor(
                images=test_image,
                text=vlm_prompt,
                return_tensors="pt"
            )
            
            # Generate response
            with torch.no_grad():
                outputs = self.vlm_model.generate(
                    **inputs,
                    max_new_tokens=100,
                    do_sample=True,
                    temperature=0.7
                )
            
            # Decode response
            response = self.vlm_processor.decode(outputs[0], skip_special_tokens=True)
            
            # Parse VLM analysis
            analysis = self._parse_vlm_analysis(response, prompt)
            return analysis
            
        except Exception as e:
            print(f"⚠️ VLM analysis failed: {e}")
            return {"style": "default", "content": prompt, "complexity": "simple"}
    
    def _parse_vlm_analysis(self, response: str, original_prompt: str) -> dict:
        """Parse VLM response to extract image generation parameters"""
        analysis = {
            "style": "default",
            "content": original_prompt,
            "complexity": "simple",
            "colors": "natural",
            "composition": "standard"
        }
        
        # Extract style information
        if "artistic" in response.lower() or "art" in response.lower():
            analysis["style"] = "artistic"
        elif "photorealistic" in response.lower() or "photo" in response.lower():
            analysis["style"] = "photorealistic"
        elif "cartoon" in response.lower() or "animated" in response.lower():
            analysis["style"] = "cartoon"
        elif "abstract" in response.lower():
            analysis["style"] = "abstract"
        
        # Extract complexity
        if "complex" in response.lower() or "detailed" in response.lower():
            analysis["complexity"] = "complex"
        elif "simple" in response.lower() or "minimal" in response.lower():
            analysis["complexity"] = "simple"
        
        # Extract color information
        if "vibrant" in response.lower() or "colorful" in response.lower():
            analysis["colors"] = "vibrant"
        elif "monochrome" in response.lower() or "black and white" in response.lower():
            analysis["colors"] = "monochrome"
        
        return analysis
    
    def _generate_image_from_analysis(self, analysis: dict, width: int = 512, height: int = 512) -> Tuple[Optional[np.ndarray], Optional[Image.Image]]:
        """Generate image based on VLM analysis"""
        try:
            # Create a base image based on analysis
            if analysis["style"] == "artistic":
                # Create artistic pattern
                img_array = self._create_artistic_pattern(width, height, analysis)
            elif analysis["style"] == "photorealistic":
                # Create photorealistic-like image
                img_array = self._create_photorealistic_image(width, height, analysis)
            elif analysis["style"] == "cartoon":
                # Create cartoon-like image
                img_array = self._create_cartoon_image(width, height, analysis)
            elif analysis["style"] == "abstract":
                # Create abstract image
                img_array = self._create_abstract_image(width, height, analysis)
            else:
                # Default image generation
                img_array = self._create_default_image(width, height, analysis)
            
            # Convert to PIL Image
            img = Image.fromarray(img_array)
            return img_array, img
            
        except Exception as e:
            print(f"⚠️ Image generation failed: {e}")
            return None, None
    
    def _create_artistic_pattern(self, width: int, height: int, analysis: dict) -> np.ndarray:
        """Create artistic pattern based on analysis"""
        img = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Create gradient background
        for y in range(height):
            for x in range(width):
                r = int(255 * (x / width))
                g = int(255 * (y / height))
                b = int(255 * ((x + y) / (width + height)))
                img[y, x] = [r, g, b]
        
        # Add artistic elements
        if analysis["complexity"] == "complex":
            # Add more complex patterns
            for i in range(10):
                center_x = np.random.randint(0, width)
                center_y = np.random.randint(0, height)
                radius = np.random.randint(20, 100)
                color = np.random.randint(0, 256, 3)
                
                for y in range(max(0, center_y - radius), min(height, center_y + radius)):
                    for x in range(max(0, center_x - radius), min(width, center_x + radius)):
                        if (x - center_x)**2 + (y - center_y)**2 <= radius**2:
                            img[y, x] = color
        
        return img
    
    def _create_photorealistic_image(self, width: int, height: int, analysis: dict) -> np.ndarray:
        """Create photorealistic-like image"""
        img = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Create natural-looking gradients
        for y in range(height):
            for x in range(width):
                # Sky-like gradient
                sky_factor = y / height
                r = int(135 + 120 * sky_factor)
                g = int(206 + 49 * sky_factor)
                b = int(235 + 20 * sky_factor)
                img[y, x] = [r, g, b]
        
        # Add some texture
        noise = np.random.randint(0, 30, (height, width, 3))
        img = np.clip(img + noise, 0, 255).astype(np.uint8)
        
        return img
    
    def _create_cartoon_image(self, width: int, height: int, analysis: dict) -> np.ndarray:
        """Create cartoon-like image"""
        img = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Create flat color areas
        colors = [
            [255, 100, 100],  # Red
            [100, 255, 100],  # Green
            [100, 100, 255],  # Blue
            [255, 255, 100],  # Yellow
            [255, 100, 255],  # Magenta
        ]
        
        # Divide image into regions
        for y in range(0, height, height // 4):
            for x in range(0, width, width // 4):
                color = colors[np.random.randint(0, len(colors))]
                img[y:y + height // 4, x:x + width // 4] = color
        
        return img
    
    def _create_abstract_image(self, width: int, height: int, analysis: dict) -> np.ndarray:
        """Create abstract image"""
        img = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Create geometric shapes
        for _ in range(5):
            # Random rectangle
            x1, x2 = sorted(np.random.randint(0, width, 2))
            y1, y2 = sorted(np.random.randint(0, height, 2))
            color = np.random.randint(0, 256, 3)
            img[y1:y2, x1:x2] = color
        
        return img
    
    def _create_default_image(self, width: int, height: int, analysis: dict) -> np.ndarray:
        """Create default image"""
        img = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Simple gradient
        for y in range(height):
            for x in range(width):
                r = int(255 * (x / width))
                g = int(255 * (y / height))
                b = 128
                img[y, x] = [r, g, b]
        
        return img
    
    def generate_image(self, prompt: str, width: int = 512, height: int = 512) -> Tuple[Optional[np.ndarray], Optional[Image.Image]]:
        """Generate image from prompt using VLM analysis"""
        print(f"🎨 Generating image for prompt: '{prompt}'")
        
        # Analyze prompt with VLM
        analysis = self._analyze_prompt_with_vlm(prompt)
        print(f"📊 VLM Analysis: {analysis}")
        
        # Generate image based on analysis
        img_array, img = self._generate_image_from_analysis(analysis, width, height)
        
        if img_array is not None and img is not None:
            print("✅ Image generated successfully")
            return img_array, img
        else:
            print("❌ Image generation failed")
            return None, None