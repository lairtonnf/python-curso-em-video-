alunos = list ()
while True:
    dados = dict()
    dados ['nome'] = str(input('Nome: ')).strip().capitalize()
    dados ['média'] = float(input('Média: '))
    if dados['média'] >= 7:
        dados ['resultado'] = 'Aprovado'
    if dados['média'] <= 6.9:
        dados ['resultado'] = 'Reprovado'
    alunos.append(dados.copy())
    resp = str(input('Continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print(f'='*20)
for x in alunos:
    print(f'Aluno:{x['nome']}')
    print(f'Média:{x['média']:.1f}')
    print(f'Situação:{x['resultado']}')
    print(f'-'*20)
