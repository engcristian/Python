"""
calcular imc
abaixo de 18.5 abaixo do peso
18.5 até 25 peso ideal
25 até 30 sobrepeso
30 até 40 obesidade
acima de 40 obesidade mórbida

"""
peso = float(input('Informe o peso em Kg: '))
alt = float(input('Informe a altura em metros: '))
imc = peso/(alt ** 2)

if imc < 18.5:
    print('IMC = {:.2f} => ABAIXO DO PESO.'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC = {:.2f} => PESO IDEAL.'.format(imc))
elif 25 <= imc <= 30:
    print('IMC = {:.2f} => SOBREPESO.'.format(imc))
elif 30 < imc <= 40:
    print('IMC = {:.2f} => OBESIDADE.'.format(imc))
elif imc > 40:
    print('IMC = {:.2f} => OBESIDADE MÓRBIDA.'.format(imc))
