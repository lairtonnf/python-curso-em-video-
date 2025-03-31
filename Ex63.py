from hmac import trans_36

print('SEQUÊNCIA DE FIBONACCI')
termos = int(input('Quantos termos você quer mostrar: '))
inicio = 3
primeiro = 0
segundo = 1
terceiro = 1
print('{} > {} '.format(primeiro, segundo), end='> ')
while inicio <= termos:
    print('{} '.format(terceiro), end= '> ')
    primeiro = segundo
    segundo = terceiro
    terceiro = primeiro + segundo
    inicio += 1
print('FIM')

