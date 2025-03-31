mais_de_dezoito = tot_homens = mulheres_menos_vente = 0
resposta = ''
while True:
    print(f'===== CADASTRE UMA PESSOA =====')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower().strip()[0]
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).lower().strip()[0]
    if idade > 18: mais_de_dezoito += 1
    if sexo == 'm': tot_homens += 1
    if sexo == 'f' and idade <20: mulheres_menos_vente +=1
    resposta = str(input('Deseja continuar [S/N] ?')).strip().lower()[0]
    while resposta not in 'sn':
        resposta = str(input('Deseja continuar [S/N] ?')).strip().lower()[0]
    if resposta == 'n':
        break
print('===== Fim do programa =====')
print(f'Foram cadastrados {mais_de_dezoito} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {tot_homens} homens.')
print(f'Foram cadastrados {mulheres_menos_vente} mulheres com menos de 20 anos.')
