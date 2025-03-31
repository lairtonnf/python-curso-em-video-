pessoas = list ()
mulheres = list()
acimdamedia = list()
tot = 0
while True:
    dados = dict()
    dados ['nome'] = str(input('Nome: ')).strip().capitalize()
    dados ['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    dados ['idade'] = int(input('idade: '))
    if dados ['sexo'] == 'F': mulheres.append(dados.copy())
    pessoas.append(dados.copy())
    dados.clear()
    tot += 1
    resp = str(input('Deseja Continuar? [S/N] ')).strip().upper()
    if resp == 'N': break
totmed = 0
for pessoa in pessoas:
    idades = pessoa['idade']
    totmed += idades
for pessoa in pessoas:
    if pessoa['idade'] >= totmed/tot:
        acimdamedia.append(pessoa)
print(f'=> Foram Registradas {tot} Pessoas')
print(f'=> Média de idade: {totmed/tot} anos')
print(f'* Todas mulheres')
for  mulher in mulheres:
    print(f'{mulher['nome']}', end=' ')
print()
print(f'* Pessoas Acima da Média')
for acima in acimdamedia:
    print(f'{acima['nome']}')
