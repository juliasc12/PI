import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

def comparar(img1, img2):
    color = ('b','g', 'r')

    for i, col in enumerate(color):
        histr_1 = cv2.calcHist([img1],[i],None,[256],[0,256])
        plt.plot(histr_1, color = col)
        plt.xlim([0,256])
    #plt.show()

    for i, col in enumerate(color):
        histr_2 = cv2.calcHist([img2],[i],None,[256],[0,256])
        plt.plot(histr_2, color = col)
        plt.xlim([0,256])
    #plt.show()

    correlacao = cv2.compareHist(histr_1, histr_2, cv2.HISTCMP_CORREL)
    chiSquare = cv2.compareHist(histr_1, histr_2, cv2.HISTCMP_CHISQR)
    bhattacharrya = cv2.compareHist(histr_1, histr_2, cv2.HISTCMP_BHATTACHARYYA)

    resultado = math.sqrt(math.pow(correlacao,2) + math.pow(chiSquare,2) + math.pow(bhattacharrya,2))
    print("%.1f" %resultado)
    return resultado

def main():
    s1 = cv2.imread("s1.jpg")
    s2 = cv2.imread("s2.jpg")
    d1 = cv2.imread("preto.jpg")
    d2 = cv2.imread("colorida.jpg")
    d3 = cv2.imread("ex2.png")


    valor_par0 = comparar(s1, d1)
    valor_par1 = comparar(s1, d2)
    valor_par2 = comparar(s1, s2)
    valor_par3 = comparar(s1, d3)

    vet = [valor_par0, valor_par1, valor_par2, valor_par3]

    menor=valor_par1
    id=0

    for i in range (0, len(vet)):
        if(menor > vet[i]):
            menor = vet[i]
            id = i

    print("A imagem mais parecida é a de posição %d " %id +"no vetor e possui valor de: %.1f"%menor)

main()
