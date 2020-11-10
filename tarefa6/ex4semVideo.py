import numpy as np
import cv2
import time
from tqdm import tqdm
import pyautogui

def videoErosion(val):
    erosion_size = cv2.getTrackbarPos('Valor', title_window_erosion)
    erosion_type = 0

    element = cv2.getStructuringElement(erosion_type, (2*erosion_size + 1,2*erosion_size+1), (erosion_size, erosion_size))

    erosion_dst = cv2.erode(src, element)
    cv2.imshow(title_window_erosion, erosion_dst)

def videoDilatation(val):
    dilatation_size = cv2.getTrackbarPos('Valor', title_window_dilatation)
    dilatation_type = 0

    element = cv2.getStructuringElement(dilatation_type, (2*dilatation_size + 1, 2*dilatation_size+1), (dilatation_size, dilatation_size))
    dilatation_dst = cv2.dilate(src, element)
    cv2.imshow(title_window_dilatation, dilatation_dst)

src = cv2.imread("ex4.png")
title_window_erosion = 'Erosao'
title_window_dilatation = 'Dilatacao'

cv2.namedWindow(title_window_erosion)
cv2.createTrackbar('Valor', title_window_erosion , 0, 50, videoErosion)

cv2.namedWindow(title_window_dilatation)
cv2.createTrackbar('Valor', title_window_dilatation , 0, 200, videoDilatation)

cv2.waitKey()
