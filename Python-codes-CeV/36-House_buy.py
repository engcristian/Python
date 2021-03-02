
''' 
Askinf th house value, buyer's salary and how many years will pay it ..
conditions: monthly installment amount, it can't exceed 30% of the salary or it will be denied.
'''
print('-='*30)
print('      \033[7;33mWelcome to the Real Estate Loan System\033[m')
print('-='*30)

name = str(input("What's your name?")).lower().title()
house = float(input(f"Hello Mr(s) {name}. Please, inform the house's value that you want to finace: "))
salary = float(input(f"Mr(s) {name}, now inform your monthly salary: "))
year = int(input(f'Very well Mr(s) {name}, to finish it, insert here in how many years do you want to pay it : '))
installments = year * 12
value = house / installments

if value > salary * 30 / 100:
    print(f"Sorry Mr(s) {name}, but your loan was denied, because in {year} year\nthe installment will be ${value:.2f}, and surpasses 30% of your salary.")
elif value <= salary * 30 /100:
    print(f"That's great! Your loan was approved, with installments of ${value:.2f}!")
