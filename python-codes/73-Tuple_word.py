'''
Brasileirão 2020/2021 Serie A table: will show all teams, the five firsts, the four lasts
and Palmeiras' position (as default)
'''
clubs = ('Internacional', 'Atléetico-MG', 'Flamengo', 'São Paulo', 'Fluminense',
        'Palmeiras', 'Grêmio','Atlético-PR', 'Ceará SC', 'Corinthians', 'Santos', 
        'Atlético-GO', 'Bragantino', 'Vasco', 'Bahia', 'Sport Recife', 'Fortaleza',
         'Goiás', 'Curitiba', 'Botafogo')
print(f'The clubs are : {clubs}')
print(f'The five firsts are: {clubs[0:5]}')
print(f'The four lasts are: {clubs[-4:]}')
print(f"Palmeiras is on the {clubs.index('Palmeiras')+1}ª position.")