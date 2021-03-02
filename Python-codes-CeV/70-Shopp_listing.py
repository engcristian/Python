'''
Shopping list, talking the cheap and expensive prices from the products
'''

total_spent = over_thousand = cheap_price = count = 0
cheap = ''
while True:
    product = str(input('Product name: ')).strip().upper()
    value = float(input('Product price: $'))
    total_spent += value
    count += 1
    if count == 1:
        cheap_price = value
        cheap = product
    else:
        if value < cheap_price:
            cheap_price = value
            cheap = product
    if value > 1000:
        over_thousand +=1
    keep = str(input('Do you want to keep purchasing? [Y/N] ')).strip().lower()[0]
    while 'y' not in keep and 'n' not in keep:
        print('Sorry, but the options are Y (yes) or N (no).')
        keep = str(input('Do you want to keep purchasing? [Y/N] ')).strip().lower()[0]
    if 'n' in keep:
        break
print('-='*30)
print(f'Total purchase ${total_spent:.2f}.')
print(f'{over_thousand} product(s) over $1000.')
print(f'The cheapest product was "{cheap}" costing ${cheap_price:.2f}.')
print('Thank you for shopping, come back often!!')
print('-='*30)
