'''
Analyzing two numbers by a simple option, in an infinite looping using a True flag to stop it
'''

from time import sleep # Used to get a dalay while finish the program.
num1 = float(input('Type a number: '))
num2 = float(input('Type another number: '))

option = 0
while True:
    print('''
            1 - Sum
            2 - Multiplication
            3 - Higher number
            4 - New numbers
            5 - Exit the program
            ''')
    option = int(input('Now choose one option above: '))
    print('-'*50)
    if option == 1:

        print(f'The sum of {num1} and {num2} is: {num1+num2}.')
    elif option == 2:

        print(f'The multiplication beteween {num1} and {num2} is: {num1*num2}.')
    elif option == 3:
        if num1 > num2:

            print(f'The number {num1} is higher than the number {num2}.')
        elif num2 > num1:

            print(f'The number {num2} is higher than the number {num1}.')
        else:

            print('The numbers are equal.')
    elif option == 4:
        num1 = float(input('Type a value: '))
        num2 = float(input('Type other value: '))
    elif option == 5:
        break
    else:
        print('The option is invalid!')
    print('-'*50)

print('Finishing...')
sleep(1)
print('Check back often!')