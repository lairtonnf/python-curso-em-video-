valor = 0
soma = 0
cont = -1
while valor != 999:
    valor = int(input('Digite um valor: '))
    soma += valor
    cont += 1
print('Você digitou {} números e a soma deles é {}'.format(cont,soma-999))
