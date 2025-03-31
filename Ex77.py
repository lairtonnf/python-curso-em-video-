palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar','trabalhar',
            'mercado','programador','futuro')
vogais = 'aeiou'
for palavra in palavras:
    print(f'A palavra {palavra} tem as vogais : ',end='')
    for vogal in palavra:
        if vogal in vogais:
            print(f'{vogal}', end=' ')
    print()
