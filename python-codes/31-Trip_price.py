''' Ask the distance of the trip in km, calculate the ticket price.
0.50 cents per km for trips up to 200km, and 0.45 cents for trips > 200 KM'''

distance = int(input('What is the trip distance in km?'))
print('You are about to take a {:.1f} km trip'.format(distance))
if distance <= 200:

    print(f'Your trip ticket will cost $ {distance*0.5:.2f}')
else:
    print(f'Your trip ticket will cost $ {distance*0.45:.2f}')
