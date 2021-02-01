'''
Will set true if you have 'Smith' inside your full name;
'''
name = str(input('Type your full name: ')).strip()
print('Do you have Smith in your name? {}'.format('smith' in name.lower()))