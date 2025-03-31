from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento
if idade < 10:
    print('Este atleta tem {} anos e esta na categoria MIRIM'.format(idade))
elif idade >9 and idade <15:
    print('Este atleta tem {} anos e esta na categoria INFANTIL'.format(idade))
elif idade >14 and idade <20:
    print('Este atleta tem {} anos e esta na categoria JUNIOR'.format(idade))
elif idade == 20:
    print('Este atleta tem {} anos e esta na categoria SêNIOR'.format(idade))
else:
    print('Este atleta tem {} anos e esta na categoria MASTER'.format(idade))