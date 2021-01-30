total_gasto = custo_mil = val_barato = c = 0
barato = ''
while True:
    prod = str(input('Nome do produto: ')).strip().upper()
    valor = float(input('Valor do produto: R$'))
    total_gasto += valor
    c += 1
    if c == 1:
        val_barato = valor
        barato = prod
    else:
        if valor < val_barato:
            val_barato = valor
            barato = prod
    if valor > 1000:
        custo_mil +=1
    keep = str(input('Deseja continuar as compras? [S/N]')).strip().lower()[0]
    while 's' not in keep and 'n' not in keep:
        print('Desculpe, as opções são S (sim) ou N (não).')
        keep = str(input('Deseja continuar as compras? [S/N]')).strip().lower()[0]
    if 'n' in keep:
        break
print('-='*30)
print(f'O total da compra foi de R${total_gasto:.2f}.')
print(f'{custo_mil} produto(s) acima de R$ 1000.')
print(f'O produto mais barato foi "{barato}" custando R${val_barato:.2f}.')
print('Obrigado pelas compras, volte sempre!!')
print('-='*30)
