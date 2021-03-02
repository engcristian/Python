'''
Reading a decimal number and asking in which bases want to convert the number to:
Hexadecimal, Binary or Octal
'''
print('Hello, which base do you want to convert your number to??\n'
                '\033[33m1\033[m - Binary base;\n'
                '\033[33m2\033[m - Hexadecimal base;\n'
                '\033[33m3\033[m - Octal base;\n')
num = int(input('Type any decimal number: '))
option = int(input('Select the option above: '))
if option == 1:
    print(f'The number {num} on Binary base is {bin(num)[2:]}.')
elif option == 2:
    print(f'The number {num} on Hexadecimal base is {hex(num)[2:]}')
elif option == 3:
    print(f'The number {num} on Octal base is {oct(num)[2:]}')
else:
    print('Sorry, but the options are 1, 2 or 3.')




