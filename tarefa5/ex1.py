import numpy as np
import cv2
import time
from tqdm import tqdm

def onChange(value):
    pass

img = cv2.imread("spider.jpeg")
copyImg = img.copy() #copia a img original
windowTitle = "Limiarizacao - tarefa 5" #nome da janela
cv2.namedWindow(windowTitle) #crio a janela gráfica

#cria o trackbar(nome, titulo da janela, valor de inicio no track bar e valor maximo)
#onChange é uma função q é chamada toda vez q a app alterar o valor, mas como a gnt n precisa só criamos ela cm a palavra chave pass
cv2.createTrackbar("Limiar: ", windowTitle, 100,255, onChange)

limiarInicial = 100 #valor inicial do trackbar
atualizarLimiar = False
cntTime = 0 #controla p saber qdo o usuario soltou o controle do trackbar

#loop infinito pra mostrar a imagem enquanto o programa estiver rodando
while True:
    limiar_value = cv2.getTrackbarPos("Limiar: ", windowTitle) #retorna valor q o usuário marcou

    if(limiarInicial != limiar_value): #se entra é pq trocou o valor do limiar no trackbar
        atualizarLimiar = True #entao é vdd q atualizou o valor
        cntTime = time.time() #conta o tempo q o usuario ta clicado no track
        limiarInicial = limiar_value #altera o valor inicial do limiar pro atual do trackbar

    if(atualizarLimiar == True and (time.time() - cntTime > 1)): #se trocou limiar e passou 1s q o usuario clico no track bar
        copyImg = img.copy() #fazemos a copia da img
        #pegamos o valor do limiar da posição do trackbar e passamos p método de limiarizar a img
        limiar_value, copyImg =  cv2.threshold(img, limiar_value, 255, cv2.THRESH_BINARY)
        #img atualizada entao atualizar limiar recebe falso
        atualizarLimiar = False

    #mostrar a imagem na janela, com o titulo escolhido e a img
    cv2.imshow(windowTitle, copyImg)

    #fechar o programa
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows() #fecha todas janelas abertas
