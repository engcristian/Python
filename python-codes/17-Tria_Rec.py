'''
Importing hypot from math lib to calculate the hypotenuse of a triangle
'''
from math import hypot
op_side = float(input('Opposite side value: '))
ad_side = float(input('Adjacent side value: '))
hip = hypot(op_side, ad_side)
print('The hypotenuse is {:.2f}.'.format(hip))
