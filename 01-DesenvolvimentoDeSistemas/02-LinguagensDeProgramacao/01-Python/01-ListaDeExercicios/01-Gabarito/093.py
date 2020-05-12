print("""
093) Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai
ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
""")

titulo = ' Programa de Aramazenamento e Aproveitamento de Jogadores '
formatador = len(titulo)
totalDeGols = 0
golsPorPartida = []

aproveitamento = dict(Nome='',
                      Partidas=0,
                      GolsPorPartida=[])

print('-'*formatador)
print(f'{titulo:^{formatador}}')
print('-'*formatador)
print(f'{"Cadastre as informações do jogdor":^{formatador}}')
nomeDoJogador = input('Nome: ')
numeroDePartidas = int(input(f'Quantas partidas {nomeDoJogador} jogou? '))

print('-'*formatador)
for partida in range(numeroDePartidas):
    numeroDeGols = int(input(f'Número de gols na partida {partida+1}: '))
    totalDeGols += numeroDeGols
    golsPorPartida.append(numeroDeGols)

aproveitamento.update(dict(Nome=nomeDoJogador,
                           Partidas=numeroDePartidas,
                           TotalDeGols=totalDeGols,
                           GolsPorPartida=golsPorPartida))

print(aproveitamento)
