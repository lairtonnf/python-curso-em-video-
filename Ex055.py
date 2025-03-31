maior = 0
menor = 0
for c in range (1,6):
    peso = float(input('Pessoa da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('{:.1f}Kg maior peso'.format(maior))
print('{:.1f}Kg menor peso'.format(menor))

