# contagem regressiva de 10 até 0 para estouros de fogos, com pausa de 1s entre eles.
from time import sleep
import emoji
print('='*5, 'CONTAGEM REGRESSIVA!', '='*5)
for c in range(10, 0, -1):
    print('{:^33}'.format(c))
    sleep(1)
print(emoji.emojize(':fireworks:'*20))
print('{:^33}'.format('Feliz Ano Novo!'))
print(emoji.emojize(':fireworks:'*20))
# 'Feliz Ano Novo!!',':fireworks:'*20))