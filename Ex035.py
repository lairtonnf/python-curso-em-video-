r1 = int(input('Comprimento da primeira reta: '))
r2 = int(input('Comprimento da segunda reta: '))
r3 = int(input('Comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As 3 retas \033[32mpodêm\033[m formar um triângulo!')
else:
    print('As 3 retas \033[31mnão podem\033[m formar um triângulo!')
