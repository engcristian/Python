'''
Read an angle and show its sin and cos.
'''
from math import radians, cos, sin, tan
ang = float(input('Type an angle value: '))
rad = radians(ang)
print('The cosine is {:.2f}\nThe sine {:.2f}\nAnd the tangent is {:.2f}.'.format(cos(rad), sin(rad),tan(rad)))
