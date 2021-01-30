'''computador pensar entre 0 e 5
e o usuário deve descobrir o valor e deverá
ser mostradona tela se venceu ou perdeu (venceu, perdeu)'''

from random import randint
from time import sleep
num = int(input('Tente descobrir qual número estou pensando entre 0 e 5 !!'))
num_pc = randint(0, 5)
print('LOADING')
sleep(3)

if num == num_pc:
    print(" Você ganhou! Eu estava pensando no número {}!!".format(num_pc))
else:
    print('Errou!! O número que eu pensei foi o {}!'.format(num_pc))