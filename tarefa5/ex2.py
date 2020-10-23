import numpy as np
import cv2
from matplotlib import pyplot as plt

def showMultipleImageGrid(imgsArray, titlesArray, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return

    #p passar varias img em 1 coluna precisamos da subplot, no caso 2 linhas e 3 colunas
    fig, axis = plt.subplots(y, x)
    xId, yId, titleId = 0, 0, 0 #contadores da img
    
    for img in imgsArray: #p cada img do meu vet de imagens
        imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #faremos a conversão
        axis[yId, xId].set_title(titlesArray[titleId]) #p esse subplot passamos tal title
        axis[yId, xId].imshow(imgMPLIB) #pedir p img atual ser exibida

        if(len(titlesArray[titleId]) == 0):
            axis[yId,xId].axis('off') #se o titulo n tem caracter n aparece o titulo

        #percorrido a primeira img, passo p seguinte
        titleId += 1
        xId += 1 #primeiro ando pelo coluna, p ex x=1, y=1

        #qdo meu identificador bater com o x q eu passei, no caso 3, ele alcançou o max do meu grid
        if xId == x:
            xId = 0 #volta a contagem dnv, cm x=0 e passo p segunda linha
            yId += 1

    fig.tight_layout(pad=0.5) #diminui a distancia das img
    plt.show() #p mostrar o grid

def plotSixImages():
    imgOriginal = cv2.imread("maquina.jpg") #le a img

    #técnica p desfocar a img alterando a cor de cada pixel misturando cm pixel ao redor.
    #útil p melhorar o processamento da imagem pra aplicar um próximo filtro
    media = cv2.blur(imgOriginal,( 11,11)) #cria um filtro de tam 11x11 e pega a média dos pixels q estão nessa kernel
    mediana = cv2.medianBlur(imgOriginal,11) #despreza valores extremos da kernel, pega o tam da kernel. alterar cor do pixel altual cm pixel vizinho
    #tb precisa da largura e altura da kernel, mas tb tem a qtd de desvio do eixo x e y
    desfoque = cv2.GaussianBlur(imgOriginal , ( 15 , 15 ), 0 ) #gera menos borrão na img, traz um efeito mais natural e reduz ruido

    #identifica o gradiente(variações inesperadas de intensidade de pixel)
    #No filtro sobel p ter uma transofmação completa precisamos juntar o filtro horizontal e o vertical
    #devido ao processamento, trabalhamos cm ponto flutuante de 64 bits(p suportar valores negativos e positivos) p dps converter p uint8
    sobelX = cv2.Sobel(imgOriginal, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(imgOriginal, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    sobel = cv2.bitwise_or(sobelX, sobelY)

    #n exige processamento individual, contudo é necessário trabalhar cm pixel flutuante e dps converter p int sem sinal
    lap = cv2.Laplacian(imgOriginal, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))

    imgsArray = [imgOriginal, media, mediana, desfoque, sobel, lap] #array com as imagens
    titlesArray = ['Imagem Original','Filtro da Média', 'Filtro da Mediana', 'Filtro da Gaussiana', 'Filtro Sobel', 'Filtro Laplaciano']
    showMultipleImageGrid(imgsArray, titlesArray, 3, 2) #3 colunas e 2 linhas

plotSixImages()
