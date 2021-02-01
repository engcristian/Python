'''
Analysing a number between 0 to 9999
'''
num = int(input('Type a number between 0 to 9999: '))
unit = num // 1 % 10
ten = num // 10 % 10
hun = num // 100 % 10
tho = num // 1000 % 10
print('Analysing the number {}...'.format(num))
print('The unit: {}'.format(unit))
print('The ten: {}'.format(ten))
print('The hundred: {}'.format(hun))
print('The thousand: {}'.format(tho))
