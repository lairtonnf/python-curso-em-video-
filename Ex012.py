Preco = float(input('Digite o preço do produto: '))
Desconto = (Preco*5)/100
Novo_Preco = Preco-Desconto
print('Produto com 5% de desconto \033[32m{:.2f}\033[mBRL'.format(Novo_Preco))




