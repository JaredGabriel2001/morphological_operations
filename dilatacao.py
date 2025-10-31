import numpy as np

def dilatation(img):

    kernel = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ], dtype=np.uint8)

    # Para alterar os resultados, modifique o kernel acima.
    # Exemplos:
    # - Cruz:
    #   kernel = np.array([
    #       [0, 1, 0],
    #       [1, 1, 1],
    #       [0, 1, 0]
    #   ], dtype=np.uint8)
    #
    # - Linha horizontal:
    #   kernel = np.array([
    #       [1, 1, 1]
    #   ], dtype=np.uint8)
    #
    # - Linha vertical:
    #   kernel = np.array([
    #       [1],
    #       [1],
    #       [1]
    #   ], dtype=np.uint8)
    # ============================================================

    k_h, k_w = kernel.shape
    pad_h, pad_w = (k_h // 2, k_h // 2), (k_w // 2, k_w // 2)

    if k_h % 2 == 0:
        pad_h = (k_h // 2, k_h // 2 - 1)
    if k_w % 2 == 0:
        pad_w = (k_w // 2, k_w // 2 - 1)

    padded_image = np.pad(
        img,
        ((pad_h[0], pad_h[1]), (pad_w[0], pad_w[1])),
        mode='constant'
    )
    dilated_image = np.zeros_like(img)

    for i in range(pad_h[0], padded_image.shape[0] - pad_h[1]):
        for j in range(pad_w[0], padded_image.shape[1] - pad_w[1]):
            region = padded_image[
                i - pad_h[0]:i + pad_h[1] + 1,
                j - pad_w[0]:j + pad_w[1] + 1
            ]
            if np.any(region[kernel == 1] == 1):
                dilated_image[i - pad_h[0], j - pad_w[0]] = 1

    return dilated_image
