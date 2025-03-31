matriz = [[],[],[]]
for primeiro in range (0,3):
    num = int(input(f'Digite o valor para [0,{primeiro}]: '))
    matriz[0].append(num)
for segundo in range (0,3):
    num = int(input(f'Digite o valor para [1,{segundo}]: '))
    matriz[1].append(num)
for terceiro in range (0,3):
    num = int(input(f'Digite o valor para [2,{terceiro}]: '))
    matriz[2].append(num)
print(f'[{matriz[0][0]}][{matriz[0][1]}][{matriz[0][2]}]')
print(f'[{matriz[1][0]}][{matriz[1][1]}][{matriz[1][2]}]')
print(f'[{matriz[2][0]}][{matriz[2][1]}][{matriz[2][2]}]')
