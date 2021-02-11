'''
Now using infinite loop with while, sum all numbers typed and show the result
The 'break' condition is the number 999
'''
sum = count = 0
while True:
    num = int(input('Type a number [999 to stop] : '))
    if num == 999: #the same as flag, the program will break/stop when 999 is typed
        break
    sum += num
    count += 1
print(f'Were {count} numbers typed and the sum beteween them is {sum}.')