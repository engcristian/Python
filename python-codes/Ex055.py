# ler o peso de 5  pessoas e mostrar qual foi o maior e o menor lido
maior = 0
menor = 0
for c in range (1, 6):
    p = int(input('Digite o peso da {}º pessoa: '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso registrado é de {}Kg'.format(maior))
print('O menor peso registrado é de {}Kg'.format(menor))
