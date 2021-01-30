'''
Do you want to know how much will be your salary when receive a 15% increase?
'''

salary = float(input("What's the employee's salary? $"))
new_salary = salary + salary*(15/100) #how to increase 15% on the salary
print('The employee who earned ${:.2f}, with 15% increase, starts to earn ${:.2f}.'.format(salary, new_salary))
