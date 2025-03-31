from random import randint
computador = randint (1,20)
resultado = cont = 0
par = 'p'
impar = 'i'
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I] ')).strip().lower()[0]
    resultado = computador + jogador
    if escolha == 'p':
        if resultado % 2 == 0:
            cont += 1
            print(f'Você jogou {jogador} e o computador {computador}. No total de {resultado} deu PAR')
            print(f'Você GANHOU!!!')
            print(f'Você venceu {cont} vez.')
        else:
            print(f'Você jogou {jogador} e o computador {computador}. No total de {resultado} deu IMPAR')
            print(f'Você PERDEU!!')
            print(f'Você venceu {cont} vez.')
            break
    if escolha == 'i':
        if resultado % 2 == 1:
            cont += 1
            print(f'Você jogou {jogador} e o computador {computador}. No total de {resultado} deu INPAR')
            print(f'Você GANHOU!!!')
            print(f'Você venceu {cont} vez.')
        else:
            print(f'Você jogou {jogador} e o computador {computador}. No total de {resultado} deu PAR')
            print(f'Você PERDEU!!!')
            print(f'Você venceu {cont} vez.')
            break



