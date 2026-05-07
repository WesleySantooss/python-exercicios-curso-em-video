n = int(input("Digite um número para\ncalcular seu Fatorial: "))
resultado = n
i = n - 1
conta = f'{n}'
while i > 0:
    resultado *= i
    conta += f' x {i}'
    i -= 1
print (f"Calculando {n}! = {conta} = {resultado}")