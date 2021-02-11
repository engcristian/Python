'''
Calculating the multiplication table using for repetition and infinite while repetition
just to stop the program.
Only will stop when type the value 0;
'''

while True:
    num = int(input('Type a value to calculate its multiplication table: '))
    if num <= 0:
        break
    print('-=' * 20)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-='*20)
print('Thank you! Check back often!')