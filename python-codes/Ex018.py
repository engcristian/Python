# ler um ângulo e mostrar seu seno, cosseno, primeiro transformar a entrada em radianos para dps calcular o valor

import math
ang = float(input('Insira um valor do ângulo: '))
rad = math.radians(ang)
print('O cosseno é {:.2f}\nO seno {:.2f}\nE a tangente é {:.2f}.'.format(math.cos(rad), math.sin(rad),math.tan(rad)))
