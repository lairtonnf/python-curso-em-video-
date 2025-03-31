from datetime import datetime
dados = dict ()
dados ['nome'] = str(input('Nome: ')).strip().capitalize()
dados ['sexo'] = str(input('Sexo:[M/F] ')).strip().capitalize()
nasci = int(input('Ano de Nascimento: '))
atual = datetime.now().year
dados ['idade'] = atual - nasci
dados ['carteira de trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['carteira de trabalho'] >0:
    dados ['contratação'] = int(input('Ano de Contratação: '))
    dados ['salário'] = float(input('Salário: R$'))
    tempo_contr = atual - dados['contratação']
print('='*30)
print(f'Nome: {dados['nome']}')
print(f'Sexo: {dados['sexo']}')
print(f'Idade: {dados['idade']}')
print(f'CTPS: {dados['carteira de trabalho']}')
if dados['carteira de trabalho'] >0:
    print(f'Ano de contratação: {dados['contratação']}')
    print(f'Salário: R${dados['salário']:.2f}')
if dados['sexo'] == 'M':
    print(f'Tempo de Contribuição Necessária: 65 anos de idade e {20-tempo_contr} anos de contribuição')
if dados['sexo'] == 'F':
    print(f'Tempo de Contribuição Necessária: 62 anos de idade e {15-tempo_contr} anos de contribuição')
