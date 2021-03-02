'''
Make a 3x3 matrix and fill with numbers
at the end show the matrix in a right format
'''
cr1 = []
cr2 = []
cr3 = []

for c in range(0,3):
    cr1.append(int(input(f'Tirst line (1 X {c+1}): ')))
for c in range(0,3):
    cr2.append(int(input(f'Second line (2 X {c+1}): ')))
for c in range(0,3):
    cr3.append(int(input(f'Third line (3 X {c+1}): ')))

print(f''' The matrix is:
            {cr1}
            {cr2}
            {cr3}''')
