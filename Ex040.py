n1 = float(input('Primeira média: '))
n2 = float(input('Segunda média: '))
m = (n1+n2)/2
if m < 5:
    print('REPROVADO')
elif m >5 and m < 6.9:
    print('RECUPERAÇÂO')
elif m > 7:
    print('APROVADO')