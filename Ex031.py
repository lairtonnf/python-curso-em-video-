km = float(input('Distância da viajem em km: '))
if km <=200:
    print('O valor da passagem sera \033[1;34m{:.2f}\033[mBRL'.format(km*0.50))
else:
    print('O valor da passagem sera \033[1;34m{:.2f}\033[mBRL'.format(km*0.45))
