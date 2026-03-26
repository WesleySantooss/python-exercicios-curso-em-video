n = int(input('Digite um número: '))
divisor = 0
for c in range (1, n + 1):
    if n % c == 0:
        print (f'\033[:33m{c}', end=' ')
        divisor += 1
    elif n % c != 0:
        print (f'\033[:31m{c}', end=' ')
print (f'\n\033[mO número {n} foi divisível {divisor} vezes')
if divisor > 2:
    print (f'E por isso ele NÃO É PRIMO!')
else:
    print (f'E por isso ele É PRIMO!')