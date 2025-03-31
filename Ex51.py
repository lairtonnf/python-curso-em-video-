print('PROGRESSÂO ARITMÉTRICA')
pt = int(input("Primeiro termo: "))
razão = int(input('Razão: '))
decimo = pt + (10-1) * razão
r = 0
for c in range(pt,decimo + razão,razão):
    print('{} '.format(c), end= ' > ')
print('ACABOU')
