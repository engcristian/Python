import csv
import pandas as pd

time = []

print('-'*50)
print('-=' * 10, ' WAKATIME ', '-=' * 10)
print('-'*50)

opt = int(input('''
Escolha uma das opções: 
1 - Acrescentar dia e hora;
2 - Total de horas;
3 - Total de horas do dia de ontem;
4 - Total de horas dos 7 últimos dias;
5 - Total de horas dos 15 últimos dias;
6 - Total de horas dos 30 últimos dias; 
7 - Fechar;
'''))

df = pd.read_csv('hours.csv', index_col= 'semana')

if opt == 1:    
    time.append(str(input('Dia: ')))
    time.append(int(input('Horario: ')))
    with open('hours.csv', 'a', newline='') as file:
    
        writer = csv.writer(file)        

        writer.writerow(time)       
        
        file.close()

    print('Suas horas foram salvas.')
if opt == 2:
    t = len(df)
    total = df['horas'].sum()
    print(f'Foram {t} dias de programação')
    print(f'Ao todo {total} horas de programação. Parabéns')

if opt == 3:
    
    tot_y = df['horas'][-1:].sum()
    a = df[-1:]
    print(a)
    print(f'Ontem foi um total de {tot_y} horas de programação.')

if opt == 4:
    print(df[-7:])
    tot_w = df['horas'][-7:].sum()
    print(f'Últimos 7 dias teve um total de {tot_w} horas de programação.')
if opt == 5:
    print(df[-15:])
    tot_q = df['horas'][-15:].sum()
    print(f'Últimos 15 dias teve um total de {tot_q} horas de programação.')
if opt == 6:
    print(df[-30:])
    tot_m = df['horas'][-30:].sum()
    print(f'Últimos 30 dias teve um total de {tot_m} horas de programação.')

if opt == 7:
    print('Obrigado, bons estudos!')