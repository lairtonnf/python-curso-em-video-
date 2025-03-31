valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite {c}° valor: ')))
print(f'Valores digitados : {valores}')
print(f'O maior valor é : {max(valores)} na posição : {valores.index(max(valores))}')
print(f'O menor valor é : {min(valores)} na posição : {valores.index(min(valores))}')

