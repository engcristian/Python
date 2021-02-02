# Read three numbers and show what's the higher and lower.
num1 = int(input('Type the 1º number: '))
num2 = int(input('Type the 2º number: '))
num3 = int(input('Type the 3º number: '))

# Putting a var with the lower value at the beggin
lower = num1
if num2 < num1 and num2 < num3:
    lower = num2 # the  2º number receives the lower value
if num3 < num2 and num3 < num1:
    lower = num3 # the 3º number receives the lower value
print(f'The lower value typed was {lower}.')

# Putting the var higher with the 1º number becames easy for the code.
higher = num1
if num2 > num1 and num2 > num3:
    higher = num2
if num3 > num1 and num3 > num2:
    higher = num3
print(f'The higher value typed was {higher}.')