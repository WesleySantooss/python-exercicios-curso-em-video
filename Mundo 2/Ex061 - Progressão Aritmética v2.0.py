print ('Gerador de PA')
print ('-=' * 10)
p1 = int(input('Primeiro termo: '))
r = int(input("Razão da PA: "))
i = 0
while i < 10:
    print (f'{p1 + (i * r)}', end=' -> ')
    i += 1
print ('FIM')