valores = []
resposta = 's'
while resposta == 's':
    valor = int(input('Digite um número : '))
    if valor in valores:
        print(f'Número já existe!')
    else:
        valores.append(valor)
        print(f'Número adicionado..')
    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).lower().strip()
        if resposta not in 'SsNn': resposta = str(input('Resposta incorreta.. Deseja continuar ? [S/N]'))
        else:
            break
valores.sort()
print(f'Número digistados : {valores}')
