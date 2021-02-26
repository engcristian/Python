'''
Take names and weights and insert in a list.
Show how many ppl were signed up;
A list with heaviest ppl;
A list with lighter ppl;
'''
#Creating two empty lists
low_weight = list()
high_weight =[]
#Getting the firsts input before get inside the looping
name = str(input('Nome: '))
weight = int(input('weight: '))
#Setting the higher and lower weights by default 
higher = weight
lower = weight
count = 0 #Counting how many people were singed up
#Inserting the default values in both lists
high_weight.append(name)
high_weight.append(weight)
low_weight.append(name)
low_weight.append(weight)
while True:
    
    opt = str(input('Continue? [Y/N] :'))
    if 'y' in opt.lower():
        count += 1
        name = str(input('Nome: '))
        weight = int(input('weight: '))        
    #Filling the high_weight list
    if  weight >= higher :        
        higher = weight
        high_weight.append(name)
        high_weight.append(weight)
    #Filling the low_weight list
    if  weight <= lower :        
        lower = weight
        low_weight.append(name)
        low_weight.append(weight)
    if 'n' in opt.lower():
        break
    else:
        print('Sorry, the options are Y - yes or N - no.')
#Getting only the information inside the list, without ''
h_person = high_weight[-2:]
l_person = low_weight[-2:]
print(f'Total {count+1} people were signed up.')
print(f'The heavier person is {h_person[-2]} with {h_person[-1]}Kg.')
print(f'The lighter person is {l_person[-2]} with {l_person[-1]}Kg.')
