print("""
073) Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
A) Os 5 primeiros
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da chapecoense.
""")

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 
'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 
'Botafogo', 'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense',
'Sport Recife', 'EC Vitória', 'Coritiba', 'Avai', 'Ponte Preta',
'Atletico-GO')
print('-=' * 15)
print ('Os 5 primeiros times são: {} '.format(times[0:5]))
print('-=' * 15)
print('Os últimos 4 colocados são: {}'.format(times[-4:]))
print('-=' * 15)
print('Os times em ordem alfabética são: {}'.format(sorted(times)))
print('-=' * 15)
print('A Chapecoense está na {} posição '.format(times.index('Chapecoense')+1))
print('-=' * 15)