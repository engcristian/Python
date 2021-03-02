'''
Read numbers and put in a list
one list will have the EVEN numbers
the other will have the ODD ones
SHow the result
'''
odd_list = []
even_list = []
num = int(input('Type a number: '))
if num%2 == 0:
    even_list.append(num)
elif num%2 != 0:
    odd_list.append(num)
while True:
    opt =  str(input('Do you want to keep adding numbers? [Y/N]: ')).lower()
    if 'y' in opt: 
        num = int(input('Type a number: '))
        if num%2 == 0:
            even_list.append(num)
        elif num%2 != 0:
            odd_list.append(num)
    elif 'n' in opt:
        print(f'The list is: {sorted(even_list + odd_list)}')
        print(f'The EVEN list: {sorted(even_list)}')
        print(f'The ODD list: {sorted(odd_list)}')
        break
    else:
        print('Sorry, the options are Y - yes or N - no.')