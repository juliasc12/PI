import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def crop(img,y1,altura,x1,largura):
    crop_img = img[ y1:altura , x1:largura ]
    #showImage(crop_img)
    cv2.imwrite("crop.jpg",crop_img)
    return (crop_img)

def paste(img, crop_img, y,x):
    img[y:y+crop_img.shape[0], x:x+crop_img.shape[1]] = crop_img
    showImage(img)
    cv2.imwrite("pythonshop.jpg", img)

def main():
    img = cv2.imread("lisa2.jpg")
    
    y1=28; altura=118; x1=276; largura=362
    crop_img = crop(img,y1,altura,x1,largura)

    y=30; x=347
    pythonshop_img = paste(img,crop_img,y,x)

main()
