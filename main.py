#pip install pillow numpy opencv-python
#python main.py caminho_imagem caminho_kernel operação (1 = Erosão ,2 = Dilatação,3= Fechamento,4= Abertura) saida.png

import cv2
import argparse
from utils import read_binary_image
from erosao import erosion
from dilatacao import dilatation

def main():
    # Configura o argparse para aceitar argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Operações morfológicas em imagens binárias.")
    parser.add_argument("image", type=str, help="Caminho para a imagem binária (arquivo de texto).")
    parser.add_argument("kernel", type=str, help="Caminho para o elemento estruturante (arquivo de texto).")
    parser.add_argument(
        "operation", type=int, choices=[1, 2, 3, 4],
        help="Operação a ser realizada: 1 - Erosão, 2 - Dilatação, 3 - Fechamento, 4 - Abertura."
    )
    parser.add_argument("output", type=str, help="Caminho para salvar a imagem de saída.")

    args = parser.parse_args()

    # Lê os arquivos de entrada
    image = read_binary_image(args.image)
    kernel = read_binary_image(args.kernel)

    # Realiza a operação selecionada
    if args.operation == 1:
        result = erosion(image, kernel)
    elif args.operation == 2:
        result = dilatation(image, kernel)
    elif args.operation == 3:
        result = erosion(dilatation(image, kernel), kernel)
    elif args.operation == 4:
        result = dilatation(erosion(image, kernel), kernel)

    # print(result)
    # Inverte a imagem e salva como arquivo
    inverted_image = 255 - result * 255
    # print(inverted_image)
    cv2.imwrite(args.output, inverted_image)

    print(f"Imagem processada e salva em: {args.output}")


if __name__ == '__main__':
    main()
