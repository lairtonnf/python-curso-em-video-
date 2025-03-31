valores = [[],[]]
for c in range (1,8):
    num = int(input(f'Digite {c}° o valor: '))
    if num %2 == 0:
        valores[0].append(num)
    if num %2 == 1:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print('='*20)
print(f'Valores pares: {valores[0]}')
print(f'Valores ímpares: {valores[1]}')