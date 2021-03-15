'''
Managing the performance of a soccer player
reading the name, how many matches, number of goals in each match,
inserting everything in one dict, including the total goals scored during the championship.
'''

info = dict()
goals_tot = []

info['name'] = str(input('name: ')) 
info['matches'] = int(input('matches: '))
for i in range(info['matches']):          
   goals_tot.append(int(input(f'Goals at the {i+1}º match: ')))

info['goals per match'] = goals_tot

info['total goals']= sum(goals_tot)
print('-='*20)
print(f"The field name has the value {info['name']}.")
print(f"The field goals per match has the value {info['goals per match']}.")
print(f"The field total goals has the value {info['total goals']}.")
print('-='*20)
opt = str(input('Wish get details from that player? [Y/N]: ')).lower()
if 'y' in opt:
    print(f'The player {info["name"]} played {info["matches"]} matches.')
    for i in range(info['matches']):
        print(f'On the {i+1}º match he scored {info["goals per match"][i]} goal(s).')
    print(f"In total he scored: {info['total goals']} goals")    