total = preço = mais_de_mil = cont = 0
nome_barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Valor do produto: '))
    while cont == 0:
        mais_barato = preço
        cont +=1
    if preço < mais_barato:
        mais_barato = preço
        nome_barato = nome
    if preço > 1000: mais_de_mil += 1
    total = total + preço
    resposta = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    while resposta not in 'sn':
        resposta = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    if resposta == 'n': break
print('===== RESULTADO =====')
print(f'Gasto total R${total:.2f}')
print(f'Produtos que custam mais de R$1000: {mais_de_mil}')
print(f'Produto mais barato: {nome_barato}')