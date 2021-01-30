# ler o primeiro termo e a razão aritimética de uma PA, mostrar os 10 primeiros termos.
s = 0

t1 = int(input('Digite o primeio termo da PA: '))
r = int(input('Digite a razão da PA: '))
d = t1 + (10-1)*r #fórmula matemática
for c in range (t1, d + r, r):

    print(c, end=' ► ')
