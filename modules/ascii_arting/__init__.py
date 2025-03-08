"""
Module for ASCII-arting
in Screenshoter
"""
try:
    from PIL import Image
    import numpy as np
except ImportError:
    raise ImportError("Numpy or/and Pillow not found. Disable ascii arting in config")

def ascii_art(image):
    img = Image.open(image)
    output_width = 80
    aspect_ratio = img.height / img.width
    output_height = int(output_width * aspect_ratio * 0.55)
    img = img.resize((output_width, output_height))
    img = img.convert("L")
    pixels = np.array(img)
    ascii_chars = "@%#*+=-:. "
    ascii_length = len(ascii_chars)
    normalized_pixels = np.clip(pixels // 25, 0, ascii_length - 1)
    ascii_art = "\n".join("".join(ascii_chars[pixel] for pixel in row) for row in normalized_pixels)
    
    return ascii_art