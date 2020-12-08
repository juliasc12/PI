import re
import cv2
from skimage import feature
from sklearn.svm import SVC
import numpy as np
import pickle
from tqdm import tqdm


rootFolder = "ex1\\"
trainFolder = "treino\\"
testFolder = "teste\\"

faca = "faca\\"
bola = "bola\\"
copo = "taça\\"

cropTrainFolder = "treinoJulia\\"
cropTestFolder = "testeJulia\\"

svmFilename = "obj.svm"

widthWindow = 64
heightWindow = 128

orientationsParam = 9
pixelsPerCellParam = 8
cellsPerBlockParam = 2

def extractFilenamesFromFolder(path, file):
    listFilenames = []
    with open(path + file) as f:
        listFilenames = [line.rstrip() for line in f]
    return listFilenames

def cropRegionOfEachPosImage(path, folder, listOfImages, ListOfAnnotations, isTrain):
    i = 0
    if(isTrain == 1):
        print("Montando base de imagens de pedestres para faca.")
    if(isTrain == 2):
        print("Montando base de imagens de pedestres para bola.")
    else:
        print("Montando base de imagens de pedestres para taça.")

    for eachImage in listOfImages:
        if(isTrain == 1):
            img = cv2.imread(path + trainFolder + faca + eachImage)
        elif(isTrain == 2):
            img = cv2.imread(path + trainFolder + bola + eachImage)
        else:
            img = cv2.imread(path + trainFolder + copo+ eachImage)

        img = cv2.resize(img, (widthWindow, heightWindow))
        flipImg = cv2.flip(img, 1)

        stringImg = listOfImages[i].split("/", 1)

        if(isTrain == 1):
            cv2.imwrite(path + cropFolder + faca + stringImg[0], img)
            cv2.imwrite(path + cropFolder + faca + "flip_" + str(i) + ".png", flipImg)
        elif(isTrain == 2):
            cv2.imwrite(path + cropFolder + bola + stringImg[0], img)
            cv2.imwrite(path + cropFolder + bola + "flip_" + str(i) + ".png", flipImg)
        elif(isTrain == 3):
            cv2.imwrite(path + cropFolder + copo+ stringImg[0], img)
            cv2.imwrite(path + cropFolder + copo+ "flip_" + str(i) + ".png", flipImg)

        i += 1

def setDatabase():
    #train
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + trainFolder, faca)
    cropRegionOfEachPosImage(rootFolder, cropTrainFolder, vectorOfFilenameImagesPos, 1)

    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + trainFolder, bola)
    cropRegionOfEachPosImage(rootFolder, cropTrainFolder, vectorOfFilenameImagesPos, 2)

    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + trainFolder, copo)
    cropRegionOfEachPosImage(rootFolder, cropTrainFolder, vectorOfFilenameImagesPos, 3)

def trainSVM():
    X = np.empty(0)
    Y = np.empty(0)
    dimensionOfFeatureVector = 0

    print("Extraindo feature HOG de faca")
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + cropTrainFolder + faca)
    for eachImage in vectorOfFilenameImagesPos:
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTrainFolder + faca + eachImage[0]

        img = cv2.imread(eachImage, 0)
        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        H = np.array(H)

        if(X.shape[0] == 0):
            X = H
            dimensionOfFeatureVector = X.shape[0]
        else:
            X = np.append(X, H)

        if(Y.shape[0] == 0):
            Y = np.array([0])
        else:
            Y = np.append(Y, np.array([0]))

    print("Extraindo feature HOG de bola...")
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + cropTrainFolder + bola)
    for eachImage in vectorOfFilenameImagesPos:
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTrainFolder + bola + eachImage[0]

        img = cv2.imread(eachImage, 0)
        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        H = np.array(H)

        X = np.append(X, H)
        Y = np.append(Y, np.array([1]))

    print("Extraindo feature HOG de taças")
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + cropTrainFolder + copo)
    for eachImage in vectorOfFilenameImagesPos:
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + cropTrainFolder + copo + eachImage[0]

        img = cv2.imread(eachImage, 0)
        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        H = np.array(H)

        X = np.append(X, H)
        Y = np.append(Y, np.array([2]))

    print("Treinando o SVM...")
    X = np.reshape(X, (-1, dimensionOfFeatureVector))

    svm = SVC(kernel='linear')
    svm.fit(X, Y)
    return svm

def testImages(svmObj):
    font = cv2.FONT_HERSHEY_SIMPLEX
    vectorOfFilenameImagesPos = extractFilenamesFromFolder(rootFolder + testFolder)
    print("Classificando imagens:")
    for eachImage in vectorOfFilenameImagesPos:
        eachImage = eachImage.split("/", -1)
        eachImage = rootFolder + testFolder + eachImage[0]
        img = cv2.imread(eachImage, 0)
        imgShow = cv2.imread(eachImage, 1)
        h, w, _ = imgShow.shape
        img = cv2.resize(img, (widthWindow, heightWindow))

        H = feature.hog(img, orientations=orientationsParam, pixels_per_cell=(pixelsPerCellParam, pixelsPerCellParam), cells_per_block=(cellsPerBlockParam, cellsPerBlockParam), block_norm='L2-Hys', feature_vector = True)
        X = np.array(H)
        X = np.reshape(X, (-1, X.shape[0]))

        if(svmObj.predict(X) == 0):
            cv2.putText(imgShow, 'Faca', (0, 30), font, 1, (10, 255, 10), 3, cv2.LINE_AA)
        elif(svmObj.predict(X) == 1):
            cv2.putText(imgShow, 'Bola', (0, 30), font, 1, (10, 255, 10), 3, cv2.LINE_AA)
        elif(svmObj.predict(X) == 2):
            cv2.putText(imgShow, 'Copo', (0, 30), font, 1, (10, 255, 10), 3, cv2.LINE_AA)

        cv2_imshow(imgShow)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def saveSVM(obj):
    pickle.dump(obj, open(svmFilename, "wb"))

def loadSVM():
    return pickle.load(open(svmFilename, "rb"))

def main():
    treino = True
    #treino = False
    if(treino):
        #constroi a base de dados
        setDatabase()
        #treina o SVM
        svmObj = trainSVM()
        saveSVM(svmObj)
    #testa o SVM
    svmObj = loadSVM()
    testImages(svmObj)

if __name__ == "__main__":
    main()
