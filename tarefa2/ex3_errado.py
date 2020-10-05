import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

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

def main():
    img = cv2.imread("sonic.jpg")
    altura, largura, canais_de_cores = img.shape

    for y in range(0,altura):
        for x in range(0,largura):
            azul,verde,vermelho = getColor(img,x,y)
            setColor(img,x,y,verde,azul,vermelho)

    showImg(img)
    cv2.imwrite("Brasonic.jpg",img)

main()
