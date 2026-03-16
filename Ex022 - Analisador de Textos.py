nome = str(input('Digite seu nome completo: '))
nomemaisculuas = nome.upper()
nomeminusculas = nome.lower()
quantidadeletras = len(nome.replace(' ', '')) #Ou len(nome) - nome.count(' ')
primeironome = (nome.split())[0]

print (f"""Analisando seu nome...
Seu nome em maiúsculas é {nomemaisculuas}
Seu nome em minúsculas é {nomeminusculas}
Seu nome tem ao todo {quantidadeletras} letras
Seu primeiro nome é {primeironome} e ele tem {len(primeironome)} letras""")
#Ou, nome.find(' ')
