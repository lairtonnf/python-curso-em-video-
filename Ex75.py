numero = (int(input('Digite um valor: ')),
          int(input('Digite o segundo valor: ')),
          int(input('Digite o terceiro valor: ')),
          int(input('Digite o quarto valor: ')))
print(f'Os números digitados foram {numero}')
if 9 in numero: print(f'O número 9 apareceu {numero.count(9)} vezes.')
else: print(f'Nenhum número 9 encontrado')
if 3 in numero: print(f'O número 3 apareceu na {numero.index(3)+1}° posição')
else: print(f'Número 3 não encontrado')
print(f'Valores pares digitados ', end='')
for c in numero:
    if c % 2 == 0:
        print( c,end= ' ')
