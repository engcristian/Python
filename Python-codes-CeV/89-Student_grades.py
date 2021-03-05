'''
Take name and two grades from many students
ONE LIST -> Nested list
Show a final grade from each student with the average grade
first show the final grade
Then ask if want to get the individual grade
'''
while True:
    name = str(input('Name: '))
    grade1 = float(input('First grade: '))
    grade2 = float(input('Second grade: '))
    avg = (grade1 + grade2)/2
    main_grade = list()

    main_grade.append([name,[grade1, grade2], avg])
    opt = str(input("Continue? [Y/N] "))
    if 'Nn' in opt:
        break
for i, a in enumerate(main_grade):
    print(f'{i}>>{a[0]}>>{a[2]}')

print(main_grade)