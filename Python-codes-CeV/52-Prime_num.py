'''
Checking if the numbers is a prime number
'''

count = 0
num = int(input('Type a number: '))
for c in range(1, num+1):
    if num % c == 0:
        count += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print(f'\n\033[mO número {num} foi dividido {count} vezes.')
if count == 2:
    print('The number is prime.')
else:
    print("The number isn't prime.")