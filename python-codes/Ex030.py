'''
Read and int number and check the EVEN or ODD 
'''

num = int(input('Digite um número:'))


if num%2 == 1:
    print('O número {} é IMPAR!'.format(num))
else:
    print('O número {} é PAR!'.format(num))