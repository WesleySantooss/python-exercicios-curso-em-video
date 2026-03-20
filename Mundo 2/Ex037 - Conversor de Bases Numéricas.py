'''

n = int(input('Digite um número inteiro: '))
print ('[ 1 ] converter para BINÁRIO')
print ('[ 2 ] converter para OCTAL')
print ('[ 3 ] converter para HEXADECIMAL')

noriginal = n
op = int(input('Sua opção: '))
opt = ''

if op == 1:
    n = bin(n)[2:]
    opt = 'BINÁRIO'
elif op == 2:
    n = oct(n)[2:]
    opt = 'OCTAL'
elif op == 3:
    n = hex(n)[2:]
    opt = 'HEXADECIMAL'
else:
    print ('A opção escolhida é inválida!')

print (f'{noriginal} convertido para {opt} é igual a {n}')]

'''

n = int(input('Digite um número inteiro: '))

print ('Escolha uma das bases para conversão:')
print ('[ 1 ] converter para BINÁRIO')
print ('[ 2 ] converter para OCTAL')
print ('[ 3 ] converter para HEXADECIMAL')

op = int(input('Sua opção: '))

if op == 1:
    print (f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif op == 2:
    print (f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif op == 3:
    print (f'{n} convertido para OCTAL é igual a {hex(n)[2:]}')
else:
    print ('A opção escolhida é inválida!')