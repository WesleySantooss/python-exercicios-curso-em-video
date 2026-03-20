import random
import time

n = random.randint(0, 6)
print ('-=-' * 20)
print ('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print ('-=-' * 20)

numero = int(input('Em que número pensei? '))
print ('Processando...')
time.sleep(2)

if numero == n:
    print ('PARABÉNS! Você conseguiu me vencer!')
else:
    print (f'GANHEI! Eu pensei no número {n} e não no {numero}!')