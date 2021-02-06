'''
Multiplication table now using for to simplificate the code
'''
num = int(input('Type a number: '))
print('-'*12)
for c in range(1, 11):
   print(f'{num} x {c} = {c*num}')
print(('-'*12))
