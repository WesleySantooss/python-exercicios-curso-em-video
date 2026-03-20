print ('-=-' * 5, 'LOJÃO', '-=-' * 5)
valor = float(input('Preço das compras: R$'))
print ('\nFORMAS DE PAGAMENTO')
print ('[ 1 ] à vista dinheiro/cheque')
print ('[ 2 ] à vista cartão')
print ('[ 3 ] 2x no cartão')
print ('[ 4 ] 3x ou mais no cartão')

opcao = int(input('Qual sua opção? '))

valorfinal = 0
parcela = 0

if opcao == 1:
    valorfinal = valor * 0.9
elif opcao == 2:
    valorfinal = valor * 0.95
elif opcao == 3:
    valorfinal = valor
    print (f'Sua compra será parcelada em 2x de R${(valor / 2):.2f}')
elif opcao == 4:
    parcela = int(input('Quantas parcelas (3 ou mais) ?  '))
    valorfinal = valor * 1.2
    if parcela < 3:
        print ('Número inválido de parcelas. Reinicie o programa!')
    else:
        print (f'Sua compra será parcelada em {parcela}x de R${(valorfinal / parcela):.2f} COM JUROS')
else:
    print ('Opção inválida de pagamento. Reinicie o programa!')
    valorfinal = valor
print (f'Sua compra de R${valor:.2f} vai custar R${valorfinal:.2f} no final.')
