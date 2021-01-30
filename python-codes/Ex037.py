## ler um número inteiro, perguntar se quer binário, octal ou hexadecimal. biblioteca!


print('Olá, para qual base deseja converter seu número?\n'
                '\033[33m1\033[m - Base Binária;\n'
                '\033[33m2\033[m - Base Hexadecimal;\n'
                '\033[33m3\033[m - Base Octal;\n')
op = int(input('Digite o valor numérico decimal:'))
num = int(input('Digite a opção desejada:'))
if num == 1:
    print('O número {} na base Binária é {}.'.format(op, bin(op)[2:]))
elif num == 2:
    print('O número {} na base Hexadecimal é {}'.format(op, hex(op)[2:]))
elif num == 3:
    print('O número {} na base Octal é {}'.format(op, oct(op)[2:]))
else:
    print('Desculpe, mas as opções são 1, 2 ou 3.')




