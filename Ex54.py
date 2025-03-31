from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for c in range (1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu: '.format(c)))
    idade = hoje - nasc
    if idade >= 18:
        maior +=  +1
    else:
        menor +=  +1
print('{} pessoas não atingiram a maioridade'.format(menor))
print('{} pesssoas tem maior idade'.format(maior))


