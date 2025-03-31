multiplicador = cont = 1
while True:
    if cont == 11:
        cont = 1
    tabuada = int(input('Tabuada: '))
    if tabuada < 0:
        break
    while cont <= 10:
        resultado = tabuada * cont
        print(f'{tabuada} X {cont} = {resultado}')
        cont += 1
print('Programa encerrado...')

