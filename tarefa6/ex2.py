import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread("ex2.png")
img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(img)

cv2.imshow ("Imagem Original" , src)
cv2.imshow ("Imagem Equalizada", eq)
plt.show()
cv2.waitKey ()
