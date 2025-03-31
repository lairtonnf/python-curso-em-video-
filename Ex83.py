expressão = str(input('Digite a expressão: '))
condição =  []
r = 0
for c in expressão:
    if c == '(':
     condição.append(1)
    elif c == ')':
        if not condição:
            print('invalido')
        condição.pop()
if not condição:
    print(f'Expressão Valida!')
else:
    print(f'Expressão Inválida!')

#        condição.append(1)
#for f in condição:
#   r = f + r
#if r %2 == 0:
#    print('Expressão valida!')
#else:
#    print('Expressão invalida!') #maneira porca e com brecha

