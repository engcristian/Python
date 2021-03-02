'''
Do you hate %discount% calculus? its a simple way to know how much 
the product will cost with a fixed discount of 5%
'''
price = float(input('How much does the product cost? \033[1;32m$\033[m'))
disc_price = price - price * (5/100) #one simple way to calculte a 5% discount
print('With \033[1;4;31m5%\033[m discount, the product will cost \033[1;33m${:.2f}\033[m.'.format(disc_price))