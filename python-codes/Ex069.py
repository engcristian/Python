maior = cont_homen =cont_mulher = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if idade > 1 and 'M' in sexo:
        cont_homen += 1
    if idade < 20 and 'F' in sexo:
        cont_mulher += 1
    parar = str(input('Deseja continuar cadastrando? [Y/N]')).strip().lower()
    while parar not in 'yn':
        print('As opções são Y - yes e N - No.')
        parar = str(input('Deseja continuar cadastrando? [Y/N]')).strip().lower()[0]
    if 'n' in parar:
        break
print(f'{maior} maiores de idade\n{cont_homen} foram homens\ne {cont_mulher} mulheres menores de idade.')