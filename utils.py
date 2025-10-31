from PIL import Image
import numpy as np

def read_binary_image(file_path):
    # abre a img
    with Image.open(file_path) as img:
        # converte para grayscale
        grayscale_img = img.convert('L')
        # converte grayscale para binario (0 and 255)
        binary_img = grayscale_img.point(lambda x: 255 if x < 128 else 0, '1')
        # converte para numpy array
        binary_array = np.array(binary_img, dtype=np.uint8)
        
    return binary_array
