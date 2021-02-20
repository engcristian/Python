'''
Reading 5 numbers and including them in a list, and at the end show the lower
the higher and in wich position are they.
'''
my_list = list()
count = 0

for num in range(0,5):
    my_list.append(input(f'Type the {num+1}º number: '))

print(f'The list created is: {my_list}')
print(f'The lower value is {min(my_list)}, and it is in the {my_list.index(min(my_list))+1}º position.')

print(f'The higher value is {max(my_list)}, and it is in the {my_list.index(max(my_list))+1}º position.')