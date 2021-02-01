'''
Convert Celsius to Farenheit and Kelvin.
'''

celsius = float(input('Put the temperature in °C:'))
farenheit = 32 + celsius*(9/5) # how to convert Celsius to Farnheit
kelvin = 273.15 + celsius # how to convert Celsius to Kelvin
print('The temperature of {:.1f}°C correspond to {:.2f} °F'.format(celsius, farenheit))
print('The temperature of {:.1f}°C correspond to {:.2f} K'.format(celsius, kelvin))
