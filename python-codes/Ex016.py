# ler um número real e mostrar apenas a parte inteira

from math import trunc
num = float(input('Digite um número real: '))

print('A parte inteira do número {} é {}'.format(num, trunc(num)))