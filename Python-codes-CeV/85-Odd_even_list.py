'''
Type seven numbers, insert in a single list;
This list separates ODD from EVEN numbers;
At the end show all them in crescent order;
E.g. numbers = [[ODD_num],[EVEN_num]]
show separated
'''
odd_even_list = [[],[]]
for i in range(0,7):
    num = int(input(f'Type the {i+1}º number: '))
    if num%2 == 0:
       odd_even_list[0].append(num)
    else:
       odd_even_list[1].append(num)
order = sorted(odd_even_list)
print(f'The odd and even list ordened is : {order}')
print(f'The EVEN list is : {order[1]}')
print(f'The ODD list is : {order[0]}')