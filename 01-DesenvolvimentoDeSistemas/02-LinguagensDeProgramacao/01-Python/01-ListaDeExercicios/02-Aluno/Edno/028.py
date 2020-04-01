# (01-Gabarito/028.py)) Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário vendeu ou perdeu.

from time import sleep
from random import randint

print('')
print('Vou pensar em um número de 0 a 5. Será que você adivinha?')
for i in range(1,5):
    print('Pensando...')
    sleep(0.3)

pensei = randint(0,5)

numero = int(input('Pronto. Qual é o número que eu pensei?'))

if numero <0 or numero >5:
    print('Seu jumento! Qual parte do "de 0 a 5" você não entendeu?')
else:
    if numero == pensei:
        print('Parabéns, você acertou. Eu pensei em ' + str(pensei))
    else:
        print('Eita. Quase. Eu tinha pensado em ' + str(pensei))

