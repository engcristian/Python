frase = str(input('Digite alguma coisa: ')).strip().upper()
palavras = frase.split()
junto = frase.replace(' ', '')
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('o texto {} inverso é {}.'.format(frase, inverso))
if inverso == junto:
    print('É um palíndromo.')
else:
    print('Não é um palindromo.')