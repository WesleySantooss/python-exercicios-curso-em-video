#Outra forma de resolução!
print ('=' * 30)
print ('10 TERMOS DE UMA PA'.center(30))
print ('=' * 30)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = a1 + (10 - 1) * r

for c in range(a1, decimo + r, r):
    print (c, end=' => ')
print ('ACABOU!')