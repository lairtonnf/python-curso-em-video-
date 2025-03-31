dados = dict ()
gols = list ()
print(f'='*25)
print(f'APROVEITAMENTO DO JOGADOR')
print(f'='*25)
dados ['nome'] = str(input('Nome : ')).strip().capitalize()
partidas = int(input('Partidas jogadas: '))
tot = 0
for jogo in range (0, partidas):
    gol = int(input(f'Gols na {jogo+1}° partida: '))
    gols.append(gol)
    tot += gol
print(f'{'Resultado':^25}')
print(f'O Jogador {dados['nome']} Jogou {partidas} partidas')
for x in range (0, partidas):
    print(f'Partida {x+1}: {gols[x]} Gols')
print(f'Total de {tot} Gols')