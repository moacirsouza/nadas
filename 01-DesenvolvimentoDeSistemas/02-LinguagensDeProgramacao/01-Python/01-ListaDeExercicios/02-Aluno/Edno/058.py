# (01-Gabarito/058.py)) Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

numero = randint(0,10)

adivinha = -1
tentativas = 0

while adivinha != numero:
    if tentativas > 0:
        print('Errô-ôu!')
        print('')
    adivinha = int(input('Qual foi o número que eu pensei??? '))
    tentativas = tentativas + 1


print('Você acertou em {} tentativas'.format(tentativas))