#ler o ano de nascimento de 7 pessoas e no final mostrar quantas atingiram a maior idade e quantas ainda não
from datetime import date
hj = date.today().year
s = 0
s2 = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if hj - ano >= 21:
        s += 1
    else:
        s2 += 1
print('O número de pessoas que estão na maior idade é: {}.'.format(s))
print('O número de pessoas que não estão na maior idade é: {}.'.format(s2))