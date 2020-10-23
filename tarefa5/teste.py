import numpy as np
import cv2
img = cv2.imread('spider.jpeg')

lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
resultado = np.vstack([lap])
cv2.imshow("Filtro Laplaciano", resultado)


cv2.imshow("Filtro Laplaciano", resultado)
cv2.waitKey(0)
