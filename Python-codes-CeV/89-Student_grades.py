'''
Take name and two grades from many students
ONE LIST -> Nested list
Show a final grade from each student with the average grade
first show the final grade
Then ask if want to get the individual grade
'''
main_grade = []
student_grade = []
while True:

    nome = input('Name: ')
    nota1 = float(input('First grade: '))
    nota2 = float(input('Second grade: '))
    student_grade.append(nome)
    student_grade.append(nota1)
    student_grade.append(nota2)
    main_grade.append(nome)
    avg = (nota1 + nota2)/2
    main_grade.append(avg)
    opt = input('Keep? [Y/N]').lower()
    if  'n' in opt:
        break

print(student_grade, main_grade)