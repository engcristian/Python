'''
Countdown from 10 to 0 using sleep, FOR and emoji
'''
from time import sleep
import emoji
print('='*5, 'COUNTDOWN', '='*5)
for c in range(10, 0, -1):
    print('{:^33}'.format(c))
    sleep(1)
print(emoji.emojize(':fireworks:'*20))
print('{:^33}'.format('Happy New Year!'))
print(emoji.emojize(':fireworks:'*20))
