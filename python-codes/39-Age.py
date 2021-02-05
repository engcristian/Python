'''
Ask the young's age and show if it's time for military enlistment
'''
from datetime import date
print('''Inform your gender:
1- Male
2- Female''')
gender = int(input('Options:'))
if gender == 1:

    birth = int(input("Please, inforem the birth year: "))
    month = int(input("Now, inform the birth month: [1 to 12] "))
    day = int(input('And finally, inform the birth day: '))
    today = date.today()
    enrol = birth + 18
    age = today.year - birth


    if age > 18:
        print(f"He has already enlisted, about {today.year-enrol} years and {month-today.month} months ago.")
    elif age == 18:
        print('He is at the limit age to enlist!')
    elif age == 17:
        print(f"He is in the enlistment period, he has {today.year-enrol} years and {-(today.month-month)} months to enlist himself!" )
    elif age > 1 < 17:
        print(f"Not yet in the enlistment poriod, wait about {17-age} years and {-(today.month-month)} months for the process.")
elif gender == 2:
    print('Sorry, but the enlistment is obligated only for men.')
