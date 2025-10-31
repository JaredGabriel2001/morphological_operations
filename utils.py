from PIL import Image
import numpy as np

def read_binary_image(file_path):
    # Open the image file
    with Image.open(file_path) as img:
        # Convert image to grayscale
        grayscale_img = img.convert('L')
        # Convert grayscale image to binary (0 and 255)
        binary_img = grayscale_img.point(lambda x: 255 if x < 128 else 0, '1')
        # Convert to numpy array
        binary_array = np.array(binary_img, dtype=np.uint8)
        
    return binary_array
