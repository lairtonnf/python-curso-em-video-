list = []
cont = 0
while True:
    list.append(int(input(f'Digite um número: ')))
    cont += 1
    resp = str(input(f'Deseja continuar? [S/N] ')).strip().upper()
    while resp not in 'SN':
        resp= str(input(f'Resposta incorreta! Deseja continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
if 5 in list:
    print(f'O número 5 foi encontrado na lista')
else:
    print(f'O número 5 não foi encontrado na lista')
print(f'{cont} números foram digitados')
print(f'Lista decrescente : {sorted(list,reverse=True)}')