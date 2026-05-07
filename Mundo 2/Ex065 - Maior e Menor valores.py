resp = 'S'
soma = qntd = 0
while resp == 'S':
    n = int(input('Digite um número: '))
    soma += n
    qntd += 1
    if qntd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in ('S', 'N'):
        print ('Opção inválida. Digite novamente', resp)
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print (f"Você digitou {qntd} números e a média foi {(soma/qntd):.2f}")
print (f"O maior valor foi {maior} e o menor foi {menor}")