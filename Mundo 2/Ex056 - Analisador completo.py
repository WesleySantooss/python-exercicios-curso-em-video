somaidade = maior = qntdf = 0
nomemaior = ''
for i in range (1, 5):
    print (f'\n----- {i}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('[M/F]: '))
    if i == 1:
        maior = idade
        nomemaior = nome
    elif idade > maior:
        maior = idade
        nomemaior = nome
    if sexo == 'F':
        if idade < 20:
            qntdf += 1
    somaidade += idade
print (f'A média de idade do grupo é de {(somaidade/4):.1f} anos')
print (f'O homem mais velho tem {maior} anos e se chama {nomemaior}')
print (f'Ao todo são {qntdf} mulheres com menos de 20 anos')