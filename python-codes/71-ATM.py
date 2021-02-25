'''
Automated Teller Machine
'''
#Bn = Banknotes
bn50 = bn20 = bn10 = bn1 = rest = 0
value = int(input('how much do you want to withdraw? $'))
while True:
    bn50 = value // 50
    rest = value - bn50*50
    value = rest

    bn20 = value//20
    rest = value - bn20*20
    value = rest

    bn10 = value//10
    rest = value - bn10*10
    value = rest

    bn1 = value//1
    rest = value - bn1*1
    value = rest
    if rest == 0:
        break
print(f'You will get:\n{bn50} dollar bills of $50.\n'
      f'{bn20} bills of $20.\n{bn10} bills of $10\n{bn1} bills of $1')