'''
Reading the car's speed and checking the fee
'''
speed = int(input("What is the actual car's speed?"))

if speed > 80:

    print('Multado!Você excedeu o limite de velocidade que é de 80km/h!\n'
          'Você deverá pagar uma multa de R$ {:.2f}'.format((speed-80)*7))
print('Tenha um bom dia! Dirija com segurança.')