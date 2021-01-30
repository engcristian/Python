frase = str(input('Digite qualquer frase: ')).strip().lower()


print('A letra A apareceu {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))