# refazer o desafio 9 da tabuada utilizando o laço for
n = int(input('Digite um valor: '))
print('-'*12)
for c in range(1, 11):
   print('{} x {} = {}'.format(n, c, c*n))
print(('-'*12))
