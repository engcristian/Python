'''
Will set true for any city with the name Saint included.
e.g. = Saint Louis
'''
city = str(input('In what city were you born? '))
c = city.lower()
print('saint' in c)