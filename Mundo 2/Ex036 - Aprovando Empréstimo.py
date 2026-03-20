valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Tempo em anos do financiamento: '))

prestacao = valor / (tempo * 12)

print (f'Para pagar uma casa de R${valor:.2f} em 7 anos a prestação será de R${prestacao:.2f}')
if prestacao <= (0.3 * salario):
    print ('Empréstimo pode ser CONCEDIDO!')
else:
    print ('Empréstimo NEGADO!')
