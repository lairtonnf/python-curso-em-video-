frase = str(input('Digite uma palavra: ')).strip().lower()
inverso = frase[::-1]
if frase == inverso:
    print('Palindromo')
else:
    print('Não palidromo')
