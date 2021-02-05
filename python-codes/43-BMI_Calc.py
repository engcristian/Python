"""
Simple Body Mass Index with five category.

"""
weight = float(input('Inform your weight in (Kg): '))
height = float(input('Inform your height in (m): '))
BMI = weight/(height ** 2)

if BMI < 18.5:
    print(f'BMI = {BMI:.2f} => UNDERWEIGHT.')
elif 18.5 <= BMI < 25:
    print(f'BMI = {BMI:.2f} => NORMAL.')
elif 25 <= BMI <= 30:
    print(f'BMI = {BMI:.2f} => OVERWEIGHT.')
elif 30 < BMI <= 40:
    print(f'BMI = {BMI:.2f} => OBESE.')
elif BMI > 40:
    print(f'BMI = {BMI:.2f} => EXTREMELY OBESE.')
