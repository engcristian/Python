'''
Ask an employee's salary,for wages above $ 1250, it increases 10%,
for wages below it, increases 15%.
'''
salary = float(input("Inform the employee's wage: "))
upten = (salary * 10/100) + salary # Adding 10% to salary 
upfifteen = (salary * 15/100) + salary # Adding 15% to salary
if salary > 1250:
    print(f'Who earned ${salary:.2f}, now starts receiving ${upten:.2f} .')
else:
    print(f'Who earned ${salary:.2f}, now starts receiving ${upten:.2f} .')