soma = numero = cont = 0
while True:
    numero = int(input('Digite um valor (999 PARA PARAR): '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'Foram digitados {cont} números e a soma é {soma}')

