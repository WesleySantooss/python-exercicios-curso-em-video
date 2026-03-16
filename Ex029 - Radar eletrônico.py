velocidade = float(input('Qual a velocidade atual do carro? '))
multa = 0

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print (f'MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print (f'Você deve pagar uma multa de R${multa:.2f}!')
print (f'Tenha um bom dia! Dirija com segurança!')