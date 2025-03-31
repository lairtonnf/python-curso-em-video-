import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O angulo {:.2f} tem o seno {:.2f} coseno {:.2f} tangente {:.2f} '.format(angulo,seno,coseno,tang))
