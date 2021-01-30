quantidade = 0
num = 1
soma = maior = menor = 0
while num != 0:
    num = float(input('Digite valores, ao terminar digite 0 para obeter o resultado: '))
    soma = soma + num
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor and num != 0:
            menor = num
print('A média dos números digitados foi {:.2f}.'.format(soma/(quantidade-1)))
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))