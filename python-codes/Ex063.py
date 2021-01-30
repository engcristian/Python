prox = 0
ant = 0
n = int(input('Digite quantos números de Fibonacci quer saber: '))
c = 0
while c < n:
    while c < n:
        c += 1
        print('{}'.format(prox), end=' ► ')
        prox = prox + ant
        ant = prox - ant
        if prox == 0:
            prox = prox + 1
print('FIM')