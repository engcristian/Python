'''
Playing a JO_KEN_PO game against the CPU with infinite loop and scores
'''
import random
from time import sleep
score_p1 = 0
score_cpu = 0
while True:
    print('-=' * 12, ' JO-KEN-PO ', '-=' * 12)
    print('Choose an option below:\n'
        '\033[1;37m1- STONE\033[m;\n'
        '\033[1;30m2- PAPER;\033[m\n'
        f'\033[1;33m3- SCISSORS;\033[m{score_cpu:30} CPU points\n'
        f'\033[1;35m4- END GAME;\033[m{score_p1:30} P1 Points')
    print('-=' * 30)
    p1 = int(input())
    if p1 == 4:
        break
    lista = ('STONE', 'PAPER', 'SCISSORS')
    cpu = random.choice(lista)

    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    print('=-'*20)
    if p1 == 1:

        print('You played: >>   \033[1;37mSTONE\033[m      <<')
    elif p1 == 2:
        print('You played: >>   \033[1;30mPAPER\033[m      <<')
    elif p1 == 3:
        print('You played: >>   \033[1;33mSCISSORS\033[m    <<')


    if cpu == 'STONE' and p1 == 3:
        print('CPU played: >>    \033[1;37mSTONE\033[m      <<')
        print('{:^50}'.format('\033[1;31mYou LOSE!\033[m'))
        score_cpu += 1
    elif cpu == 'PAPER' and p1 == 1:
        print('CPU played: >>    \033[1;30mPAPER\033[m      <<')
        print('{:^50}'.format('\033[1;31mYou LOSE!\033[m'))
        score_cpu += 1
    elif cpu == 'SCISSORS' and p1 == 2:
        print('CPU played: >>    \033[1;33mSCISSORS\033[m    <<')
        print('{:^50}'.format('\033[1;31mYou LOSE!\033[m'))
        score_cpu += 1
    elif cpu == 'STONE' and p1 == 1 or cpu == 'PAPER' and p1 == 2 or cpu == 'SCISSORS' and p1 == 3:
        print('CPU played: >>    \033[1;36m{}\033[m    <<'.format(cpu))
        print('{:^50}'.format('\033[1;34mDRAW !!\033[m'))
    else:
        print('CPU played: >>    \033[1;36m{}\033[m    <<'.format(cpu))
        print('{:^50}'.format('\033[1;32mYou WIN!!\033[m'))
        score_p1 += 1
    print('-='*20)
print("Thank you for playing with me, you're a great player!!")
print(f'You did {score_p1} points against me, do your best next time!!')