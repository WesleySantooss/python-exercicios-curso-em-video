frase = str(input('Digite uma frase: ')).upper().split()
frasecompleta = ''.join(frase)
inverso = ''

for c in range (len(frasecompleta) -1, -1, -1 ):
    inverso += frasecompleta[c]

print (f'O inverso de {frasecompleta} é {inverso}')

if inverso == frasecompleta:
    print ('Temos um palíndromo!')
else:
    print ('A frase digitada não é um palíndromo!')