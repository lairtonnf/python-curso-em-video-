from time import sleep
from random import randint
from operator import itemgetter
jogadores = {'Jogador1': 0, 'Jogador2': 0, 'Jogador3': 0, 'Jogador4': 0}
for jogada in jogadores:
    dado = randint(1,6)
    jogadores[jogada] = dado
print(f'Valores Sorteados:')
for j in jogadores:
    sleep(1)
    print(f'{j} tirou {jogadores[j]}')
print(f'Ranking dos jogadoes:')
rank = (sorted(jogadores.items(),key=itemgetter(1),reverse=True)) #ordena o dicinario (1) seguindo o numero
for x, y in enumerate(rank):
    sleep(1)
    print(f'{x+1}°Lugar: {y[0]} com {y[1]} pontos')


