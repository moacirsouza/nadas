print("""
095) Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
""")

### TODO: Reorganizar o código para promover maior legibilidade

titulo = ' Programa de Aramazenamento e aproveitamento de Jogadores '
formatador = len(titulo)
totalDeGols = 0
golsPorPartida = []
jogador = {}
time = []

print('-'*formatador)
print(titulo)
print('-'*formatador)
print(f'{"Cadastre as informações do jogador":^{formatador}}')

while True:
    nomeDoJogador = input('Nome: ')
    numeroDePartidas = int(input(f'Quantas partidas "{nomeDoJogador}" jogou? '))

    print('-'*formatador)
    for partida in range(numeroDePartidas):
        numeroDeGols = int(input(f'Número de gols na partida {partida+1}: '))
        totalDeGols += numeroDeGols
        golsPorPartida.append(numeroDeGols)

    ### O uso do método "copy()" na chave "GolsPorPartida" é necessário para
    ### evitar o acúmulo de informações dentro da lista "golsPorPartida"
    ### entre as iterações do laço principal
    jogador = dict(Nome=nomeDoJogador,
                   Partidas=numeroDePartidas,
                   TotalDeGols=totalDeGols,
                   GolsPorPartida=golsPorPartida.copy())

    time.append(jogador.copy())
    jogador.clear()

    totalDeGols = 0
    golsPorPartida.clear()

    while True:
        continuar = input('Deseja continuar? (s/n) ').strip().lower()

        if continuar == 's' or continuar == 'n':
            break
        print('Digite S/s ou N/n para prosseguir ou suspender, respectivamente.')

    if continuar == 'n':
        break

print('-'*formatador)
print(f'{"Resultados":^{formatador}}')
print('-'*formatador)
print(f'Registro - Nome - Gols por Partida - Total de Gols')

for registro, dicionario in enumerate(time):
    print(f'{registro+1:08d} - {dicionario["Nome"]} - {dicionario["GolsPorPartida"]} - {dicionario["TotalDeGols"]}')

print('-'*formatador)
print(f'{"Apresentação de Resultado por Jogador":^{formatador}}')
print('-'*formatador)

while True:
    sair = int(input('Registro do jogador (999 para sair): ').strip())

    if sair == 999:
        print('FIM')
        break
    
    dadosDoJogador = time[sair-1]
    nome = dadosDoJogador['Nome']
    gols = dadosDoJogador['GolsPorPartida']

    print(f'Resumo para o jogador {nome}')
    for jogo, gol in enumerate(gols):
        print(f'Jogo {jogo+1}: {gol} gol(s)')
