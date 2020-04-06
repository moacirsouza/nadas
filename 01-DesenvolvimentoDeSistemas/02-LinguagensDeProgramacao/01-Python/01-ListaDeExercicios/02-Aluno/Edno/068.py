# (01-Gabarito/068.py)) Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.
# Mas tá valendo.

from random import randint

ganhou = True
tipo = ['Par','Ímpar']
print('*' * 100)
vitorias = 0
total = 0
while ganhou:
    total += 1
    soma = 0
    pc = randint(1,10)
    pc_eh = randint(0,1)
    print('Eu sou {}'.format(tipo[pc_eh]))

    usuario = int(input('Digite um número\t: '))

    soma = pc + usuario

    resultado = soma%2
    resultado == pc_eh

    print('Eu escolhi {}. Você escolheu {}. {} é {}'.format(pc, usuario, soma, tipo[soma%2]))
    print('*'*100)

    if resultado:
        ganhou = False
    else:
        vitorias += 1


print('Você obteve {} vitórias em {} partidas.'.format(vitorias, total))