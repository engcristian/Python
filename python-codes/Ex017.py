# calcular a hipotenusa de um triângulo retângulo
from math import hypot
catop = float(input('Valor do cateto oposto: '))
catadj = float(input('Valor do cateto adjacente: '))
hip = hypot(catop, catadj)
print('A hipotenusa é {:.2f}.'.format(hip))
