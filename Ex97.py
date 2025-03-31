def frase (txt):
    tamanho = len(txt) +4
    print('~'*tamanho)
    print(f'{txt:^{tamanho}}')
    print('~'*tamanho)

frase(input('Digite a frase: '))