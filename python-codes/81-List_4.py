'''
Reading many numbers and insert in a list
1 - how many numbers were typed?
2- list in reverse - true
3- if the number 5 was typed and is inside or not the list
'''
my_list = []
count = 0
my_list.append(int(input('Type any number: ')))
while True:    
    
    opt = str(input('Do you want to keep? [Y/N]: ')).lower()
    if 'y' in opt:
        count+= 1 
        my_list.append(int(input('Type any number: ')))
        
    elif 'n' in opt: 
              
        my_list.sort(reverse = True)       
        print(f'Were typed {count+1} numbers in this list.')
        print(f'The reverse list is {my_list}')
        
        if 5 in my_list:        
              
            print(f'Was found the number 5 in the  position.',end='')
            for i, v in enumerate(my_list):
                if v == 5:
                    print(f'{i}...',end='') 
        elif 5 not in my_list:
            print('Was not found the number 5')
            break
    else:
        print('Sorry, the options are Y - yes or N - no.')  