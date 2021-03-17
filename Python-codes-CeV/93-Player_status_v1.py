'''
Managing the performance of a soccer player
reading the name, how many matches, number of goals in each match,
inserting everything in one dict, including the total goals scored during the championship.
'''

info = dict()
goals_tot = []

info["name"] = str(input("Player's name: ")) 
info["matches"] = int(input('How many matches did he/she play? '))
for i in range(info['matches']):          
   goals_tot.append(int(input(f'How many goals at the {i+1}º match: ')))

info['goals per match'] = goals_tot
info['total goals']= sum(goals_tot)
opt =''
print('-='*20)
print(f"The field 'name' has the value {info['name']}.")
print(f"The field 'goals per match' has the value {info['goals per match']}.")
print(f"The field 'total goals' has the value {info['total goals']}.")
print('-='*20)
while 'y' or 'n' in opt:
    opt = str(input('Do you wish to get details from that player? [Y/N]: ')).lower()
    
    if 'y' in opt:
        print(f'The player {info["name"]} played {info["matches"]} matches.')
        for i in range(info['matches']):
            print(f'On the {i+1}º match he/she scored {info["goals per match"][i]} goal(s).')
        print(f"In total he/she scored: {info['total goals']} goals")
        break
        
    if 'n' in opt:
        print('Thank you! Come back often.')
        break
    else:
        print('Sorry, the options are Y/N.')

