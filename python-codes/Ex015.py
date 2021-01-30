# quantidade de km rodado
# quantidades de dias
#calcular preço a pagar sabendo que a diária é R$60 + R$0,15 por km rodado

dias = int(input('Quantos dias alugado?'))
km = float(input('Quantos Km rodados?'))
preço = (60 * dias) + (0.15*km)
print('O total a pagar é de R${:.2f}'.format(preço))
