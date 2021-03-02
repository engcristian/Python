'''
Will sum all numbers typed infinitely, while the flag 999 isn't typed
'''
n = 0 # number
s = 0 # sum  
c = 0 # counter 
print('Type 999 to stop and get the result;')
n = int(input('Type a number: '))
while n != 999:
    s = s + n
    c += 1
    n = int(input('Type other number: '))
print(f'The sum of the typed numbers were {s}.')
print(f'The amount of typed numbers were {c}.')
print('END')

