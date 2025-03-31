from random import sample
valores = tuple(sample(range(10),5))
print(f'Listagem de números aleatórios {valores}')
print(f'O maior número é {max(valores)}')
print(f'O menor número é {min(valores)}')