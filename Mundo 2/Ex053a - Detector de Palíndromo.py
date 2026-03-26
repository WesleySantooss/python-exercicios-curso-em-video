#Outra solução para o exercício:
frase = str(input('Digite uma frase: ')).upper().split()
frasecompleta = ''.join(frase)
inverso = frasecompleta[::-1]

print (f'O inverso de {frasecompleta} é {inverso}')

if inverso == frasecompleta:
    print ('Temos um palíndromo!')
else:
    print ('A frase digitada não é um palíndromo!')