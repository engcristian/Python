'''
Improve ex-86
Sum all EVEN numbers
Sum all 3º columns
Highest value from the second line
'''
cr1 = []
cr2 = []
cr3 = []
sum_even_cr1 = sum_even_cr2 = sum_even_cr3 = 0

for c in range(0,3):
    num1 = int(input(f'Tirst line (1 X {c+1}): '))
    cr1.append(num1)
    if num1%2 == 0:
        sum_even_cr1 += num1        

for c in range(0,3):
    num2 = int(input(f'Second line (2 X {c+1}): '))
    cr2.append(num2)
    if num2%2 == 0:
        sum_even_cr2 += num2
for c in range(0,3):
    num3 = int(input(f'Third line (3 X {c+1}): '))
    cr3.append(num3)
    if num3%2 ==0:
        sum_even_cr3 += num3
total_sum= sum_even_cr1+sum_even_cr2+sum_even_cr3
sum_3rd_column = cr1[-1] + cr2[-1] + cr3[-1]
print(f''' The matrix is:
            {cr1}
            {cr2}
            {cr3}''')
print(f'The sum of all even numbers is {total_sum}.')
print(f'The sum of all numbers in the 3rd column is {sum_3rd_column}.')
print(f'The highest value in the second line is {max(cr2)}')