times = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo','Corinthias',
         'Bahia','Cruzeiro','Vasco da Gama','EC Vitória','Atlético-MG','Fluminense','Grêmio'
         ,'Juventude','Bragantino','Athlético-PR','Criciúma','Atlético-GO','Cuiabá')
print(f'Os 5° primeiros colocados')
for c in range (0,5): print(f'{times[c]}')
print(f'Os 4° últimos colocados')
for c in range (16,20): print(f'{times[c]}')
print(f'Listagem em ordem alfabetica')
print(sorted(times))
print(f'O Criciúma esta na posição {times.index('Criciúma')}')

