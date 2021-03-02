'''
CPU will chose a number and the user must discover it in one chance, without
use rep structure.
'''
from random import randint
from time import sleep
num = int(input("Try to discover the number I'm thinking !!"))
num_cpu = randint(0, 5)
print('LOADING')
sleep(3)
if num == num_cpu:
    print(" You WON!! I was thinking about number {num_cpu}!!".format(num_cpu))
else:
    print('Missed!! The number I was thinking was {num_cpu}!'.format(num_cpu))