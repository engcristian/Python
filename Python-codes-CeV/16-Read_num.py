'''
Just read a float number and show the int part.
'''
from math import trunc
num = float(input('Type a real number: '))
print('The int number from {} is {}'.format(num, trunc(num)))