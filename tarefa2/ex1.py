import random

lista_certa = [7,5,4,3,1]
lista_sorteada = [1,3,4,5,7]
random.shuffle(lista_sorteada)

while (lista_certa != lista_sorteada):
    random.shuffle(lista_sorteada)
    print(lista_sorteada)

print("conseguimos!")
