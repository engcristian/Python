'''

'''
name_older = ''
adulthood = 0
average = 0
sum = 0
tot_weman = 0
for p in range(1, 5):
    name = str(input('name: '))
    age = int(input('age: '))
    gender = str(input('gender [M/F]: '))
    sum += age
    if p == 1 and gender in 'Mm': # o primeiro registro recebe os valores de base
        adulthood = age
        name_older = name
    if gender in 'Mm' and age > adulthood: # se o valor do segundo ou posterior for acima do primeiro registro, então ele recebe o novo valor
        adulthood = age
        name_older = name
    if gender in 'Ff' and age < 20: # se o gender for F, e a age menor que 20
        tot_weman += 1
average = sum /4
print('A average de age registrada é {} anos'.format(average))
print('O homem mais velho se chama {} e tem {} anos de age.'.format(name_older, adulthood))
print('Ao todo são {} o número de mulheres que estão abaixo de 20 anos.'.format(tot_weman))
