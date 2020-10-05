import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImg(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def getColor(img,x,y):
    return img.item(y,x,0), img.item(y,x,1),img.item(y,x,2)

def setColor(img, x,y, b, g, r):
    img.itemset((y,x,0), b)
    img.itemset((y,x,1), g)
    img.itemset((y,x,2), r)

def imgAzul(img,altura,largura):
    for y in range(0,altura):
        for x in range(0,largura):
            azul,verde,vermelho = getColor(img,x,y)
            setColor(img,x,y,azul,0,0)

    cv2.imwrite("LisaAzul.jpg",img)

def imgVerde(img,altura,largura):
    for y in range(0,altura):
        for x in range(0,largura):
            azul,verde,vermelho = getColor(img,x,y)
            setColor(img,x,y,0,verde,0)
    cv2.imwrite("LisaVerde.jpg",img)

def imgVermelho(img,altura,largura):
    for y in range(0,altura):
        for x in range(0,largura):
            azul,verde,vermelho = getColor(img,x,y)
            setColor(img,x,y,0,0,vermelho)

    LisaVermelha = cv2.imwrite("LisaVermelha.jpg",img)



def main():
    img = cv2.imread("lisa2.jpg")
    altura, largura, canais_de_cores = img.shape

    #Lisa_Azul = imgAzul(img,altura,largura)
    #Lisa_Verde= imgVerde(img,altura,largura)
    #Lisa_Vermelho = imgVermelho(img,altura,largura)
    showImg(img)

main()
