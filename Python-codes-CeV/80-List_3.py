'''
Insert 5 numbers in the right position without using .sort()
Then show the list orderned
'''
my_list = []
for c in range(0, 5):
    num = int(input('Type a number: '))
    if c == 0 or num > my_list[-1]:
        my_list.append(num)
        print('Add this number at the end.')
    else:
        pos = 0
        while pos < len(my_list):
            if num <= my_list[pos]:
                my_list.insert(pos, num)
                print(f'The number was added in the {pos} position')
                break
            pos +=1
print(my_list)