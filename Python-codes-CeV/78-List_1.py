'''
Reading 5 numbers and including them in a list, and at the end show the lower
the higher and in wich position are they.
'''
#creating an empty list;
my_list = []
count = 0
#Iserting 5 numbers in a list, so doing  for in a range 0 to 5;
for num in range(0,5):
    my_list.append(int(input(f'Type the {num+1}º number: '))) #append to add at the end;
#looking for the max and minimun value;
max_num = max(my_list)
min_num = min(my_list)

print(f'The list created is: {my_list}')
print(f'The lower value is {min_num}, and it is in the position: ',end='')
for i, v in enumerate(my_list):
    if v == min_num:
        print(f'{i}...',end='')
print(f'\nThe higher value is {max_num}, and it is in the position: ',end='')
for i, v in enumerate(my_list):
    if v == max_num:
        print(f'{i}...', end='')