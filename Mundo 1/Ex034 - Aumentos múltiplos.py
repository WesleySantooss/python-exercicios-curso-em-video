salario = float(input('Qual é o salário do funcionário? R$'))

if (salario > 0) and (salario <= 1250):
    print (f'Quem ganhava R${salario:.2f} passa a ganhar R${(salario * 1.15):.2f} agora.')
elif salario > 1250:
    print (f'Quem ganhava R${salario:.2f} passa a ganhar R${(salario * 1.1):.2f} agora.')
else:
    print ('O valor digitado é inválido!')