c50 = c20 = c10 = c1 = 0
print('='*30)
print('{:^30}'.format('BANCO BOLO'))
print('='*30)
valor = int(input('Qual valor deseja sacar? R$'))
montante = valor
while montante >= 50:
    montante -= 50
    c50 += 1
while montante >= 20:
    montante -= 20
    c20 += 1
while montante >= 10:
    montante -= 10
    c10 += 1
while montante >= 1:
    montante -= 1
    c1 += 1
print(f'Total de cedulas de R$50: {c50}')
print(f'Total de cedulas de R$20: {c20}')
print(f'Total de cedulas de R$10: {c10}')
print(f'TOtal de cedulas de R$1: {c1}')
print('='*30)
print('Volte Sempre!! Aproveite o bolo!')
