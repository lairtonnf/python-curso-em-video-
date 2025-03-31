lista = ('Café',20.50,'Leite',7.30,'Arroz',3.70,'Feijão',4.48,'Ovo',17.60)
print('-'*30)
print(f'{'Listagem de compras':^30}')
print('-'*30)
for c in lista:
    if type(c) is str:
        print(f'{c:.<15}', end='')
    if type(c) is float:
        print(f'R${c:>6.2f}')

print('='*30)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<15}', end='')
    if pos % 2 == 1:
        print(f'R${lista[pos]:6.2f}')