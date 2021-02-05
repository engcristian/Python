""" Ask for the Athlet age and show in with category he/she fits.
    Using date from datetime lib to check the current date
"""
from datetime import date
year = int(input("Inform the athlete's year of birth: "))
day_today = date.today().year
age = day_today - year

if age <= 9:
    print(f'The athlete is {age} y.o and fits the \033[32mCHILD\033[m category.')
elif age <= 14:
    print(f'The athlete is {age} y.o and fits the \033[32mCHILDISH\033[m category.')
elif age <= 19:
    print(f'The athlete is {age} y.o and fits the \033[32mJUNIOR\033[m category.')
elif age <= 25:
    print(f'The athlete is {age} y.o and fits the \033[32mSENIOR\033[m category.')
else:
    print(f'The athlete is {age} y.o and fits the \033[32mMASTER\033[m category.')