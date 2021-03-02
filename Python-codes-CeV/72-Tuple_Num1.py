'''
Type a number and receive the written number using tuple as exercise. 
'''
number_list = ('zero','one', 'two', 'three', 'four', 'five','six',
'seven','eight','nine','ten','eleven','twelve','thirteen','fourteen',
'fifteen','sixteen','seventen','eighteen','nineteen','twenty')
while True:    
    num = int(input('Type a number between 0 and 20: '))    
    if num > 20 or num < 0:
        print("You didn't type right. Type a number between 0 and 20.")        
    else:
        print(f'You typed the number {number_list[num]}.')

