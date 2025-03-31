from random import randint
itens = ['Pedra','Papel','Tesoura']
pc = randint(0,2)
print('JOKENPÔ')
print('''Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Escolha sua jogada: '))
print('-'*20)
print('Computador jogou {}'.format(itens[pc]))
print('Você jogou {}'.format(itens[jogador]))
print('-'*20)
if pc == 0:
    if jogador == 0:
       print('EMPATE')
    elif jogador == 1:
        print('Você ganhou')
    elif jogador == 2:
        print('Você perdeu')
    else:
        print('Opção invalida')
if pc == 1:
    if jogador == 0:
        print('Você perdeu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Você ganhou')
    else:
        print('Opção invalida')
if pc == 2:
    if jogador == 0:
        print('Você ganhou')
    elif jogador == 1:
        print('Você perdeu')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Opção invalida')