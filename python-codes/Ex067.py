while True:
    num = int(input('Digite o valor para calcular sua tabuáda: '))
    if num <= 0:
        break
    print('-=' * 20)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-='*20)
print('Obrigado, volte sempre!')