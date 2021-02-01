'''
Now using shuffle from random lib to set the names in order
'''
from random import shuffle
n1 = str(input('Type the first name: '))
n2 = str(input('Type the second name: '))
n3 = str(input('Type the third name: '))
n4 = str(input('Type the fourth name: '))

name_list = [n1, n2, n3, n4 ]
shuffle(name_list)
print(' The order of names is: ')
print(name_list)