'''
The summing of all even numbers in six numbers typed using FOR
'''
sum = 0
count = 0
for c in range(1, 7):
    num = int(input(f'Type the {c}º number: '))
    if num % 2 == 0:
        sum += num
        count += 1
print(f'The sum of {count} even numbers typed is {sum}.')
