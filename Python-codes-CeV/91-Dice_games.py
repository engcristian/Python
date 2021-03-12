'''
Quatro jogadores jogam um dado e tenham resultados aleatórios
guardar os valores em um dicionário 
colocar o dicionário em orgem**
sabendo que o vencedor tirou o maior número do dado**
Ex.:
>> o jogador1 tirou 6
>> o jogador2 tirou 4
...
1º lugar: jogador1 com 6 
2º lugar: jogador2 com4
...

'''
from random import randint

game = {}
jogador = 4

for j in range(jogador):
    jogada = randint(1,6)
    game[f'Jogador{j+1}']= jogada
    

for k, v in game.items():
    print(f'O jogador {k} obteve o valor {v}')
print(f'O vencedor foi o jogador {}')