'''
Mega sena
vai perguntar quantos jogos serão gerados
sortear seis numeros entre 1 e 60 para cada jogo
cadastrar tudo em uma lista composta
'''
from random import randint
#game = []
game = []
jogada = int(input('Jogadas: '))
while True:

    for j in range(jogada):
        for i  in range (6):
            num = randint(1,60)
            game.append(num)
    break
print(game)
