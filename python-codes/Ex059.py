from time import sleep
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

menu = 0
while menu != 5:
    print(''' 
            1 - somar
            2 - multiplicação
            3 - maior
            4 - novos números
            5 - sair do programa
            ''')
    menu = int(input('Agora escolha uma das opções do menu acima: '))
    if menu == 1:

        print('A soma de {} com {} é: {}.'.format(n1, n2, n1 + n2))
    elif menu == 2:

        print('A multiplicação entre {} e {} é: {}.'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:

            print('O número {} é maior que o número {}.'.format(n1, n2))
        elif n2 > n1:

            print('O número {} é maior que o número {}.'.format(n2, n1))
        else:

            print('Os números são iguais.')
    elif menu == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    else:
        print('O valor do menu está incoreto!')

print('Finalizando...')
sleep(1)
print('Volte Sempre!')