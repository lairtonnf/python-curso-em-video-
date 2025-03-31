n = int(input('Digite um valor inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[m')
print('o número {} foi divisivel {} vezes'.format(c,tot))
if tot == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO È PRIMO!')
