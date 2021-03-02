'''
Read 5 weights and show the higher and the lower value in KG
'''
higher = 0
lower = 0
for p in range (1, 6):
    weight = int(input(f"Type the {p}º person's weight: ")) # p counts the people
    if p == 1: # First loop the higher and the lower receives the first value
        higher = weight 
        lower = weight
    else: # second loop onward compare the higher and lower values
        if weight > higher:
            higher = weight
        if weight < lower:
            lower = weight
print(f'The highest weight registered was {higher}Kg')
print(f'The lowest weight registered was {lower}Kg')
