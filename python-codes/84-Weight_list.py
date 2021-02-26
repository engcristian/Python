'''
Take names and weights and insert in a list.
Show how many ppl were signed up;
A list with heaviest ppl;
A list with lighter ppl;
'''
main_list = []
name_weight =[]
    name = str(input('Nome: '))
    peso = int(input('Peso: '))
    name_weight.append(name)
    name_weight.append(peso)
while True:
    
    opt = str(input('Continue? [Y/N] :')).lower()
    if 'y' in opt:
        name = str(input('Nome: '))
        peso = int(input('Peso: '))
        name_weight.append(name)
        name_weight.append(peso)
    elif 'n' in opt:
       break

print(name_weight)
