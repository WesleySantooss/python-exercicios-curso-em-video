#Resolução do EX60 usando "for" ao invés de "while"
resultado = n = int(input("Digite um número para\ncalcular seu Fatorial: "))
conta = f'{n}'

for i in range (n-1, 0, -1):
    resultado *= i
    conta += f' x {i}'
print (f'Calculando {n}! = {conta} = {resultado}')