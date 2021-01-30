sexo = ''
while sexo in 'F' or 'M':
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'M' or sexo in 'F':
        if sexo in 'M':
            print('Sexo masculino registrado.')
        elif sexo in 'F':
            print('Sexo feminino registrado.')
    else:
        print('Por favor, informe o sexo corretamente!')