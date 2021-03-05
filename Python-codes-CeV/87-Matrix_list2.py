'''
Improve ex-86
Sum all EVEN numbers
Sum all 3º columns
Highest value from the second line
'''
cr = [[],[],[]]
sum_even_cr0 = sum_even_cr1 = sum_even_cr2 = 0

for c in range(0,3):
    num0 = int(input(f'Tirst line [1, {c+1}]: '))
    cr[0].append(num0)
    if num0 % 2 == 0:
        sum_even_cr0 += num0        

for c in range(0,3):
    num1 = int(input(f'Second line [2, {c+1}]: '))
    cr[1].append(num1)
    if num1 % 2 == 0:
        sum_even_cr1 += num1
for c in range(0,3):
    num2 = int(input(f'Third line [3, {c+1}]: '))
    cr[2].append(num2)
    if num2 % 2 ==0:
        sum_even_cr2 += num2
total_sum= sum_even_cr0 + sum_even_cr1 + sum_even_cr2
sum_3rd_column = cr[0][-1] + cr[1][-1] + cr[2][-1]
print(f''' The matrix is:\n {cr[0]}\n {cr[1]}\n {cr[2]}''')
print(f'The sum of all even numbers is {total_sum}.')
print(f'The sum of all numbers in the 3rd column is {sum_3rd_column}.')
print(f'The highest value in the second line is {max(cr[1])}')