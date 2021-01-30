n = 0
s = 0
q = 0
print('Digite 999 para obte o resultado do programa;')
n = int(input('Digite um número: '))
while n != 999:
    s = s + n
    q = q + 1
    n = int(input('Digite um número: '))
print('A soma dos números digitados foi {}.'.format(s))
print('A quantidade de números digitados foram {} números.'.format(q))
print('Fim')

