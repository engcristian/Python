'''
Insert 5 numbers in the right position without using .sort()
Then show the list orderned
'''
my_list = []

while True:

    my_list.append(int(input('Type any number: ')))
    if -0 in my_list:
        my_list.pop()
        order_list = sorted(my_list)
        print(f'Ordered list: {order_list}.')