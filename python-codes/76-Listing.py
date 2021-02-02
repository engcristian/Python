'''
Using Tuple to create a simple listing including the products and the respective prices.
'''
print('-'*40)
print(f'{"LISTING":^40}')
print('-'*40)
listing = ('Água', 2, 'Arroz', 5.47, 'Feijão', 7.26,'Óleo',
    6.89,'Macarrão', 4.39)
for l in range(0, len(listing)):
    if l%2 == 0:
        print(f'{listing[l]:.<30}', end='')
    else:
        print(f'R$ {listing[l]:>7.2f}')