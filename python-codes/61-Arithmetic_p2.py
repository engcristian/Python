'''
Remaking the ex. 51-Arithmetic_p using 'while' to get 10 firsts elements 
'''
first_term = int(input('Type the first term of this A.P: '))
reason = int(input('Type the reason of this A.P: '))
cont = 1
while cont <= 10:
    print(f'{first_term} ► ', end=' ')
    first_term += reason
    cont += 1

