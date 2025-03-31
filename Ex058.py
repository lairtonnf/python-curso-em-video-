from random import  randint
print('MINIGAME - TENTE ADIVINHAR O NÚMERO!')
numero = randint(0,10)
cont = 0
jogador = int(input('Digite um valor de 0 a 10: '))
cont += 1
while jogador != numero:
    if jogador > numero:
        jogador = int(input('Menos... Tente de novo: '))
        cont += 1
    else:
        jogador = int(input('Mais... Tente de novo: '))
        cont += 1
print('Parabêns!! você venceu a máquina, depois de {} tentativas '.format(cont))
