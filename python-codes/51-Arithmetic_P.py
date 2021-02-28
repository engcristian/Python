'''
Arithmetic progression with 10 elements.
'''
first_term = int(input('Type the first term of this A.P: '))
reason = int(input('Type the reason of this A.P: '))
last_term = first_term + (50-1)*reason # A.P formula
for c in range (first_term, last_term + reason , reason):

    print(c, end=' ► ')
