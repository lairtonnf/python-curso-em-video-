import math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
comprimento = math.hypot(cateto_oposto,cateto_adjacente)
print('A hipotenusa vai medir {:.2f}'.format(comprimento))

