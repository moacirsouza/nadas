print("""
068) Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no
final do jogo.
""")

from random import randint

numeroDoComputador = randint(0, 5)
# escolhaDoComputador = randint(0,1)
# parOuImpar = ('PAR', 'ÍMPAR')
contador = 0
soma = 0
perdeu = 'Você perdeu!'
venceu = 'Você venceu!'

while True:
    numeroDoJogador = int(input('Escolha um número entre 0 e 5: ').strip())

    # if numeroDoJogador < 0 or numeroDoJogador > 5:
    #     continue
    # else:
    #     break

    while True:
        jogada = str(input('Par ou ímpar? [p/i]: ').strip().lower())

        soma = numeroDoComputador + numeroDoJogador

        if soma%2 == 0:
            if jogada == 'p':
                resultado = venceu
            else:
                resultado = perdeu
        else:
            if jogada == 'i':
                resultado = perdeu
            else:
                resultado = venceu
        print(resultado)
        break
    
    if resultado == venceu:
        contador += 1
    else:
        break
print('Você venceu {} vez(es).'.format(contador))