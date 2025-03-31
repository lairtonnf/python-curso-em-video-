print('SISTEMA DE MULTAS')
velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você foi \033[1;31mmultado\033[m')
    print('Sua multa foi no valor de \033[1;31m{}\033[mBRL'.format(((velocidade)-80)*7))
else:
    print('Você não foi multado')
