n1 = int(input('Primeiro valor: '))#2
n2 = int(input('Segundo valor: '))#4
n3 = int(input('Terceiro valor: '))#7

if (n1 >= n2) and (n2 >= n3):
    print (f'O menor valor digitado foi: {n3}')
    print (f'O maior valor digitado foi: {n1}')
elif (n1 >= n3) and (n3 >= n2):
    print (f'O menor valor digitado foi: {n2}')
    print (f'O maior valor digitado foi: {n1}')
elif (n2 >= n1) and (n1 >= n3):
    print (f'O menor valor digitado foi: {n3}')
    print (f'O maior valor digitado foi: {n2}')
elif (n2 >= n3) and (n3 >= n1):
    print (f'O menor valor digitado foi: {n1}')
    print (f'O maior valor digitado foi: {n2}')
elif (n3 >= n1) and (n1 >= n2):
    print (f'O menor valor digitado foi: {n2}')
    print (f'O maior valor digitado foi: {n3}')
elif (n3 >= n2) and (n2 >= n1):
    print (f'O menor valor digitado foi: {n1}')
    print (f'O maior valor digitado foi: {n3}')