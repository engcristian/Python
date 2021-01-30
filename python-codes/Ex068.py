from random import randint
from time import sleep
cont = 0
while True:
    cpu = randint(0, 5)
    p1 = str(input('PAR ou ÍMPAR? [P/I]')).strip().lower()
    val = int(input('Um valor entre 0 e 5!!'))
    s = cpu + val
    if p1 == 'i':
        print('Você escolheu ÍMPAR!')
        sleep(1.5)
        print('Então eu fico com PAR!')
        sleep(1.5)
        print('Do lá sí... JÁ!!')
        sleep(2.5)
        if s % 2 == 0:
            print(f'VOCÊ PERDEU!! Você colocou {val} e eu coloquei {cpu}, logo {s} é Par!')
            break
        else:
            print(f'VOCÊ GANHOU!! Você colocou {val} e eu coloquei {cpu}, logo {s} é Ímpar!')
            cont += 1
    elif p1 == 'p':
        print('Você escolheu PAR!')
        sleep(1.5)
        print('Então eu escolho ÍMPAR!')
        sleep(1.5)
        print('Do lá sí... JÁ!!')
        sleep(2.5)
        if s % 2 == 0:
            print(f'VOCÊ GANHOU!! Você colocou {val} e eu coloquei {cpu}, logo {s} é Par!')
            cont += 1
        else:
            print(f'VOCÊ PERDEU!! Você colocou {val} e eu coloquei {cpu}, logo {s} é Ímpar!')
            break
print(f'Você me venceu {cont} vezes!!')
