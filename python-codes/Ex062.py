t1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = t1
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ► '.format(n), end=' ')
        n = n + r
        cont += 1
    print('Pausa')
    mais = int(input('Deseja inserir mais termos?'))
print('foram calculados {} termos.'.format(total))
print('FIM')

