'''perguntar o salário de um funcionário,
para salários superiores a 1250, aumenta 10%, para inferiores, 15%'''

salary = float(input('Informe o salário do funcionário: '))
upten = (salary * 10/100) + salary
upfifteen = (salary * 15/100) + salary

if salary > 1250:
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f} agora. '.format(salary, upten))
else:
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f} agora.'.format(salary, upfifteen))