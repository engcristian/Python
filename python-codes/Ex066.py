s = c = 0
while True:
    n = int(input('Digite um número [ou 999 para finalizar] : '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram {c} números digitados e a soma entre eles foi {s}.')