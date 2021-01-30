# ler 6 números inteiros no for e mostrar apenas a soma dos números pares, os impares dessconsiderar
s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'A soma dos {cont} números pares digitados é {s}.')
