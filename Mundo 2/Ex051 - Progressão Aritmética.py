print ('=' * 30)
print ('10 TERMOS DE UMA PA'.center(30))
print ('=' * 30)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range (1, 11):
    print ((a1 + (c-1) * r), end=' => ')
print ('ACABOU')