import cv2
import numpy as np
from matplotlib import pyplot as plt

def showImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def main():
    mae = cv2.imread("mae.jpg")
    pai = cv2.imread("pai.jpg")

    #ambas c/ a mesma dimensão
    alturaMae, larguraMae, _ = mae.shape
    pai = cv2.resize(pai,(larguraMae, alturaMae))

    #Soma os pixel de kd pixel, e os 0.5 sao os pesos.
    amores = cv2.addWeighted(mae, 0.5,pai,0.5, 0)
    showImage(amores)

main()
