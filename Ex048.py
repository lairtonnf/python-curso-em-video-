cont = 0
r = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        r += c
print('''Soma entre todos os {} números impares multiplos de trés entre 1 ate 500: 
{}'''.format(cont,r))
