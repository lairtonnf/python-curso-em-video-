from random import randint
lista = list ()
def sorteia():
    for x in range(0,5):
        numero = randint(0,10)
        lista.append(numero)
    print(F'Lista de números : {lista}')

def somapar(numeros):
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(f'Soma dos valores pare: {soma}')

sorteia()
somapar(lista)