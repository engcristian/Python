'''
Mega sena
vai perguntar quantos jogos serão gerados
sortear seis numeros entre 1 e 60 para cada jogo
cadastrar tudo em uma lista composta
'''
from random import randint
geral = []
game = []
n = 6
jogada = int(input('Jogadas: '))
while True:
    for j in range(jogada):  
        for a  in range (n):
            num = randint(1,60)
            geral.append(num)
            sorted(geral)
               
    splited = [geral[i::jogada] for i in range(jogada)]
    order = sorted(splited)
    print(order)
    break

    
    
