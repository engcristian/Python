brasil = []
estado = {}

for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)

for l in brasil:
    for k, v in l.items():
        print(f'O campo {k} tem valor {v}.')