matriz = [[],[],[]]
par = 0
s_tcoluna = 0
for p in range (0,3):
    num = int(input(f'Digite o valor para [0,{p}]: '))
    matriz[0].append(num)
    if num %2 == 0:
        par += num
    if p == 2:
        s_tcoluna += num
for s in range (0,3):
    num = int(input(f'Digite o valor para [1,{s}]: '))
    matriz[1].append(num)
    if num %2 == 0:
        par += num
    if s == 2:
        s_tcoluna += num
for t in range (0,3):
    num = int(input(f'Digite o valor para [2,{t}]: '))
    matriz[2].append(num)
    if num %2 == 0:
        par += num
    if t == 2:
        s_tcoluna += num
print('='*20)
print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]')
print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')
print(f'Soma dos valores pares: {par}')
print(f'Soma dos valores da terceira coluna: {s_tcoluna}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')
