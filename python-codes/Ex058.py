from random import randint
t = 0
p1 = 0
cpu = randint(0, 10)
while p1 != cpu:
    cpu = randint(0, 10)
    p1 = int(input('Tente descobrir qual número estou pensando entre 0 e 10:'))
    t += 1
    if p1 != cpu:
        print('Errou ! Estava pensando no {}'.format(cpu))
print('Você ganhou! Estava pensando no número {}.'.format(cpu))
print('Você teve {} tentativas até acertar.'.format(t))
