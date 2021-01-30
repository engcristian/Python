""" LEr a idade de um atleta e informar sua categoria
até 9 = mirim
até 14 = infantil
até 19 = junior
até 20 = sênior
acima = master
"""
from datetime import date
age = int(input('Informe o ano de nascimento do atleta: '))
hj = date.today().year
ano = hj - age

if ano <= 9:
    print('O atleta tem {} anos e se encaixa na categoria \033[32mMIRIM\033[m.'.format(ano))
elif ano <= 14:
    print('O atleta tem {} anos e se encaixa na categoria \033[32mINFANTIL\033[m.'.format(ano))
elif ano <= 19:
    print('O atleta tem {} anos e se encaixa na categoria \033[32mJUNIOR\033[m.'.format(ano))
elif ano <= 25:
    print('O atleta tem {} anos e se encaixa na categoria \033[32mSÊNIOR\033[m.'.format(ano))
else:
    print('O atleta tem {} anos e se encaixa na categoria \033[32mMASTER\033[m.'.format(ano))