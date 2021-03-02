'''
Reading two numbers and show the higher number, if they are the same, it will show 'both'.
'''
n1 = float(input('Type a number: '))
n2 = float(input('Type other number: '))

if n1 > n2:
    print(f'The number {n1} is higher than the {n2}')
elif n2 > n1:
    print(f'The number {n2} is higher than the {n1}')
else:
    print('The numbers are the same !!')