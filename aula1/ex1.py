import random

sorteio = random.randint(0,10)
print('Você tem 3 chances de acertar o numero sorteado')
print('numero sorteado: ', +sorteio)

for i in range(0,3):
    chute = int(input("Escolha seu número: "))

    if (chute == sorteio):
        print('Você acertou, parabéns!')
        break

    if (chute > sorteio):
        print('Você errou. O numero sorteado é menor')

    if (chute < sorteio):
        print('Você errou. O numero sorteado é maior')


if(chute!=sorteio):
    print ('O numero sorteado era: ', +sorteio)



        

    
