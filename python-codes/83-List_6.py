'''
Checking the expression's parentheses
'''

expression = str(input('Type a math expression with parentheses: '))
par_list = [] # parentheses list
for simbol in expression:
    if simbol =='(':
        par_list.append('(')
    elif simbol == ')':
        if len(par_list)>0:
            par_list.pop()
        else:
            par_list.append(')')
            break
if par_list == 0:
    print('Your expression is right.')
else:
    print("Your expression isn't right.")