print("""
068) Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no
final do jogo.
""")

from random import randint

numeroDoComputador = randint(0, 5)
contador = soma = 0
perdeu = 'Você perdeu!'
venceu = 'Você venceu!'

while True: # WHILE 1: Coleta o número usuário
    numeroDoJogador = input('Escolha um número entre 0 e 5: ').strip()

    if not numeroDoJogador.isnumeric():
        continue
    else:
        numeroDoJogador = int(numeroDoJogador)

        if numeroDoJogador < 0 or numeroDoJogador > 5:
            continue
        else:
            while True: # WHILE 2: Coleta a escolha do usuário (par ou ímpar)
                jogada = str(input('Par ou ímpar? [p/i]: ').strip().lower())

                if jogada != 'p' and jogada != 'i':
                    continue
                else:
                    soma = numeroDoComputador + numeroDoJogador

                    if soma%2 == 0:
                        if jogada == 'p':
                            resultado = venceu
                        else:
                            resultado = perdeu
                    else:
                        if jogada == 'i':
                            resultado = venceu
                        else:
                            resultado = perdeu
                    print(resultado)
                    break # SAIDA do WHILE 2
    
    if resultado == venceu:
        contador += 1
    else:
        break # Saída do WHILE 1

print('Você venceu {} vez(es).'.format(contador))
