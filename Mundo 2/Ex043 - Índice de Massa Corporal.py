peso = float(input('Peso em KG: '))
altura = float(input('Altura em M: '))

imc = peso / (altura ** 2)

print (f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print ('Você está ABAIXO do peso normal')
elif imc < 25:
    print ('PARABÉNS, você está na faixa de peso NORMAL')
elif imc < 35:
    print ('Você está em SOBREPESO')
elif imc < 40:
    print ('Você está em OBESIDADE!')
else:
    print ('Você está em OBESIDADE MÓRBIDA, cuidado!')
