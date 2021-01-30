# somar todos os números ímpares e que são múltiplos de 3 , entre 1 e 500
s = 0
cont = 0
for c in range(3, 501, 6):
    s += c
    cont += 1
    print(c)
print(s, cont)