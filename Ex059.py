from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('=====MENU=====')
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa''')
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        print('O resultado de {} + {} é = {}'.format(n1,n2, n1+n2))
    if opção == 2:
        print('O resultado de {} X {} é = {}'.format(n1,n2, n1*n2))
    if opção == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    if opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    if opção == 5:
        print('Finalizando programa, aguarde...')
        sleep(1)
        print('Programa encerrado')