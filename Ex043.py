peso = float(input('Digite o peso em Kg: '))
altura = float(input('Digite a altura em M:'))
imc = peso/(altura*altura)
print('Seu IMC é {:.1f}Kg/m²'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc <=30:
    print('Sobrepeso')
else:
    print('Obesidade mórbida')