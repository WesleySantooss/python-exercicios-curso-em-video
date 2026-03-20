distancia = float(input('Digite a distância da viagem em Km: '))
passagem = 0

if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print (f'Você está prestes a começar uma viagem de {distancia}Km.')
print (f'O valor da passagem é de R${passagem:.2f}.')
