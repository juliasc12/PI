import numpy as np
import cv2 as cv

img = cv.imread('1.jpg')
Z = img.reshape((-1,3)) #altura e colunas da nova matriz -1 digo q n sei altura mas a

# convert to np.float32
Z = np.float32(Z)

# define criteria,
#epslon = qto diferentes serao um criterio do outro. por exemplo, 0 é ridigo
#max_iter = maximo de interações. no caso 10 de interações e epslon 1
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 0.1)
K = 256 #img de 8 bits tem 256 cores

#invoca kmeans
#10x reiniciar o algorimto p ter melhores resultados
ret,label,centroides = cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
centroides = np.uint8(centroides)
imgCentroides = centroides[label.flatten()] #label = matriz quadrada q tem a localização de cada pixel e o flattem pega essa matriz e transnforma num vetor de 1 d
imgModificada = imgCentroides.reshape((img.shape))

cv.imshow("Imagem Original", img)
cv.imshow('Imagem 8 bits', imgModificada)
cv.waitKey(0)
cv.destroyAllWindows()
