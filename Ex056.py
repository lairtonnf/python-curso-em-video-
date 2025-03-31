somaidade = 0
nomevelho = ''
maioridadehomem = 0
mulheres_menos_20 = 0
for c in range (1,3):
    nome = str(input('Nome da {}° pessoa: '.format(c))).strip()
    idade = int(input('Idade da {}° pessoa: '.format(c)))
    sexo = str(input('Sexo da {}° pessoa [M/F]: '.format(c))).strip()
    print('-'*30)
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_menos_20 += 1
media = somaidade/4
print('A média de idade do grupo é {:.1f} anos'.format(media))
print('O homem mais velho é {} e tem {} anos'.format(nomevelho,maioridadehomem))
print('{} mulheres tem menos de 20 anos'.format(mulheres_menos_20))
