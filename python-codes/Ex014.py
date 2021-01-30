celsius = float(input('Informe a temperatura em ºC:'))
farenheit = 32 + celsius*(9/5)
kelvin = 273.15 + celsius
print('A temperatura {:.1f}ºC corresponde a {:.2f} ºF'.format(celsius, farenheit))
print('A temperatura {:.1f}ºC corresponde a {:.2f} K'.format(celsius, kelvin))
