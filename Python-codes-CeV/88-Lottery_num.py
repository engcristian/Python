'''
Mega sena
vai perguntar quantos jogos serão gerados
sortear seis numeros entre 1 e 60 para cada jogo
cadastrar tudo em uma lista composta
'''
from random import randint
my_game = [1,5,17,16,39,44]
num_list = []
game_list = []
amount = int(input('How many games do you want? '))
total = 1
tot = 0
while total <= amount:
    count = 0
    while True:
        num = randint(1,60)
        if num not in num_list:
            num_list.append(num)
            count += 1
        if count >= 6:
            break
    num_list.sort()
    game_list.append(num_list[:])
    num_list.clear() 
    total += 1   

for i, l in enumerate(game_list):
    print(f'{i+1}º game = {l}')
    if l == my_game:
        
        tot +=1
print(tot)