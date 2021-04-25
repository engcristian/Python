'''
Aplicar o ex. 93 para vários jogadores 
Incluir um sistema de vizualização de detalhes do aproveitamento
de cada jogador.
Ex.
<< mesma entrada do ex 93
>> cod nome     gols      total
>> 0 player1      [3,2,0]     5
>> 1 player2      [1,5,0,0,3] 9
>>.....
<< Quer mostrar dados de qual jogador?   0  
>> levantamento do jogador player1
>> no jogo 0 fez 3 gols
>> no jogo 1 fez 1 gols
>> no jogo 2 fez 0 gols
<< quer mostrar dados.......
*** valores fora do range, mostra uma msg de erro, e 999 é condição de parada***
'''
df = []
df_2 = []
info = dict()
info_2 = {}

goals_tot = []

opt =''
num = 0
while True :

    info["name"] = str(input("Player's name: "))

    gender = str(input('Gender: [M/F] ')).lower()

    if 'm' in gender:

        gen_1 = 'he'

        gen_2 = 'him'

    if 'f' in gender:

        gen_1 = 'she'

        gen_2 = 'her'

    info["matches"] = int(input(f'How many matches did {gen_1} play? '))

    for i in range(info['matches']):          

        goals_tot.append(int(input(f'How many goals at the {i+1}º match: ')))

        info['goals per match'] = goals_tot

        info['total goals']= sum(goals_tot)

        
    
    df.append(info)
    info_2 = info.copy()
    del info_2['matches']
    df_2.append(info_2)
    
    num = (int(input('''Do you want to keep?
                            0 - No
                            1 - Yes ''')))
    if num == 0:
        break
print('ID_NOME____GOLS____TOTAL')
for i in df_2:
    for p in i.values():
        print(f'{p}',end='' )








