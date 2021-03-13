'''
ler o nome, ano de nascimento e carteira de trabalho
cadastrar com idade em um dicionário
se ctps for diferente de 0, o dicionário recebera o ano da contratação e salario
calcular e acrescentar além da idade, com quantos anos a pessoa vai se aposentar.
(35 anos contribuindo)
Ex.
>>nome tem o valor cristian
>>idade tem o valor 29
ctps .......... 1234
contratação...........2014
salário ............ 1240
aposentadoria......... x
'''
from datetime import date

hoje = date.today()

reg = {}

nome = str(input('Nome: '))
reg['Nome'] = nome
ano = int(input('Ano de nascimento: '))
idade = (hoje.year - ano)
reg['Idade'] = idade
ctps = int(input('CTPS: '))
reg['CTPS'] = ctps
salario = float(input('Salário: '))
print(reg)