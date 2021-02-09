'''
Checking the sequence of Fibonacci number
'''
next_num = 0
prev_num = 0
num = int(input('Type how many Fibonacci numbers do you want to check: '))
count = 0
while count < num:
    while count < num:
        count += 1       
        print(f'{next_num}', end=' ► ')
        # basic mathmatic logic of a Fiboncci number
        next_num = next_num + prev_num
        prev_num = next_num - prev_num
        if next_num == 0:
            next_num = next_num + 1
print('END')