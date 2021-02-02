'''
simple string excersice with names;
'''
nome = str(input('Digite seu nome completo: ')).rstrip().lstrip().split()

print('Muito prazer em te conhecer!!')
print('Seu primeiro nome é {}!'.format(nome[0]))
print('Seu último nome é {}!'.format(nome[len(nome)-1]))

