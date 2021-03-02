''' Calculat the leap year'''
from datetime import date
year = int(input('What year do you want to analyse? Type 0  for the current year.'))
if year == 0:
   year = date.today().year
if year%4 ==0 and year%100 != 0 or year%400 == 0:
    print(F"The year {year} it's a LEAP year.".)
else:
    print(F"The year {year} isn't a LEAP year.")