nascimento = int(input('Em que ano voce nasceu: '))
idade = 2025 - nascimento
if idade < 18 :
    print('''Você ainda não pode se alistar ao serviço militar
Faltam {} anos'''.format((idade-18)*-1))
elif idade == 18:
    print('Esta na hora de se alistar ao serviço militar')
elif idade > 18:
    print('''Já passou do tempo do seu alistamento
Seu alistamento foi {} anos atras'''.format(idade-18))