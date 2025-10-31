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

import cv2
import argparse
from utils import read_binary_image
from erosao import erosion
from dilatacao import dilatation

def main():
    # Argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Operações morfológicas em imagens binárias.")
    parser.add_argument("image", type=str, help="Caminho da imagem binária (arquivo de imagem).")
    parser.add_argument(
        "operation", type=int, choices=[1, 2, 3, 4],
        help="Operação: 1 - Erosão, 2 - Dilatação, 3 - Fechamento, 4 - Abertura."
    )
    parser.add_argument("output", type=str, help="Caminho para salvar a imagem resultante.")
    args = parser.parse_args()

    # Lê a imagem de entrada
    image = read_binary_image(args.image)

    # Executa a operação selecionada (kernel já está dentro dos arquivos)
    if args.operation == 1:
        result = erosion(image)
    elif args.operation == 2:
        result = dilatation(image)
    elif args.operation == 3:
        result = erosion(dilatation(image))
    elif args.operation == 4:
        result = dilatation(erosion(image))

    # Converte o resultado (0/1) para 0/255 e inverte para visualização
    inverted_image = 255 - result * 255
    cv2.imwrite(args.output, inverted_image)

    print(f"Imagem processada e salva em: {args.output}")

if __name__ == '__main__':
    main()