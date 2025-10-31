import numpy as np  

def erosion(img, kernel):
    # obtem o tamanho (altura e largura) do kernel (elemento estruturante)
    k_h, k_w = kernel.shape

    # calcula o "padding", area extra adicionada ao redor da imagem
    # isso permite aplicar o kernel também nas bordas
    pad_h, pad_w = (k_h // 2, k_h // 2), (k_w // 2, k_w // 2)

    # ajusta o padding se o kernel tiver dimensões pares
    # (em kernels pares, o "centro" é deslocado levemente para a direita/baixo)
    if k_h % 2 == 0:
        pad_h = (k_h // 2, k_h // 2 - 1)
    if k_w % 2 == 0:
        pad_w = (k_w // 2, k_w // 2 - 1)

    # adiciona bordas de zeros a imagem (para nao perder informação nas extremidades)
    # np.pad adiciona linhas e colunas de pixels 0 (preto) ao redor da imagem
    padded_image = np.pad(
        img,
        ((pad_h[0], pad_h[1]), (pad_w[0], pad_w[1])),
        mode='constant'
    )

    # cria uma nova imagem com o mesmo tamanho da original, inicialmente toda preta (0s)
    eroded_image = np.zeros_like(img)

    # varre cada pixel da imagem original (sem contar o padding)
    for i in range(pad_h[0], padded_image.shape[0] - pad_h[1]):
        for j in range(pad_w[0], padded_image.shape[1] - pad_w[1]):

            # extrai uma "janela" da imagem do mesmo tamanho do kernel
            # essa regiao é usada para comparar com o elemento estruturante
            region = padded_image[
                i - pad_h[0] : i + pad_h[1] + 1,
                j - pad_w[0] : j + pad_w[1] + 1
            ]

            # regra da erosão:
            # o pixel central só sera 1 se TODAS as posições do kernel que sao 1
            # também forem 1 na imagem (ou seja, o kernel "cabe" dentro do objeto).
            if np.all(region[kernel == 1] == 1):
                eroded_image[i - pad_h[0], j - pad_w[0]] = 1

    return eroded_image
