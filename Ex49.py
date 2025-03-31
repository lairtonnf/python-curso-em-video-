mult = 0
n = int(input('Digite um numero: '))
print('-' * 11)
for c in range(1,11):
    mult += 1
    valor = n*c
    print('{} X {:2} = {}'.format(n, mult, valor))
