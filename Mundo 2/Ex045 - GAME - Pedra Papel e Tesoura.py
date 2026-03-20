from time import sleep
from random import randint

print ('SUAS OPÇÕES:')
print ('[ 0 ] PEDRA')
print ('[ 1 ] PAPEL')
print ('[ 2 ] TESOURA')

opcao = int(input('Qual a sua jogada? '))
if opcao not in [0, 1, 2]:
    print ('JOGADA INVÁLIDA!')
else:
    opcaocomputador = randint(0, 2)
    vencedor = ''

    print ('JO')
    sleep(0.75)
    print ('KEN')
    sleep(0.55)
    print ('PO!!!')

    item = ['Pedra', 'Papel', 'Tesoura']
    print ('-=' * 10)
    print (f'Computador jogou {item[opcaocomputador]}')
    print (f'Jogador jogou {item[opcao]}')
    print ('-=' * 10)

    if opcao == 0: #Jogador jogou Pedra
        if opcaocomputador == 1:# Computador jogou PAPEL
            vencedor = 'COMPUTADOR'
        elif opcaocomputador == 2: #Computador jogou tesoura
            vencedor = 'JOGADOR'
        else:
            vencedor = 'EMPATE'
    elif opcao == 1: #Jogador jogou papel
        if opcaocomputador == 0: #computador jogou pedra
            vencedor = 'JOGADOR'
        elif opcaocomputador == 2: #computador jogou tesoura
            vencedor = 'COMPUTADOR'
        else:
            vencedor = 'EMPATE'
    elif opcao == 2: #Jogador jogou tesoura
        if opcaocomputador == 0: #computador jogou pedra
            vencedor = 'COMPUTADOR'
        elif opcaocomputador == 1: #computador jogou papel
            vencedor = 'JOGADOR'
        else:
            vencedor = 'EMPATE'
    else:
        print ('JOGADA INVÁLIDA!')
    if vencedor == 'EMPATE':
        print ('Ninguem ganhou \nHouve um empate!')
    else:
        print (f'{vencedor} VENCE')