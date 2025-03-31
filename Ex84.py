pessoas = []
dados = []
cadastro = 0
pesados = ['pessoa',0]
leves = ['pessoa', 500]
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    cadastro += 1
    resp = str(input('Deseja continuar ? [S/N]')).strip().upper()
    if resp == 'N':
        break
for peso in pessoas:
    if peso[1] >= pesados[1]:
        pesados = peso
    if peso[1] <= leves[1]:
        leves = peso
print(f'Foram cadastrados {cadastro} pessoas.')
print(f'{pesados[0]} tem o maior peso de {pesados[1]:.2f}Kg')
print(f'{leves[0]} tem o menor peso de {leves[1]:.2f}Kg')