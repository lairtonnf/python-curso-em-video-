alunos = []
dados = []
while True:
    dados.append(str(input('Nome do aluno: ')).strip().capitalize())
    dados.append(float(input('Primeira nota: ')))
    dados.append(float(input('Segunda nota: ')))
    m = (dados[1] + dados[2]) / 2
    dados.append(m)
    alunos.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print(f'{'N°':<3}  {'NOME':<7}  {'MÉDIA':>3}')
print(f'-'*20)
for n, dd in enumerate(alunos):
    print(f'{n:<4} {dd[0]:<7} {dd[3]:4.1f}')