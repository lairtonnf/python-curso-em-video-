from time import sleep
valor = int(input('Qual número deseja ver o fatorial: '))
resultado = valor*valor
contagem = 0
while contagem != resultado:
    resposta = valor * contagem
    contagem += 1
print('Calculando {}!'.format(valor))
sleep(1)
print('O fatorial de {} é {}'.format(valor,resposta))
