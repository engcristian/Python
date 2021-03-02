'''
Generate 5 numbers in a Tuple and show the max and min value
'''
from random import randint
num = (randint(1, 10),randint(1, 10),randint(1, 10),
        randint(1, 10),randint(1, 10))
print(f'The values sorted are: ' , end=' ')
for n in num:     
    print(f' {n} ', end=" ")
print(f'\nThe max value is {max(num)}.')
print(f'The min value is {min(num)}')