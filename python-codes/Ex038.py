## escrever um programa que lê dois numeros, um maior, um menor, ou são iguais

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print('O número {} é maior que o número {}'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que o número {}'.format(n2, n1))
else:
    print('Os números são idênticos!!')