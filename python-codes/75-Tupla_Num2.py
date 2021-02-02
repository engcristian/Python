
'''
Using tuple to save numbers and show it later
'''

num =  (int(input('Type a number: ')),
        int(input('Type other number: ')),
        int(input('Type another number: ')),
        int(input('Type the last number: ')))
print('The pair numbers were: ',end='')
for n in num:    
    if n % 2 == 0:
        print(n, end=' ')
print(f'\nAltogether {num.count(9)} number(s) 9 were typed. ')
if 3 in num:
    print(f'The first number 3 is on the {num.index(3)+1}ª position.')
else:
    print("The number 3 didn't appeared in any position.")
