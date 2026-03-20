from datetime import date

anonascimento = int(input('Ano de Nascimento: '))
anoatual = date.today().year
idade = anoatual - anonascimento
classificacao = ''

if idade <= 9:
    classificacao = 'MIRIM'
elif idade <= 14:
    classificacao = 'INFANTIL'
elif idade <= 19:
    classificacao = 'JUNIOR'
elif idade <= 25:
    classificacao = 'SÊNIOR'
else:
    classificacao = 'MASTER'
print (f'O atleta tem {idade} anos.')
print (f'Classificação: {classificacao}')