''' LEr a velocidade de um carro, se 80km+ (foi multado) e a multa vai custar
7 reais por cada km acima do limite (condição simples)'''

speed = int(input('Qual é a velocidade atual do carro?'))

if speed > 80:

    print('Multado!Você excedeu o limite de velocidade que é de 80km/h!\n'
          'Você deverá pagar uma multa de R$ {:.2f}'.format((speed-80)*7))
print('Tenha um bom dia! Dirija com segurança.')