print("""
068) Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no
final do jogo.
""")

from random import randint

numeroDoComputador = randint(0, 5)
escolhaDoComputador = randint(0,1)
parOuImpar = ('PAR', 'ÍMPAR')
contador = 0

while True:
    while True:
        numeroDoJogador = int(input('Escolha um número entre 0 e 5: ').strip())

        if numeroDoJogador < 0 or numeroDoJogador > 5:
            continue
        else:
            break

    while True:
        jogada = str(input('Par ou ímpar? [P/I]').strip())

        if jog

    break
