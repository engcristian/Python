valor_prod = float(input('Qual é o valor do produto? R$'))
cond = int(input('Escolha a opção de pagamento abaixo:\n'
                 '1- À vista ou cheque, 10% off;\n'
                 '2- À vista no débito ou crédito, 5% off;\n'
                 '3- Parcelado em até 3x, preço normal;\n'
                 '4- Parcelas em 4x ou mais, 20% de juros;'))
desc5 = valor_prod - valor_prod * 5 / 100
desc10 = valor_prod - valor_prod * 10 / 100
juros = valor_prod + valor_prod * 20 / 100

if cond == 1:
    print('O produto de R${} custará R${} à vista ou cheque!'.format(valor_prod, desc10))
elif cond == 2:
    print('O produto de R${} custará R${} à vista no débito ou crédito!'.format(valor_prod, desc5))
elif cond == 3:
    parc3 = int(input('Okay, deseja parcelar em 2x ou 3x?\n'
                      '2- Parcelar 2x;\n'
                      '3- Parcelar 3x;\n'))
    if parc3 == 2:
        print(' O produto custará R${:.2f} parcelado em 2x de R${:.2f}.'.format(valor_prod, valor_prod / 2))
    elif parc3 == 3:
        print(' O produto custará R${:.2f} parcelado 3X de R${:.2f}.'.format(valor_prod, valor_prod / 3))
elif cond == 4:
    parc4 = int(input('Por favor informe o número de parcelas acima de 3x.'))
    print('\n'
    'O produto de R${:.2f} sairá parcelado em {}x de R${:.2f}.\n'
    'Total a prazo sai a R${:.2f}'.format(valor_prod, parc4, juros / parc4, juros))
else:
    print('Opção inválida de pagamento, tente outra.')
