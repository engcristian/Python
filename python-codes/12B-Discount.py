'''
 As in 12A, you can see the discount by purchase with money
 and an increasement when used credit card.'''

price = float(input('Inform the product price: $'))
desc_cash = price - price*(10/100) # discount 10% from the real price
increase = price + price*(8/100)      # 8% increasement 
print("The product costs ${:.2f}. In cash with 10% discount it's ${:.2f}\n "
      "And by credit card has an increasement of 8%, so it's ${:.2f}.".format(price, desc_cash, increase))