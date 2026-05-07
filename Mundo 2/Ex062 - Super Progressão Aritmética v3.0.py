print ('Gerador de PA')
print ('-=' * 10)
p1 = int(input('Primeiro termo: '))
r = int(input("Razão da PA: "))
i = 0
t = 10
qntd = 0
while i < t:
    print (f'{p1 + (i * r)}', end=' -> ')
    if i == t-1:
        print ('PAUSA')
        t += int(input('Quantos termos você quer mostrar a mais? '))
    i += 1
    qntd += 1
print (f'Progressão finalizada com {qntd} termos mostrados')