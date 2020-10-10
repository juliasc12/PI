import cv2
from matplotlib import pyplot as plt
import os

def getColor(img,x,y):
    return img.item(y,x,0), img.item(y,x,1),img.item(y,x,2)

def main():
    img = cv2.imread("lisa2.jpg")
    altura, largura, canais_de_cores = img.shape

    plt.imshow(img[:,:,0], 'gray')
    plt.show()
    plt.imshow(img[:,:,1], 'gray')
    plt.show()
    plt.imshow(img[:,:,0], 'gray')
    plt.show()

    contB=0; contG=0; contR=0
    for y in range(0,altura):
        for x in range(0,largura):
            azul,verde,vermelho = getColor(img,x,y)
            contB = azul+contB
            contG = verde+contG
            contR = vermelho+contR

    #img de dimensoes 436x512 = 223.232
    TotalPixel = 223332
    MediaB = (contB/TotalPixel)
    MediaG = (contG/TotalPixel)
    MediaR = (contR/TotalPixel)

    print("Media Azul: "+str(MediaB)+"/ Media Verde: "+str(MediaG)+"Media Vermelha: "+str(MediaR))


main()
