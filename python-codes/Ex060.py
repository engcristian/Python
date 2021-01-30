num = int(input('Digite um número: '))
fat = 1
while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')
    fat *= num
    num -= 1
print(fat)
