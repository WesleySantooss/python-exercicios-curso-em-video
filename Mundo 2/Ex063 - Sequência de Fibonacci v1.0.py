print ('-'*30)
print ('Sequência de Fibonacci'.center(30))
print ('-'*30)
n = int(input('Número de termos a ser exibido: '))
print ('='*30)
a = i = 0
b = 1
while i < n:
    print (a, end=' -> ')
    c = a
    a += b
    b = c
    i += 1
print ('FIM')
print ('='*30)