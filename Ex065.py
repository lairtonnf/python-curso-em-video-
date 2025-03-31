girador = ''
resposta = 'N'
média = soma = cont = maior = menor = 0
while girador != resposta:
    numero = int(input('Digite um valor: '))
    girador = str(input('Digite continuar [S/N]: ').upper()).strip()[0]
    cont += 1
    soma += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
média = soma / cont
print('A média entre os valores digitados é {:.1f}'.format(média))
print('O maior número é {} e o menor número é {}'.format(maior,menor))
