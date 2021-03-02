'''
How much liters of paint do you need to paint your wall?
Simple way to discover that by a simple area formula.
'''
width = float(input("What's your wall's width? "))
height = float(input("What's your wall's height"))
area = width * height #area formula
print('Your wall has the dimension of \033[1;32m{} x {}\033[m, and its area is \033[1;32m{}m²\033[m.'.format(width, height, area))
print('Will be necessary \033[1;31m{:.1f} L\033[m of paint to paint the wall'.format(area / 2))
