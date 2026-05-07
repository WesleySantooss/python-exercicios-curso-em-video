from time import sleep
opcao = 4
while opcao != 5:
    if opcao == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    print ("=-=" * 10)
    sleep(0.5)
    print ("    [ 1 ] somar\n"
           "    [ 2 ] multiplicar\n"
           "    [ 3 ] maior\n"
           "    [ 4 ] novos números\n"
           "    [ 5 ] sair do programa")
    opcao = int(input(">>>>> Qual é a sua opção? "))
    if opcao == 1:
        print (f'A soma entre {n1} + {n2} é {(n1+n2)}')
    elif opcao == 2:
        print (f'O resultado de {n1} x {n2} é {(n1*n2)}')
    elif opcao == 3:
        if n1 > n2:
            print (f'Entre {n1} e {n2} o maior valor é {n1}')
        else:
            print (f'Entre {n1} e {n2} o maior valor é {n2}')
    elif opcao == 4:
        print ("Informe os números novamente: ")
    elif opcao != 5:
        print ('Opção inválida. Tente novamente')
print ('Finalizando...')
print ('=-=' * 10)
sleep(2)
print ("Fim do programa! Volte sempre!")