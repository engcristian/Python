'''
A dice game beteween 4 players, that will show at the end the results and also show up a
rank of the players.
'''
from random import randint
import operator

count = 0
game = {}
players = 4

for j in range(players):
    dice = randint(1,6)
    game[f'player_{j+1}']= dice    
print('-='*30)
for k, v in game.items():
    
    print(f'The  {k} got {v}')
print('-='*30)
for k, v in sorted(game.items(), key=operator.itemgetter(1), reverse = True):
    count += 1
    print(f'{count}º place: {k} with {v}')
print('-='*30)