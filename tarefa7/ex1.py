import numpy as np
import cv2 as cv

img = cv.imread('1.jpg')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 256
ret,label,centroides=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
centroides = np.uint8(centroides)
imgCentroides = centroides[label.flatten()]
imgModificada = imgCentroides.reshape((img.shape))

cv.imshow("Imagem Original", img)
cv.imshow('Imagem 8 bits', imgModificada)
cv.waitKey(0)
cv.destroyAllWindows()
