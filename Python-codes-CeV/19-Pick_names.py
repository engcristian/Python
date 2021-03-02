'''
Using choice from the random lib, it's able to choose a name randomly
'''
from random import choice

n1 = str(input('First name: '))
n2 = str(input('Second name: '))
n3 = str(input('Third name: '))
n4 = str(input('Fourth name: '))
name_list = [n1, n2, n3, n4 ]
name = choice(name_list)
print('The choosen name was {}.'.format(name))
