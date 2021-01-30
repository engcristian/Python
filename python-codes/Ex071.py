cd50 = cd20 = cd10 = cd1 = rest = 0
valor = int(input('Quanto deseja sacar? R$'))
while True:
    cd50 = valor // 50
    rest = valor - cd50*50
    valor = rest

    cd20 = valor//20
    rest = valor - cd20*20
    valor = rest

    cd10 = valor//10
    rest = valor - cd10*10
    valor = rest

    cd1 = valor//1
    rest = valor - cd1*1
    valor = rest
    if rest == 0:
        break
print(f'Você receberá:\n{cd50} notas de R$50.\n'
      f'{cd20} notas de R$20.\n{cd10} notas de R$10\n{cd1} notas de R$1')