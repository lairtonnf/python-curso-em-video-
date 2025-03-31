def contador (inicio,fim,passos):
    if passos <0:
        passos = passos*-1
    if passos == 0:
        passos = 1
    print(f'Contagem de {inicio} até {fim} de {passos} em {passos}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end =' ')
            cont += passos
        print('Fim!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            cont -= passos
        print('Fim!')

contador(1,10,1)
contador(10,0,2)
print('Sua Vez')
ini = int(input('Inicio: '))
fi = int(input('Fim:     '))
pas = int(input('Passo:  '))
contador(ini,fi,pas)