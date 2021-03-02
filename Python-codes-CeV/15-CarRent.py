'''
How to know the fee's rental car by the days rented and distance it traveled.
'''
days = int(input('How many days with the rental car? ')) 
km = float(input('How many Km traveled? '))
fee = (60 * days) + (0.15*km) #Fee that correspond the days with the car and how long it traveled
print(" The fee's amount is $ {:.2f}".format(fee))
