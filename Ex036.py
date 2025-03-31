valor_da_casa = float(input('Informe o valor da casa: '))
salario_comprador = float(input('Informe o salário do comprador: '))
parcelas = int(input('Informe em quantos anos sera pago: '))
prestaçao = ((valor_da_casa)/(parcelas*12))
if prestaçao < (salario_comprador*30)/100:
    print('Emprestimo aprovado, no valor de R${:.2f} mensais por {} anos.'.format(prestaçao,parcelas))
else:
    print('Emprestimo negado.')



