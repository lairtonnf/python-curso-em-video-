salario = float(input('Salário do funcionário: '))
if salario <= 1250:
    print('O novo salário sera de \033[32m{:.2f}\033[mBRL'.format(salario+(salario*15)/100))
else:
    print('O novo salário sera de \033[32m{:.2f}\033[mBRL'.format(salario+(salario*10)/100))

