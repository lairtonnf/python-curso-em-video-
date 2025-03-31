valor = float(input('Digite o valor do produto: R$'))
print('''FORMAS DE PAGAMENTOS:
[1] Dinheiro/Cheque
[2] Débito
[3] 2x no cartão
[4] 3x ou mais no cartão ''')
escolha = int(input('Opção: '))
if escolha == 1:
    print('O valor a ser pago sera de R$\033[32m{:.2f}'.format(valor*(1-0.10)))
elif escolha == 2:
    print('O valor a ser pago sera de RS\033[32m{:.2f}'.format(valor*(1-0.05)))
elif escolha == 3:
    print('O valor a ser pago sera de R$\033[32m{:.2f}'.format(valor))
elif escolha == 4:
    print('O valor a ser pago sera de \033[32mR${:.2f}'.format(valor*(1+0.20)))
else:
    print('Opção Invalida')