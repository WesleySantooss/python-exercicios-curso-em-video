peso = maior = menor = float(input("Peso da 1ª pessoa: "))
for i in range (2, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print (f'Peso maior informado: {maior:.1f}Kg')
print (f'Peso menor informado: {menor:.1f}Kg')