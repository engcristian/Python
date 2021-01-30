''' perguntar a distância da viagem em km, calcular o preço da passagem
0.50 centavos por km p/ viagens de até 200km, e 0.45 centavos para v>200KM'''

distância = int(input('Qual é a distância da viagem em km?'))
print('Você está prestes a fazer uma viagem de {:.1f} km'.format(distância))
if distância <= 200:

    print('O valor da sua passagem é de R$ {:.2f}'.format(distância*0.5))
else:
    print('O valor da sua passagem é de R$ {:.2f}'.format(distância*0.45))
