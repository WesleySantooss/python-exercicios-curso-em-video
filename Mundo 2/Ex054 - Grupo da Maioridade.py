from datetime import date

anoatual = date.today().year
maior = 0
menor = 0

for c in range (1, 8):
    ano = int(input(f'Em que ano nasceu a {c}ª pessoa? '))
    idade = anoatual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print (f'\nAo todo tivemos {maior} pessoas maiores de idade')
print (f'E também tivemos {menor} pessoas menores de idade')