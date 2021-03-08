'''
Make a program that reads a student's name and average grade and
also keeping the student's situation.
at the end show the content of the structure.
'''
student = {}

student['name'] = str(input("Student's name: "))
student['avg'] = float(input("Student's average grade: "))
if student['avg'] >= 7:
    student['situation'] = 'APPROVED'
    print(student)
    print(f'The student {student["name"]} has grade: {student["avg"]}.\nSituation : {student["situation"]}')    
else:
    student['situation'] = 'DISAPPROVED'
    print(student)
    print(f'The student {student["name"]} has grade: {student["avg"]}.\nSituation : {student["situation"]}')