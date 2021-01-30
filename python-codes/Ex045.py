# criar um jokenpô entre você e a máquina.

import random
from time import sleep

print('-=' * 12, ' JOKENPÔ ', '-=' * 12)
print('Escolha uma das opções abaixo:\n'
      '\033[1;37m1- PEDRA\033[m;\n'
      '\033[1;30m2- PAPEL;\033[m\n'
      '\033[1;33m3- TESOURA;\033[m')
print('-=' * 30)
p1 = int(input())

lista = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = random.choice(lista)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
print('=-'*20)
if p1 == 1:

    print('Você jogou: >>   \033[1;37mPEDRA\033[m      <<')
elif p1 == 2:
    print('Você jogou: >>   \033[1;30mPAPEL\033[m      <<')
elif p1 == 3:
    print('Você jogou: >>   \033[1;33mTESOURA\033[m    <<')


if cpu == 'PEDRA' and p1 == 3:
    print('CPU jogou: >>    \033[1;37mPEDRA\033[m      <<')
    print('{:^50}'.format('\033[1;31mVocê PERDEU!\033[m'))
elif cpu == 'PAPEL' and p1 == 1:
    print('CPU jogou: >>    \033[1;30mPAPEL\033[m      <<')
    print('{:^50}'.format('\033[1;31mVocê PERDEU!\033[m'))
elif cpu == 'TESOURA' and p1 == 2:
    print('CPU jogou: >>    \033[1;33mTESOURA\033[m    <<')
    print('{:^50}'.format('\033[1;31mVocê PERDEU!\033[m'))


elif cpu == 'PEDRA' and p1 == 1 or cpu == 'PAPEL' and p1 == 2 or cpu == 'TESOURA' and p1 == 3:
    print('CPU jogou: >>    \033[1;36m{}\033[m    <<'.format(cpu))
    print('{:^50}'.format('\033[1;34mEMPATOU !!\033[m'))

else:
    print('CPU jogou: >>    \033[1;36m{}\033[m    <<'.format(cpu))
    print('{:^50}'.format('\033[1;32mVOCÊ GANHOU!!\033[m'))
print('-='*20)