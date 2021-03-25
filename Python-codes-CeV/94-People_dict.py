'''
Ler nome, sexo e idade de várias pessoas
guardar em um dicionário
e todos os dicts tem uma lista.
A. quantas pessoas foram cadastradas (cont)
B. média de idade das pessoas
C. uma lista com todas as mulheres
D. uma lista com as pessoas com idade acima da média
Ex.
<< nome
<< sexo
<< idade
<< opt
>> o grupo tem x pessoas
>> a média de idade é y
>> as mulheres cadastradas foram : ana
>> lista das pessoas acima da média
>> nome = cristian; sexo= M; idade = 29;
>> nome = ana; sexo=F; idade = 25;

'''
reg = {}
cad = []
idade = []
media = 0
mulheres = []
acima_media = []
cont_p = 0


while True:

    
    reg['nome'] = str(input('nome: '))

    reg['sexo'] = str(input('sexo M/F: ')).lower()

    reg['idade'] = int(input('idade: '))
    if reg['idade'] > media :
        acima_media.append(reg['nome'])
        acima_media.append(reg['sexo'])
        acima_media.append(reg['idade'])
    
    cont_p +=1
    cad.append(reg.copy())
    idade.append(reg['idade'])
    media = sum(idade)//len(idade)
    if reg['sexo'] == 'f':
        mulheres.append(reg['nome'])
    opt = str(input('Deseja continuar? Y/N  ')).lower()
    if 'n' in opt:
        break


num = acima_media[2]
acima = acima_media.copy()
if num < media:
    for i in range(3):
        acima.pop(0)
        
print(acima_media)
print(f'Total de pessoas cadastradas: {cont_p}')
print(f'A média de idade das pessoas cadastradas: {media} anos.')
print(f'Mulheres cadastradas: {mulheres}')
print(acima)



