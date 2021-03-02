'''
Analysing a full name.
'''
name = str(input('Type your full name: ')).strip()
print('Your name in capital letters is {}.'.format(name.upper()))
print('Your name in lower case is {}.'.format(name.lower()))
print('Your name has altogther {} letters.'.format(len(name) - name.count(' ')))
splitted = name.split()
print('Your first name is {} and it has {} letters.'.format(splitted[0], len(splitted[0])))