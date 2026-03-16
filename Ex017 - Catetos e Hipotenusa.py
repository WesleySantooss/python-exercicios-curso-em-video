import math
from math import hypot
cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(cat1, cat2)
print (f'A hipotenusa vai medir {hip:.2f}')




#Outra forma:

cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))
hip = ((cat1 ** 2) + (cat2 ** 2)) ** 0.5
print (f'A hipotenusa vai medir {hip:.2f}')
