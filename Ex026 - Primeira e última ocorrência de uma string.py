frase = str(input('Digite uma frase: ')).upper().strip()
quantidadea = frase.count('A')
primeiroa = frase.find('A') + 1
ultimoa = frase.rfind('A') + 1

print (f'A letra A aparece {quantidadea} vezes na frase.')
print (f'A primeira letra A apareceu na posição {primeiroa}')
print (f'A última letra A apareceu na posição {ultimoa}')