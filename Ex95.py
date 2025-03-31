jogadores = list()
gols = list ()
print(f'='*25)
print(f'APROVEITAMENTO DOS JOGADORES')
print(f'='*25)
while True:
    dados = dict ()
    gol = list ()
    dados ['nome'] = str(input('Nome : ')).strip().capitalize()
    partidas = int(input('Partidas Jogadas: '))
    tot = 0
    for jogo in range (0, partidas):
        goll = int(input(f'Gols na {jogo+1}° Partida: '))
        gol.append(goll)
        tot += goll
    gols.append(gol[:])
    gol.clear()
    dados ['total'] = tot
    jogadores.append(dados.copy())
    resp = str(input('Deseja Continuar? [S/N]')).strip().upper()
    if resp == 'N': break
print(f'='*38)
print(f'{'Cod.'} {'Nome'} {'Gols':>12} {'Total':>15}')
print(f'-'*38)
for x,jogador in enumerate(jogadores):
   print(f'{x:<5}{jogador['nome']:<13}{format(gols[x]):<15}{jogador['total']}')
print(f'-'*38)
while True:
    escolha = int(input(f'Deseja Vizualizar os Dados de Qual Jogador? (999 para parar) '))
    if escolha == 999: break
    if escolha >= len(jogadores): print(f'ERRO! Código {escolha} Não Encontrado!')
    else:
        print('-'*43)
        print(f'LEVAMTAMENTO DO JOGADOR: {jogadores[escolha]['nome']}')
        for j,g in enumerate(gols[escolha]):
            print(f'No {j+1}º Jogo Fez {gols[escolha][j]} Gols')
