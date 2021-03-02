'''
(Inclomplete) ODD or EVEN game against the cpu, using numbers beteween 0 and 5.
'''
from random import randint #making the cpu pic a random number
from time import sleep #just to give an interaction for the game
count = 0
while True:
    cpu = randint(0, 5)
    #the imput is a string, so clear all possible error chances
    p1 = str(input('PAR ou ÍMPAR? [O/E]')).strip().lower()
    value = int(input('Um valueor entre 0 e 5!!'))   
    add = cpu + value 
    if p1 in 'o':
        print('Você escolheu ÍMPAR!')
        sleep(1.5)
        print('Então eu fico com PAR!')
        sleep(1.5)
        print('Do lá sí... JÁ!!')
        sleep(2.5)
        if add % 2 == 0:
            print(f'VOCÊ PERDEU!! Você colocou {value} e eu coloquei {cpu}, logo {add} é Par!')
            break
        else:
            print(f'VOCÊ GANHOU!! Você colocou {value} e eu coloquei {cpu}, logo {add} é Ímpar!')
            count += 1
    elif p1 in 'e':
        print('Você escolheu PAR!')
        sleep(1.5)
        print('Então eu escolho ÍMPAR!')
        sleep(1.5)
        print('Do lá sí... JÁ!!')
        sleep(2.5)
        if add % 2 == 0:
            print(f'VOCÊ GANHOU!! Você colocou {value} e eu coloquei {cpu}, logo {add} é Par!')
            count += 1
        else:
            print(f'VOCÊ PERDEU!! Você colocou {value} e eu coloquei {cpu}, logo {add} é Ímpar!')
            break

print(f'Você me venceu {count} vezes!!')
