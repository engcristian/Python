'''
Type seven numbers, insert in a single list;
This list separates ODD from EVEN numbers;
At the end show all them in crescent order;
E.g. numbers = [[ODD_num],[EVEN_num]]
show separated
'''
odd_list = []
even_list = []
odd_even_list = []

for i in range(0,7):
    num = int(input(f'Type the {i+1}º number: '))
    if num%2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
odd_even_list.append(sorted(even_list))
odd_even_list.append(sorted(odd_list))
print(f'The odd and even list ordened is : {odd_even_list}')