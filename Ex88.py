from random import sample
from time import sleep
print(f'JOGOS DA MEGA SENA ALEATORIOS')
print(f'='*35)
sorteio = int(input('Quantos jogos você quer que sorteie? '))
jogos = []
for a in range (0, sorteio):
    num = sample(range(1,61),6) # Sorteia 6 números únicos entre 1 e 60
    jogos.append(num)
print(f'===Sorteando {sorteio} jogos===')
for tot, jogo in enumerate(jogos):
    sleep(1)
    print(f'Jogo {tot+1}:{sorted(jogo)}')
print(f'Boa sorte!!')

