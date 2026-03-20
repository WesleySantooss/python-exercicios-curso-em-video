from datetime import date

ano = int(input('Ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - ano

maioridade = 18 - idade
anomaior = anoatual + maioridade



print (f'Quem nasceu em {ano} tem {idade} anos em {anoatual}')

if idade < 18:
    print (f'Ainda faltam {18 - idade} anos para o alistamento')
    print (f'Seu alistamento será em {anoatual + maioridade}.')
elif idade > 18:
    anospassaram = anoatual - (ano + 18)
    print (f'Você já deveria ter se alistado há {anospassaram} anos.')
    print (f'Seu alistamento foi em {ano + 18}')
else:
    print  ('É hora de se alistar!')