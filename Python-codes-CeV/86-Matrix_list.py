'''
Make a 3x3 matrix and fill with numbers
at the end show the matrix in a right format
'''
cr = [[],[],[]]
for c in range(0,3):
    cr[0].append(int(input(f'First line [1, {c+1}]: ')))
for c in range(0,3):
    cr[1].append(int(input(f'Second line [2, {c+1}]: ')))
for c in range(0,3):
    cr[2].append(int(input(f'Third line [3, {c+1}]: ')))
print(f'''The matrix is:\n{cr[0]}\n{cr[1]}\n{cr[2]}''')
