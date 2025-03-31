Salario = float(input('Salário do funcionário: '))
# Aumento = (Salario*15)/100
Novo_Salario = Salario + (Salario*15/100)
print('Novo salário do funcionário \033[32m{:.2f}\033[mBRL'.format(Novo_Salario))


