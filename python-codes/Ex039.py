## ler a idade de um jovem, informar se ele vai, se é hora, ou se já se alistou
from datetime import date
print('''Informe o seu sexo:
1- Masculino
2- Feminino''')
gender = int(input('Opção:'))
if gender == 1:

    age = int(input('Por favor, informa o ano de nascimento do jovem: '))
    mes = int(input('Agora informe o mês do nascimento: '))
    dia = int(input('E por último, o dia do nascimento: '))
    today = date.today()
    alist = age + 18
    idade = today.year - age


    if idade > 18:
        print('Ele já se alistou, cerca de {} anos e {} meses atrás'.format(today.year - alist, mes - today.month))
    elif idade == 18:
        print('Está na idade limite para se alistar!')
    elif idade == 17:
        print('Está no período de alistamento, ele tem {} ano e {} meses para se alistar!'.format(-(today.year-alist), -(today.month-mes)))
    elif idade > 1 < 17:
        print('Ainda não está no período de alistamento, aguardar {} anos e {} meses para o processo.'.format(17-idade, -(today.month-mes)))
elif gender == 2:
    print('Desculpe, mas o alistamento é obrigatório apenas para homens.')
