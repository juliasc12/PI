import cv2
import numpy as np
from matplotlib import pyplot as plt

def pretoEbranco():
    img = cv2.imread("preto.jpg")
    plt.hist(img.ravel(), 256, [0,256])
    cv2.imshow("Imagem", img)
    plt.show()

def colorido():
    img = cv2.imread("colorida.jpg")
    color = ('b','g', 'r')

    for i, col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr, color = col)
        plt.xlim([0,256])
    cv2.imshow("Imagem", img)
    plt.show()

colorido()
