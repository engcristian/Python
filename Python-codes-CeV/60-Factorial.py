'''
Factorial of a number typed using while
'''
num = int(input('Type a number: '))
factorial = 1
while num > 0:
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    factorial *= num
    num -= 1
print(factorial)
