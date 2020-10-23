import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    _, frame = cap.read() #ler a webcam e joga na variavel frame

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #valores de azul
    azulMinimo = np.array([70, 50, 0])
    azulMaximo = np.array([130, 255, 255])

    #Analisa todos os pixels da img e todos q cairem no intervalo do azul ele marca
    mask = cv2.inRange(hsvImage, azulMinimo, azulMaximo)

    #Pega todos os pixels marcados de branco na mascara e retorna os valores
    #RETR_TREE = retorna tds as curvas e constroi uma arvore hierarquica entre eles
    #CHAIN_APPROX_SIMPLE = pega somente os pontos essenciais da curva e amarzena-os
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #se existir contornos
    if contours:
        #retorna a área em pixels de um determinado contorno
        maxArea = cv2.contourArea(contours[0])
        contourId = 0; i = 0
        for cnt in contours:
            #p pegar o contorno q tiver maior área
            if maxArea < cv2.contourArea(cnt):
                maxArea = cv2.contourArea(cnt)
                #pega identificador do maior contorno
                contourId = i
            i += 1

        #retorna um retângulo que envolve o contorno em questão
        x,y,w,h = cv2.boundingRect(contours[contourId])

        # desenha o retângulo vermelho com espessura 3
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
