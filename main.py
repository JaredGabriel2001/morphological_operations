# pip install pillow numpy opencv-python
# Execução:
# python main.py caminho_imagem caminho_kernel operação saida.png
# Exemplo:
# python main.py imagem.png kernel.png 1 saida.png
# Onde:
#   operação = 1 → Erosão
#             = 2 → Dilatação
#             = 3 → Fechamento
#             = 4 → Abertura

import cv2  # OpenCV: usado aqui apenas para salvar a imagem final (cv2.imwrite)
import argparse # Biblioteca para ler parâmetros via linha de comando (terminal)
from utils import read_binary_image
from erosao import erosion
from dilatacao import dilatation

def main():
    # configura o argparse para aceitar argumentos da linha de comando
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

    # a imagem gerada pelo algoritmo é composta por valores 0 e 1.
    # para salvar como uma imagem real (visível), multiplicamos por 255
    # e invertemos as cores (para que o fundo fique preto e o objeto branco).
    inverted_image = 255 - result * 255

    # o cv2.imwrite é utilizado porque ele salva rapidamente uma matriz numpy
    cv2.imwrite(args.output, inverted_image)

    print(f"Imagem processada e salva em: {args.output}")


if __name__ == '__main__':
    main()
