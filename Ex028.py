import random
print('MINIGAME - TENTE ADIVINHAR O NÚMERO')
numero = random.randint(0,5)
escolhido = int(input('Digite um valor de 0 a 5: '))
if escolhido == numero:
    print('\033[1;32mVenceu\033´m!!!')
else:
    print('\033[1;31mPerdeu XD\033[m')
print('O número era \033[32m{}'.format(numero))
