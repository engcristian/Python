""" ler 3 comprimentos de reta, e saber se podem ou não formar um triângulo."""
from math import pow, sqrt
print('-='*20)
print('       Analisador de Triânngulos')
print('-='*20)

a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))

if a < b + c and b < c + a and c < a + b:
    print('Os segmentos FORMAM um triângulo!')
else:
    print('Os segmentos NÃO FORMAM um triângulo!')