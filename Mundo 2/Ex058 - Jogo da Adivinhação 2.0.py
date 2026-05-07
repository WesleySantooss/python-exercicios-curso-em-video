from random import randint
n = randint(0, 10)

print ("Sou seu computador...")
print ("Acabei de pensar em um número entre 0 e 10.")
print ("Será que você consegue adivinhar qual foi?")

qntdp = 1
nu = int(input("Qual é seu palpite? "))
while nu != n:
    if nu < n:
        print ("Mais... Tente mais uma vez")
    else:
        print ("Menos... Tente mais uma vez")
    qntdp += 1
    nu = int(input("Qual é seu palpite? "))
print (f"Acertou com {qntdp} tentativas. Parabéns!")