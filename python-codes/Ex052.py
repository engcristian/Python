#ler um número inteiro, e saber se ele é primo (for)
cont = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes.'.format(n, cont))
if cont == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')