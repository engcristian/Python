'''
By a product price is possible check many ways of payments
and how it will change the price depending on each form of payment
'''
price_prod = float(input("What's the product price?"))
option = int(input('Choose the form of payment :\n'
                 '1- In cash, 10% off;\n'
                 '2- Cash on debt or credit, 5% off;\n'
                 '3- Installmentes up to 3x, normal price;\n'
                 '4- Installmentes up to 4x or more, 20% interest;'))
disccount_5 = price_prod - price_prod * 5 / 100 # discounting 5% from the product price
discount_10 = price_prod - price_prod * 10 / 100 # discounting 10% from the product price
interest = price_prod + price_prod * 20 / 100 # adding 20% interest on the product price

if option == 1:
    print(f'The product costs ${price_prod:.2f}, so will cost ${discount_10:.2f} in cash!')
elif option == 2:
    print(f'The product costs ${price_prod:.2f}, so will cost ${disccount_5:.2f} on debt or credit!')
elif option == 3:
    parcel_3 = int(input('Okay, do you wish small installments?\n'
                      '2- Installments 2x;\n'
                      '3- Installments 3x;\n'))
    if parcel_3 == 2:
        print(f' The product will cost ${price_prod:.2f} in 2x on card, each installment will cost ${price_prod / 2:.2f}.')
    elif parcel_3 == 3:
        print(f' The product will cost ${price_prod:.2f} in 3x on card, each installment will cost ${price_prod / 3:.2f}.')
elif option == 4:
    parcel_4 = int(input('Please, inform the number of installments.'))
    print(f'The product costs ${price_prod:.2f}, and will be {parcel_4}x of ${interest / parcel_4:.2f}.\n'
        f'In total will cost ${interest:.2f}.')
else:
    print('Invalid payment option, please insert the right number.')
