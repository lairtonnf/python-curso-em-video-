print('PROGRESSÂO ARITMÉTRICA')
pt = int(input("Primeiro termo: "))
razão = int(input('Razão: '))
r = 1
total = 0
mais = 10
print('{} '.format(pt), end='> ')
while mais != 0:
    total = total + mais
    while r < total:
        pt = pt + razão
        print('{} > '.format(pt), end = '')
        r += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
