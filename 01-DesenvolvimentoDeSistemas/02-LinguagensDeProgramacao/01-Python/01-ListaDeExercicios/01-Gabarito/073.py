print("""
073) Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição da tabela está o time Chapecoense.
""")

tabela2018 = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 
              'São Paulo', 'Atlético', 'Athletico Paranaense', 'Cruzeiro', 
              'Botafogo', 'Santos', 'Bahia', 'Fluminense', 
              'Corinthians ', 'Chapecoense', 'Ceará', 'Vasco da Gama', 
              'America Fc', 'Sport', 'Vitória', 'Paraná')

print(f'Lista completa, ordenada, dos 20 colocados do Campeonato Brasileiro de 2018: {tabela2018}\n')
print(f'A) Os cinco primeiros colocados foram: {tabela2018[:5]}')
print(f'B) Os quatro últimos colocados foram: {tabela2018[-4:]}')
print(f'C) Lista dos times em ordem alfabética: {sorted(tabela2018)}')
print(f'D) O Chapecoense está em {tabela2018.index("Chapecoense")+1}º lugar.')
