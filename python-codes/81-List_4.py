'''
Reading many numbers and insert in a list
1 - how many numbers were typed?
2- list in reverse - true
3- if the number 5 was typed and is inside or not the list
'''

my_list = []
count = 0

while True:
    my_list.append(int(input('Type any number: ')))
    
    count+= 1
    
    if -0 in my_list:
        
        my_list.pop() 
        my_list.sort(reverse = True)       
        print(f'Were typed {count-1} numbers in this list.')
        print(f'The reverse list is {my_list}')
        
        if 5 in my_list:            
            print(f'Was found the number 5 in the {my_list.index(5)+1} position.')

        elif 5 not in my_list:
            print('Was not found the number 5')
        break