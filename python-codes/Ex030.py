''' ler um número inteiro, se é par ou impar'''

num = int(input('Digite um número:'))


if num%2 == 1:
    print('O número {} é IMPAR!'.format(num))
else:
    print('O número {} é PAR!'.format(num))