import numpy as np
import cv2
import time
from tqdm import tqdm
src = cv2.imread("ex4.png")

def onChange(value):
    pass

def videoErosion():
    title_window_erosion = 'Erosao'
    cv2.namedWindow(title_window_erosion)
    cv2.createTrackbar('Valor', title_window_erosion , 0, 50, onChange)

    erosionInicial = 0
    atualizarErosion = False
    erosion_dst = src.copy()
    cntTime = 0

    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    out = cv2.VideoWriter('outputErosao.avi',fourcc, 20.0, (448,600))

    while True:
        erosion_size = cv2.getTrackbarPos('Valor', title_window_erosion)

        if(erosionInicial != erosion_size):
            atualizarErosion = True
            cntTime = time.time()
            erosionInicial = erosion_size

        if(atualizarErosion == True and (time.time() - cntTime > 1)):
            erosion_type = 0
            element = cv2.getStructuringElement(erosion_type, (2*erosion_size + 1,2*erosion_size+1), (erosion_size, erosion_size))
            erosion_dst = cv2.erode(src, element)
            atualizarErosion = False


        cv2.imshow(title_window_erosion, erosion_dst)

        frame = np.array(erosion_dst)
        out.write(frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    out.release()
    cv2.destroyAllWindows()

def videoDilatation():
    title_window_dilatation = 'Dilatation'
    cv2.namedWindow(title_window_dilatation)
    cv2.createTrackbar('Valor', title_window_dilatation , 0, 50, onChange)

    dilatationInicial = 0
    atualizarDilatation = False
    dilatation_dst = src.copy()
    cntTime = 0

    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    out = cv2.VideoWriter('outputDilatation.avi',fourcc, 20.0, (448,600))

    while True:
        dilatation_size = cv2.getTrackbarPos('Valor', title_window_dilatation)

        if(dilatationInicial != dilatation_size):
            atualizarDilatation = True
            cntTime = time.time()
            dilatationInicial = dilatation_size

        if(atualizarDilatation == True and (time.time() - cntTime > 1)):
            dilatation_type = 0
            element = cv2.getStructuringElement(dilatation_type, (2*dilatation_size + 1,2*dilatation_size+1), (dilatation_size, dilatation_size))
            dilatation_dst = cv2.dilate(src, element)
            atualizarDilatation = False


        cv2.imshow(title_window_dilatation, dilatation_dst)

        frame = np.array(dilatation_dst)
        out.write(frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    out.release()
    cv2.destroyAllWindows()

def main():
    #videoErosion()
    videoDilatation()

main()
