print('PROGRESSÂO ARITMÉTRICA')
pt = int(input("Primeiro termo: "))
razão = int(input('Razão: '))
r = 0
print('{} '.format(pt), end='> ')
while r < 9:
    pt = pt + razão
    print('{} '.format(pt), end = '')
    print('> ' if r < 8 else ' ', end= '')
    r += 1