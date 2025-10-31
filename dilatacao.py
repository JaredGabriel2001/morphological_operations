import numpy as np  # Biblioteca para manipulação de matrizes (representam imagens e kernels)

def dilatation(img, kernel):

    # obtem o tamanho (altura e largura) do elemento estruturante
    k_h, k_w = kernel.shape

    # calcula o "padding", a quantidade de pixels que será adicionada em volta da imagem
    pad_h, pad_w = (k_h // 2, k_h // 2), (k_w // 2, k_w // 2)

    # se o kernel tiver dimensões pares, ajusta o padding para manter o ponto central correto
    # exemplo: um kernel 4x4 precisa de ajuste, pois não tem um centro "exato"
    if k_h % 2 == 0:
        pad_h = (k_h // 2, k_h // 2 - 1)
    if k_w % 2 == 0:
        pad_w = (k_w // 2, k_w // 2 - 1)

    # adiciona bordas de zeros (fundo preto) a imagem original
    # assim o kernel pode ser aplicado mesmo nas regiões próximas das bordas
    # mode='constant' e constant_values=0 garantem que o preenchimento é feito com 0 (preto)
    padded_image = np.pad(
        img,
        ((pad_h[0], pad_h[1]), (pad_w[0], pad_w[1])),
        mode='constant'
    )

    # cria uma nova imagem (mesmo tamanho da original) preenchida com zeros (preto)
    dilated_image = np.zeros_like(img)

    # percorre todos os pixels da imagem original (sem contar o padding)
    for i in range(pad_h[0], padded_image.shape[0] - pad_h[1]):
        for j in range(pad_w[0], padded_image.shape[1] - pad_w[1]):

            # extrai uma pequena região da imagem do mesmo tamanho do kernel
            # essa região "anda" sobre a imagem conforme o kernel é aplicado pixel a pixel
            region = padded_image[
                i - pad_h[0] : i + pad_h[1] + 1,
                j - pad_w[0] : j + pad_w[1] + 1
            ]

            # a operação de dilatação é satisfeita se HOUVER SOBREPOSIÇÃO
            # entre algum pixel 1 do kernel e algum pixel 1 da imagem
            # np.any() retorna True se pelo menos uma condição for verdadeira
            if np.any(region[kernel == 1] == 1):
                # Se essa condição for atendida, o pixel central se torna 1 (branco)
                dilated_image[i - pad_h[0], j - pad_w[0]] = 1

    return dilated_image
