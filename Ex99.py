from time import sleep
def maior(*num):
    print('-'*40)
    print('Analisando Valores Informados...')
    if not num:
        print(f'Foram informados 0 Valores')
        print(f'O Maior Valor Informado foi 0')
    else:
        for v in num:
            print(f'{v}', end=' ', flush=True)
            sleep(0.5)
        print(f': Foram Informados {len(num)} Valores')
        print(f'O Maior Valor Informado Foi {max(num)}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()