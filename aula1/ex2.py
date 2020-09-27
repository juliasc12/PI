import random

print('O jogo será melhor de 3.. o primeiro a fazer 2 pontos vence!')
jogo = ['pedra','papel','tesoura']
ganhou = 1
computador = 0
usuario = 0

for i in range(0,3):
    sorteio = random.randint(-1,2)
    computador_escolha = jogo[sorteio]
    print(computador_escolha)
    usuario_escolha = input('Escolha: ')
    
    if((usuario_escolha == 'papel') and (computador_escolha == 'pedra')):
        print('Você venceu a partida')
        usuario = usuario + 1
      
    if((usuario_escolha == 'tesoura') and (computador_escolha == 'pedra')):
        print('O computador venceu a partida')
        computador = computador + 1

    if((usuario_escolha == 'papel') and (computador_escolha == 'tesoura')):
        print('O computador venceu a partida')
        computador = computador + 1

    if((usuario_escolha == 'pedra') and (computador_escolha == 'papel')):
        print('O computador venceu a partida')
        computador = computador + 1

    if((usuario_escolha == 'tesoura') and (computador_escolha == 'papel')):
        print('Você ganhou a partida')
        usuario = usuario + 1

    if((usuario_escolha == 'pedra') and (computador_escolha == 'tesoura')):
        print('Você ganhou a partida')
        usuario = usuario + 1

    if((usuario_escolha == 'papel') and (computador_escolha == 'papel')):
        print('A partida empatou')

    if((usuario_escolha == 'tesoura') and (computador_escolha == 'tesoura')):
        print('A partida empatou')

    if((usuario_escolha == "pedra") and (computador_escolha == "pedra")):
        print('A partida empatou')
        
    if(computador == 2):
        print('O jogo acabou. Vitória do computador!')
        break
    
    if(usuario == 2):
        print('O jogo acabou. Vitória do usuário!')
        break
    
