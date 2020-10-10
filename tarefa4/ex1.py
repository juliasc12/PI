import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(img):
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)
    plt.show()

def InserindoTexto(texto):
    img = cv2.imread("ceu.jpg")
    finalImage = cv2.putText(img, texto, (250, 120), cv2.FONT_HERSHEY_SIMPLEX ,
                  2.5, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imwrite("escrito-no-ceu.png", finalImage)
    showImage(img)

def UnindoImg():
    ceu = cv2.imread("ceu.jpg")
    marca = cv2.imread("marca.jpg")

    #ambas c/ a mesma dimensão
    alturaCeu, larguraCeu, _ = ceu.shape
    marca = cv2.resize(marca,(larguraCeu, alturaCeu))

    #Soma os pixel de kd pixel, e os 0.5 sao os pesos.
    uniao = cv2.addWeighted(ceu, 1,marca,0.2, 0)
    cv2.imwrite("uniao.png", uniao)
    showImage(uniao)

def main():
    InserindoTexto("Cansada!")
    UnindoImg()

main()
