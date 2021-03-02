'''
Simple game to discover the cpu's number is 'thinking'
'''
from random import randint
attempts = 0
p1 = 0
cpu = randint(0, 10)
while p1 != cpu:
    cpu = randint(0, 10)
    p1 = int(input('Try to guess the cpu is thinking beteween 0 and 10!'))
    attempts += 1
    if p1 != cpu:
        print(f'Failed! I was thinking about {cpu}')
print(f'You won! I was thinking about {cpu}.')
print(f'You had {attempts} attempts to get ir right.')
