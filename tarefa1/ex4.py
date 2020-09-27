import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImg(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def main():
    img = cv2.imread("lisa.png")

    y1 = int(input('valor do y: '))
    x1 = int(input('valor do x: '))
    altura = int(input('valor da altura: '))
    largura = int(input('valor da largura: '))

    #tampar o olho da lisa pq é legal y=300 x=700 altura=580 largura=1200
    for y in range(y1,altura):
        for x in range(x1,largura):

            #acessar o item da posição
            azul = img.item(y,x,0)
            verde = img.item(y,x,1)
            vermelho = img.item(y,x,2)

            #modificar o item na posição
            img.itemset((y,x,0),0)
            img.itemset((y,x,1),0)
            img.itemset((y,x,2),0)

    showImg(img)

main()
