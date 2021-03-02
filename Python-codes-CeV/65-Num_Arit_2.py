'''
It shows the sum's average of the numbers typed, the lower value and the higher too.
'''
average = 0
num = 1
add = higher = lower = 0
#using flag as example
while num != 0:
    num = float(input('Type values, when finish, type 0 to get the results: '))
    add = add + num
    average = average + 1
    if average == 1:
        higher = num
        lower = num
    else:
        if num > higher:
            higher = num
        if num < lower and num != 0:
            lower = num
#sum all numbers and get the average
print(f'The average of the typed numbers were {add/(average-1):.2f}.')
print(f'The lower value typed was {lower}.')
print(f'The higher value typed was {higher}.')