cidade = str(input('Nome da cidade: '))
separado = cidade.split()
if 'santo' in separado[0].lower():
    print('\033[32mVerdadeiro')
else:
    print('\033[31mFalso')

