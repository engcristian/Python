# ler três números e mostrar qual é o menor e o maior
num1 = int(input('Digite o 1º número:'))
num2 = int(input('Digite o 2º número:'))
num3 = int(input('Digite o 3º número:'))
# Atribui uma variável como a menor, para eliminar uma tentativa.
menor = num1

if num2 < num1 and num2:
    menor = num2
if num3 < num2 and num1:
    menor = num3
print('O menor valor digitado foi {}.'.format(menor))

# Atribuindo uma variável como a maior, para facilitar a lógica.
maior = num1

if num2 > num1 and num3:
    maior = num2
if num3 > num1 and num2:
    maior = num3
print('O maior valor digitado foi {}.'.format(maior))