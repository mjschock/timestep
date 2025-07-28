import numpy as np
from PIL import Image
import re

class ImageTextConverter:
    @staticmethod
    def image_to_text(img_array):
        """Convert numpy image to text format: (x,y):#RRGGBB"""
        h, w = img_array.shape[:2]
        if len(img_array.shape) == 2:  # grayscale
            img_array = np.stack([img_array] * 3, axis=-1)
        
        text = f"Size:{w}x{h}\n"
        for y in range(h):
            for x in range(w):
                r, g, b = img_array[y, x]
                text += f"({x},{y}):#{r:02x}{g:02x}{b:02x} "
            text += "\n"
        return text
    
    @staticmethod
    def text_to_image(text):
        """Convert text back to numpy image"""
        lines = text.strip().split('\n')
        size_match = re.search(r'Size:(\d+)x(\d+)', lines[0])
        w, h = int(size_match.group(1)), int(size_match.group(2))
        
        img = np.zeros((h, w, 3), dtype=np.uint8)
        
        for line in lines[1:]:
            matches = re.findall(r'\((\d+),(\d+)\):(#[a-fA-F0-9]{6})', line)
            for x_str, y_str, hex_color in matches:
                x, y = int(x_str), int(y_str)
                r = int(hex_color[1:3], 16)
                g = int(hex_color[3:5], 16) 
                b = int(hex_color[5:7], 16)
                img[y, x] = [r, g, b]
        return img

    @staticmethod
    def test_lossless_conversion():
        """Test that conversion is lossless"""
        converter = ImageTextConverter()
        test_img = np.random.randint(0, 256, (8, 8, 3), dtype=np.uint8)
        text = converter.image_to_text(test_img)
        reconstructed = converter.text_to_image(text)
        assert np.array_equal(test_img, reconstructed), "CONVERSION FAILED!"
        print("✓ Lossless conversion verified")
        return True