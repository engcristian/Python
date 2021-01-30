# refazer o ex 51, lendo o termo e a razão de uma PA, usando o while

t1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = t1
cont = 1
while cont <= 10:
    print('{} ► '.format(n), end=' ')
    n = n + r
    cont += 1

