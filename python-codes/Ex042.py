# complemento do ex35 , para saber se o triângulo e equilátero, isósceles ou escaleno
print('-='*20)
print('       Analisador de Triânngulos')
print('-='*20)
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a < b + c and b < c + a and c < a + b:
    print('Os segmentos FORMAM um triângulo!')
    if a == b == c:
        print('O triângulo é um equilátero!')
    elif a != b != c != a:
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isosceles')
else:
    print('Os segmentos NÃO FORMAM um triângulo!')
