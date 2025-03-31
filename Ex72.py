numero = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis',
          'Sete','Oito','Nove','Dez','Onze','Doze','Treze',
          'Quatorze','Quinze','Dezesseis','Dezessete','Dezoito',
          'Dezenove','Vinte')
c = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= c <= 20:
        break
    c = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
print(numero[c])
