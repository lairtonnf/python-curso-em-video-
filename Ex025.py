nome = str(input('Digite o nome: '))
if 'silva' in nome.lower():
    print('Tem \033[32msilva\033[m no nome')
else:
    print('Não tem \033[32msilva\033[m no nome')
