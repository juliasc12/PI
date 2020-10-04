import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

def showImg(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def dataImg(img):
    altura, largura, canais_de_cores = img.shape
    print("Altura: " + str(altura) + " / Largura = " + str(largura) + " / Canais de Cor =  " + str(canais_de_cores))
    byts = os.path.getsize('lisa.png')
    print("Tamanho da imagem em byts: " + str(byts))

def main():
    img = cv2.imread("lisa.png")
    dataImg(img)
    showImg(img)

main()
