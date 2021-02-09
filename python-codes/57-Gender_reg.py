'''
Registering the gender of people infinitely using while
'''

gender = ''
while gender in 'F' or 'M':
    gender = str(input('Inform the gender [M/F]: ')).strip().upper()[0]
    if gender in 'M' or gender in 'F':
        if gender in 'M':
            print('Registered male gender.')
        elif gender in 'F':
            print('Registered female gender.')
    else:
        print('Please, inform the gender correctly!')