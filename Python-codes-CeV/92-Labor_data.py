'''
Make a simple registration of a labor data, inserting all in a dict and showing also other
informations. 
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
if ctps > 0 :

    ano_contrato = int(input('Ano da contratação: '))
    salario = float(input('Salário: '))
    reg['Ano contratação'] = ano_contrato
    reg['Salário'] = salario
    apo = 35 - (hoje.year- ano_contrato)
    reg['Aposentadoria em:'] = apo
print('-='*15)
for k, v in reg.items():
    print(f'{k}: {v}')
print('-='*15)