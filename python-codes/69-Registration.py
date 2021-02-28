'''
Signing up men and women both getting the gender and age information
'''

older = count_man =count_woman = 0
while True:
    age = int(input('Type your age: '))
    gender = ' '
    while gender not in 'MW':
        gender = str(input('Type your gender: [M/W]')).strip().upper()[0]
    if age >= 18:
        older += 1
    if age > 1 and 'M' in gender:
        count_man += 1
    if age < 20 and 'W' in gender:
        count_woman += 1
    stop = str(input('Do you want to keep? [Y/N]')).strip().lower()
    while stop not in 'yn':
        print('Sorry, the options are Y - yes and N - No.')
        stop = str(input('Do you want to keep signin up? [Y/N]')).strip().lower()[0]
    if 'n' in stop:
        break
print(f'{older} Older people\n{count_man} were men\nand {count_woman} underage woman.')