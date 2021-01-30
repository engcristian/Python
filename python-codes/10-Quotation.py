'''
Simple way to know how much U$ Dollars I can buy with some Reais in my wallet
Note: The dollar price is fixed based on a false quotation.
'''
money = float(input('How much Reais do you have in your wallet? R$ \033[1;32mR$\033[m'))
value = money / 5.23
print('You can buy \033[1;36mU${:.2f}\033[m dollars.'.format(value))