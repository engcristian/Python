'''
Arithmetic progression using a flag to stop the program
'''
first_term = int(input('Type the first term of this A.P: '))
reason = int(input('Type the reason of this A.P: '))

count = 1
add = 10
total = 0
while add != 0:
    total = total + add
    while count <= total:
        print(f'{first_term} ► ', end=' ')
        first_term += reason
        count += 1
    print('Type [0] to stop')
    add = int(input('How many elements do you wish to insert more?'))
print(f'Were calculated {total} terms.')
print('END')

