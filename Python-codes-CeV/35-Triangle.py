""" 
Read 3 lengths of a line, and discover if they can form a triangle or not.
"""
print('-='*20)
print(f'{"Triangle Analyzer":^40}')
print('-='*20)

a = float(input('First segment: '))
b = float(input('Scond segment: '))
c = float(input('Third segment: '))

if a < b + c and b < c + a and c < a + b: #basic logic to check if three lines can form a triangle
    print('The segments MAKE a triangle!')
else:
    print("The segmanets DON'T MAKE a triangle!")