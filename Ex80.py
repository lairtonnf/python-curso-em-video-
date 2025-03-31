lista = []
for n in range(0, 5):
    num = int(input(f'Digite o valor {n+1}°: '))
    if n == 0: lista.append(num)
    elif num >= lista[-1]: lista.append(num)
    elif num <= lista[0]: lista.insert(0, num)
    else:
        for i in range(1, len(lista)):#Esse loop começa no índice 1 e vai até o último índice da lista.
            if lista[i-1] <= num <= lista[i]:#Essa condição verifica se o número num está dentro do intervalo entre o elemento anterior e o elemento atual.
                lista.insert(i,num)
                break
    print(lista)

