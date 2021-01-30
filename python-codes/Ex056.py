nomemaisvelho = ''
maioridade = 0
média = 0
soma = 0
totmulher = 0
for p in range(1, 5):
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: '))
    soma += idade
    if p == 1 and sexo in 'Mm': # o primeiro registro recebe os valores de base
        maioridade = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridade: # se o valor do segundo ou posterior for acima do primeiro registro, então ele recebe o novo valor
        maioridade = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20: # se o sexo for F, e a idade menor que 20
        totmulher += 1
média = soma /4
print('A média de idade registrada é {} anos'.format(média))
print('O homem mais velho se chama {} e tem {} anos de idade.'.format(nomemaisvelho, maioridade))
print('Ao todo são {} o número de mulheres que estão abaixo de 20 anos.'.format(totmulher))
