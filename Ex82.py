lista = []
par = []
impar = []
num = 0
while True:
    num = (int(input('Digite um número: ')))
    lista.append(num)
    if num %2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Resposta incorreta! Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'Lista Pares: {par}')
print(f'Lista Impares: {impar}')
print(f'Lista: {lista}')