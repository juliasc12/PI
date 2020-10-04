import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def crop(img,y1,altura,x1,largura):
    crop_img = img[ y1:altura , x1:largura ]
    showImage(crop_img)
    cv2.imwrite("crop.jpg",crop_img)

def main():
    img = cv2.imread("lisa2.jpg")
    y1=28; altura=118; x1=276; largura=375
    crop(img,y1,altura,x1,largura)

main()
