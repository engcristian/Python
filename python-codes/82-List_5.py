'''
Read numbers and put in a list
one list will have the EVEN numbers
the other will have the ODD ones
SHow the result
'''
odd_list = []
even_list = []

while True:
    num = int(input('Type a number: '))
    if num%2 == 0:
        even_list.append(num)
    elif num%2 != 0:
        odd_list.append(num)
    if num == -0:
        even_list.pop()
        print(f'The EVEN list: {even_list}')
        print(f'The ODD list: {odd_list}')
        break