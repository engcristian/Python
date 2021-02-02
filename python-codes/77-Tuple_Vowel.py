'''
Using tuple to check the vowels in many words.
'''
words = ('Internacional', 'Atletico-MG', 'Flamengo', 'Sao Paulo', 'Fluminense',
        'Palmeiras', 'Gremio','Atletico-PR', 'Ceara SC', 'Corinthians', 'Santos', 
        'Atletico-GO', 'Bragantino', 'Vasco', 'Bahia', 'Sport Recife', 'Fortaleza',
         'Goias', 'Curitiba', 'Botafogo')
for w in words:
    print(f'\nThe word {w.upper()} has the vowels  ', end='')
    for letter in w:
        if letter.lower() in 'aeiou' :
            print(f'{letter.lower()}', end='')